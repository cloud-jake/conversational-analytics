import os
from flask import Flask, render_template, request, jsonify
from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables from .config file
load_dotenv(dotenv_path='.config')

app = Flask(__name__)

# Initialize BigQuery client
# The client will use Application Default Credentials (ADC)
# to authenticate. Ensure you have run 'gcloud auth application-default login'.
try:
    project_id = os.environ.get("PROJECT_ID")
    if not project_id:
        raise ValueError("PROJECT_ID not found in .config file.")
    bigquery_client = bigquery.Client(project=project_id)
except Exception as e:
    print(f"Error initializing BigQuery client: {e}")
    bigquery_client = None

@app.route('/')
def index():
    """Renders the main web interface."""
    return render_template('index.html')

@app.route('/api/query', methods=['POST'])
def handle_query():
    """Handles API requests to query BigQuery."""
    if not bigquery_client:
        return jsonify({"error": "BigQuery client not initialized. Check server logs."}), 500

    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. 'query' field is missing."}), 400

    user_query = data['query']
    dataset_id = os.environ.get("BIGQUERY_DATASET")
    table_id = os.environ.get("BIGQUERY_TABLE")

    if not dataset_id or not table_id:
        return jsonify({"error": "BIGQUERY_DATASET or BIGQUERY_TABLE not configured."}), 500

    # This is a simplified approach. For a real-world demo, you might use
    # a GenAI model (like Gemini) to translate the natural language `user_query`
    # into a more complex SQL query.
    # For now, we'll do a simple text search on the 'transcript' column.
    sql_query = f"""
        SELECT *
        FROM `{project_id}.{dataset_id}.{table_id}`
        WHERE STRPOS(LOWER(transcript), LOWER(@query_text)) > 0
        LIMIT 25
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("query_text", "STRING", user_query)]
    )

    try:
        query_job = bigquery_client.query(sql_query, job_config=job_config)
        results = [dict(row) for row in query_job.result()]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": f"An error occurred while querying BigQuery: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)