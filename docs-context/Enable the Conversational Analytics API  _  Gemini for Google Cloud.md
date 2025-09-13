9/13/25, 12:07 PM Enable the Conversational Analytics API \| Gemini for Google Cloud

         Enable the Conversational Analytics API
         This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms
         (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the
         launch stage descriptions (/products#product-launch-stages).



         This page describes the steps for enabling the Conversational Analytics API (accessed through
         geminidataanalytics.googleapis.com) for your Google Cloud project. The Conversational Analytics API is the first
         capability under the Data Analytics API with Gemini
         (https://console.cloud.google.com/apis/library/geminidataanalytics.googleapis.com) in the Google Cloud console.




         Before you begin
         Before you can use the Conversational Analytics API, you must have a Google Cloud project that can access the data that
         you want to work with. To set up your project, complete the following steps:

             1. Identify the data that you want to use with the Conversational Analytics API. You can use data sources like BigQuery
                tables, Looker Explores, and Looker Studio reports.

             2. In the Google Cloud console, on the project selector page, create a Google Cloud project
                (/resource-manager/docs/creating-managing-projects) that can access the data that you want to use with the
                Conversational Analytics API.



         star Note: There is no billing for the Conversational Analytics API at this time.

                Go to project selector (https://console.cloud.google.com/projectselector2/home/dashboard)




         Enable the required APIs
         To use the Conversational Analytics API, you must enable a set of required APIs (#required-apis) in your Google Cloud project.
         If you plan to use the Conversational Analytics API from a Colab Enterprise environment, you must also enable additional
         APIs (#apis-for-colab-enterprise).



         Required APIs

         Note: If you don't have permission to enable the APIs, ask your project administrator to enable the APIs for you from the APIs & Services
         dashboard (https://console.cloud.google.com/apis/dashboard). Alternatively, your project administrator can grant you the Service Usage
         Admin (roles/serviceusage.serviceUsageAdmin) (/service-usage/docs/access-control) role in the Google Cloud console, which lets you
         enable and disable APIs for the current project.




         consolegcloud (#gcloud)
             (#console)

https://cloud.google.com/gemini/docs/conversational-analytics-api/enable-the-api 1/3 9/13/25, 12:07 PM Enable the Conversational Analytics API \| Gemini for Google Cloud

             Enable the following APIs in the Google Cloud console for the Google Cloud project that you will use with the
             Conversational Analytics API.


             Enable the Gemini Data Analytics API (https://console.cloud.google.com/flows/enableapi?apiid=geminidataanalytics.googleapis.com)


             Enable the Gemini for Google Cloud API (https://console.cloud.google.com/flows/enableapi?apiid=cloudaicompanion.googleapis.com)


             Enable the BigQuery API (https://console.cloud.google.com/flows/enableapi?apiid=bigquery.googleapis.com)



       star Tip: When you enable an API, you might need to refresh the Google Cloud console page to confirm that it's enabled.


         APIs for Colab Enterprise
         If you plan to use the Conversational Analytics API from a Colab Enterprise environment, also enable the following APIs:


         Enable the Dataform API (https://console.cloud.google.com/flows/enableapi?apiid=dataform.googleapis.com)


         Enable the Compute Engine API (https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)


         Enable the Vertex AI API (https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)


         Tip: When you enable an API, you might need to refresh the Google Cloud console page to confirm that it's enabled.




         Grant required roles
         To use the Conversational Analytics API, grant the following Identity and Access Management (IAM) roles in the Google
         Cloud console to the principals (such as users or service accounts) that need to interact with the API:


         Go to Roles (https://console.cloud.google.com/iam-admin/roles)

                Gemini for Google Cloud User (roles/cloudaicompanion.user)
                (/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user): required to create conversations that are
                managed by Google Cloud.

                Looker Instance User (roles/looker.instanceUser) (/iam/docs/roles-permissions/looker#looker.instanceUser): required
                to access data from a Looker (Google Cloud core) instance

                BigQuery User (roles/bigquery.user) (/iam/docs/roles-permissions/bigquery#bigquery.user): required to access data in
                BigQuery

                BigQuery Studio User (roles/bigquery.studioUser) (/iam/docs/roles-permissions/bigquery#bigquery.studioUser): required
                if you use BigQuery Studio and data canvas

         In addition, permissions for actions like managing agents are controlled by Gemini Data Analytics roles, as described in
         Grant Conversational Analytics API IAM roles and permissions (/gemini/docs/conversational-analytics-api/access-control).

https://cloud.google.com/gemini/docs/conversational-analytics-api/enable-the-api 2/3 9/13/25, 12:07 PM Enable the Conversational Analytics API \| Gemini for Google Cloud

         Additional configuration for VPC Service Controls
         If VPC Service Controls (https://cloud.google.com/security/vpc-service-controls) is enabled for your organization or for the Google
         Cloud project that you're using, add the following APIs, which are used by the Conversational Analytics API, to the allowlist:

                From geminidataanalytics.googleapis.com, allow the following API:

                       projects.locations.chat

                From aiplatform.googleapis.com (/vertex-ai/docs/reference/rest), allow the following API:

                       projects.locations.endpoints.generateContent
                       (/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/generateContent)

                From datacatalog.googleapis.com (/data-catalog/docs/reference/rest), allow the following APIs:

                       entries.lookup (/data-catalog/docs/reference/rest#rest-resource:-v1beta1.entries)

                       catalog.search (/data-catalog/docs/reference/rest/v1/catalog/search)

                From bigquery.googleapis.com (/bigquery/docs/reference/rest), allow the following APIs:

                       jobs.query (/bigquery/docs/reference/rest/v2/jobs/query)

                       jobs.insert (/bigquery/docs/reference/rest/v2/jobs/insert)

                       jobs.getQueryResults (/bigquery/docs/reference/rest/v2/jobs/getQueryResults)

         Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License
         (https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the Apache 2.0 License
         (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies
         (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

         Last updated 2025-09-12 UTC.

https://cloud.google.com/gemini/docs/conversational-analytics-api/enable-the-api 3/3 
