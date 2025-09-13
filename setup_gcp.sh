#!/bin/bash

# This script configures the necessary Google Cloud APIs and IAM permissions
# for the Conversational Analytics demo application.

# --- Configuration ---
# Please edit the following variables with your specific details.

# Your Google Cloud Project ID.
PROJECT_ID="partarch-ecommerce-demo"

# The service account that will run the application.
# 1. Run the `create_service_account.sh` script to create a new service account.
# 2. Copy the service account email address that is output by the script.
# 3. Paste the email into the format: "serviceAccount:your-sa-email@..."
MEMBER="serviceAccount:conv-analytics-demo-sa@partarch-ecommerce-demo.iam.gserviceaccount.com"

# --- Script ---

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Pre-flight Checks ---
if ! command -v gcloud &> /dev/null
then
    echo "Error: 'gcloud' command not found."
    echo "Please install the Google Cloud CLI: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .
then
    echo "Error: Not authenticated with gcloud."
    echo "Please run 'gcloud auth login' and 'gcloud auth application-default login'."
    exit 1
fi

echo "--- Using Project: $PROJECT_ID ---"
echo "--- Granting roles to: $MEMBER ---"
echo ""

# Set the active project for gcloud
echo "1. Setting active gcloud project..."
gcloud config set project "$PROJECT_ID"
echo "   Done."
echo ""

# Enable required APIs
echo "2. Enabling required APIs (geminidataanalytics, cloudaicompanion, bigquery)..."
gcloud services enable \
    geminidataanalytics.googleapis.com \
    cloudaicompanion.googleapis.com \
    bigquery.googleapis.com
echo "   Done."
echo ""

# Grant IAM permissions
echo "3. Granting IAM roles..."

echo "   - Granting 'Gemini Data Analytics Stateless Chat User' (roles/geminidataanalytics.dataAgentStatelessUser)..."
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="$MEMBER" --role="roles/geminidataanalytics.dataAgentStatelessUser" --condition=None > /dev/null

echo "   - Granting 'BigQuery User' (roles/bigquery.user)..."
gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="$MEMBER" --role="roles/bigquery.user" --condition=None > /dev/null

echo "   Done."
echo ""

echo "--- Setup Complete! ---"
echo "Your project '$PROJECT_ID' is now configured for the Conversational Analytics demo."