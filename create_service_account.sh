#!/bin/bash

# This script creates a service account for the Conversational Analytics demo.

# --- Configuration ---
# Your Google Cloud Project ID.
PROJECT_ID="partarch-ecommerce-demo"

# The name for the new service account (e.g., 'conv-analytics-demo-sa').
SA_NAME="conv-analytics-demo-sa"

# The display name for the new service account.
SA_DISPLAY_NAME="Conversational Analytics Demo SA"

# --- Script ---
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
    echo "Please run 'gcloud auth login'."
    exit 1
fi

echo "--- Using Project: $PROJECT_ID ---"
echo ""

# Set the active project for gcloud
echo "1. Setting active gcloud project..."
gcloud config set project "$PROJECT_ID"
echo "   Done."
echo ""

# Create the service account
echo "2. Creating service account '$SA_NAME'..."
gcloud iam service-accounts create "$SA_NAME" \
    --project="$PROJECT_ID" \
    --display-name="$SA_DISPLAY_NAME"

SA_EMAIL=$(gcloud iam service-accounts list \
    --project="$PROJECT_ID" \
    --filter="name:$SA_NAME" \
    --format='value(email)')

echo ""
echo "   Service Account created successfully."
echo "   Waiting 3 seconds for IAM to propagate..."
sleep 3
echo ""
echo "--- Action Required: Grant Impersonation Permissions ---"
echo "To allow your local user to act as this service account for development,"
echo "run the following command:"
echo ""
echo "gcloud iam service-accounts add-iam-policy-binding \\"
echo "    \"$SA_EMAIL\" \\"
echo "    --member=\"user:$(gcloud config get-value account)\" \\"
echo "    --role=\"roles/iam.serviceAccountTokenCreator\""
echo ""
echo "--- Action Required: Update setup_gcp.sh ---"
echo "Copy this service account email and paste it into the 'MEMBER' variable in 'setup_gcp.sh':"
echo "$SA_EMAIL"
echo ""