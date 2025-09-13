import os
from flask import Flask, render_template, request, jsonify
from google.cloud import geminidataanalytics
from dotenv import load_dotenv

# Load environment variables from .config file
load_dotenv(dotenv_path='.config')

app = Flask(__name__)

# Initialize Conversational Analytics client
# The client will use Application Default Credentials (ADC)
# to authenticate. Ensure you have run 'gcloud auth application-default login'.
try:
    project_id = os.environ.get("PROJECT_ID")
    if not project_id:
        raise ValueError("PROJECT_ID not found in .config file.")
    data_chat_client = geminidataanalytics.DataChatServiceClient()
except Exception as e:
    print(f"Error initializing DataChatServiceClient: {e}")
    data_chat_client = None

# Load and parse the list of available BigQuery tables from the config
AVAILABLE_TABLES = [
    table.strip() for table in os.environ.get("BIGQUERY_TABLES", "").split(',') if table.strip()
]
if not AVAILABLE_TABLES:
    print("Warning: BIGQUERY_TABLES not found or empty in .config file.")

@app.route('/')
def index():
    """Renders the main web interface."""
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def handle_query():
    """Handles API requests to query BigQuery."""
    if not data_chat_client:
        return jsonify({"error": "DataChatServiceClient not initialized. Check server logs."}), 500

    data = request.get_json()
    if not data or 'query' not in data or 'table_id' not in data:
        return jsonify({"error": "Invalid request. 'query' and 'table_id' fields are required."}), 400

    user_query = data['query']
    table_id = data['table_id']

    # Security: Validate that the requested table is in our allowed list
    if table_id not in AVAILABLE_TABLES:
        return jsonify({"error": f"Invalid table_id: {table_id}. Not in allowed list."}), 400
    
    # Deconstruct the full table ID into project, dataset, and table parts
    try:
        project, dataset, table = table_id.split('.')
    except ValueError:
        return jsonify({"error": f"Invalid table ID format: {table_id}. Expected 'project.dataset.table'."}), 400

    try:
        # 1. Define the data source for the API
        bq_ref = geminidataanalytics.BigQueryTableReference(
            project_id=project, dataset_id=dataset, table_id=table
        )
        datasource_refs = geminidataanalytics.DatasourceReferences()
        datasource_refs.bq.table_references = [bq_ref]

        # 2. Set up the context for the chat (stateless)
        inline_context = geminidataanalytics.Context(
            system_instruction=os.environ.get("SYSTEM_INSTRUCTION"),
            datasource_references=datasource_refs,
        )

        # 3. Create the chat request
        messages = [geminidataanalytics.Message(user_message=geminidataanalytics.UserMessage(text=user_query))]
        request_obj = geminidataanalytics.ChatRequest(
            parent=f"projects/{project_id}/locations/{os.environ.get('LOCATION', 'global')}",
            messages=messages,
            inline_context=inline_context,
        )

        # 4. Call the API and process the streaming response
        stream = data_chat_client.chat(request=request_obj)

        generated_sql = ""
        results = []
        text_response = ""

        for reply in stream:
            if "generated_sql" in reply.system_message:
                generated_sql = reply.system_message.generated_sql
            if "text" in reply.system_message:
                text_response += "".join(reply.system_message.text.parts)
            if "data" in reply.system_message and "result" in reply.system_message.data:
                # The data comes in a structured format, convert it to a list of dicts
                fields = [field.name for field in reply.system_message.data.result.schema.fields]
                for row_data in reply.system_message.data.result.data:
                    results.append({field: row_data[field] for field in fields})

        return jsonify({
            "results": results,
            "generated_sql": generated_sql,
            "text_response": text_response
        })
    except Exception as e:
        return jsonify({"error": f"An error occurred with the Conversational Analytics API: {str(e)}"}), 500

@app.route('/api/tables', methods=['GET'])
def get_tables():
    """Returns the list of available tables to query."""
    return jsonify(AVAILABLE_TABLES)


if __name__ == '__main__':
    app.run(debug=True, port=8080)