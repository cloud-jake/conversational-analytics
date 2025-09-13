import os
from flask import Flask, render_template, request, jsonify
import logging
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
    logging.critical(f"Fatal: Could not initialize DataChatServiceClient: {e}")
    data_chat_client = None # The app will not be able to serve queries.

# Load and parse the list of available BigQuery tables from the config
AVAILABLE_TABLES = [
    table.strip() for table in os.environ.get("BIGQUERY_TABLES", "").split(',') if table.strip()
]
if not AVAILABLE_TABLES:
    app.logger.warning("BIGQUERY_TABLES not found or empty in .config file.")

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

    app.logger.info(f"Received query for table '{table_id}': '{user_query}'")

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

        app.logger.info("Sending request to Conversational Analytics API...")
        # 4. Call the API and process the streaming response
        stream = data_chat_client.chat(request=request_obj)

        app.logger.info("Processing streaming response from API...")
        generated_sql = ""
        results = []
        text_response = ""

        for reply in stream:
            system_msg = reply.system_message

            if "text" in system_msg:
                text_part = "".join(system_msg.text.parts)
                app.logger.info("API step: Received text response part.")
                app.logger.debug(f"Text content: '{text_part}'")
                text_response += text_part
            elif "data" in system_msg:
                data_msg = system_msg.data
                if "generated_sql" in data_msg:
                    generated_sql = data_msg.generated_sql
                    app.logger.info("API step: Received generated SQL.")
                    app.logger.debug(f"\n--- Generated SQL ---\n{generated_sql}\n---------------------")
                elif "result" in data_msg:
                    app.logger.info("API step: Receiving data results.")
                    fields = [field.name for field in data_msg.result.schema.fields]
                    app.logger.debug(f"Result fields: {fields}")
                    for row_data in data_msg.result.data:
                        results.append({field: row_data[field] for field in fields})
            elif "schema" in system_msg:
                app.logger.info("API step: Received schema information (not handled by UI).")
                app.logger.debug(f"Schema message: {system_msg.schema}")
            elif "chart" in system_msg:
                app.logger.info("API step: Received chart data (not handled by UI).")
                app.logger.debug(f"Chart message: {system_msg.chart}")
            else:
                app.logger.warning(f"API step: Received unhandled message type: {system_msg}")

        app.logger.info("Finished processing API stream.")
        return jsonify({
            "results": results,
            "generated_sql": generated_sql,
            "text_response": text_response
        })
    except Exception as e:
        # Log the full exception traceback to the console for debugging.
        app.logger.exception(f"An error occurred during the API call for query: '{user_query}'")
        return jsonify({"error": f"An error occurred with the Conversational Analytics API: {str(e)}"}), 500

@app.route('/api/tables', methods=['GET'])
def get_tables():
    """Returns the list of available tables to query."""
    app.logger.debug(f"Serving table list: {AVAILABLE_TABLES}")
    return jsonify(AVAILABLE_TABLES)


if __name__ == '__main__':
    app.run(debug=True, port=8080)