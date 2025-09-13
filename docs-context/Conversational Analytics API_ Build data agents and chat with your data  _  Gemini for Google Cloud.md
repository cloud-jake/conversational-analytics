9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

         Conversational Analytics API: Build data
         agents and chat with your data
         This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of
         the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and
         might have limited support. For more information, see the launch stage descriptions
         (/products#product-launch-stages).




         Important: The Data QnA API is deprecated. If you're migrating from the Data QnA API, see the migration
         guide (/gemini/docs/conversational-analytics-api/migration-guide) for an overview of key differences and
         required migration steps.



         Developers can use the Conversational Analytics API, which is accessed through
         geminidataanalytics.googleapis.com, to build an artificial intelligence (AI)-powered chat
         interface, or data agent, that answers questions about structured data in BigQuery, Looker, and
         Looker Studio using natural language. With the Conversational Analytics API, you provide your
         data agent with business information and data ("context"), as well as access to tools such as
         SQL, Python, and visualization libraries. These agent responses are presented to the user and
         can be logged by the client application, creating a seamless and auditable data chat
         experience.

         Learn how and when Gemini for Google Cloud uses your data
         (/gemini/docs/discover/data-governance).



         As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible
         but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products
         before you use it. For more information, see Gemini for Google Cloud and responsible AI
         (/gemini/docs/discover/responsible-ai).




         Note: Pre-GA Preview offerings (1) are intended for use in test environments only and shouldn't be used in a
         production environment or to process personal data or other data subject to legal or regulatory compliance
         requirements, and (2) are subject to the Pre-GA Offerings Terms of the Service Specific Terms

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 1/7 9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

         (/terms/service-terms#1), and the Consent Addendum for Gemini for Google Cloud Trusted Tester Program
         (/trusted-tester/gemini-for-google-cloud-preview).




         Get started with the Conversational Analytics API
         To start using the Conversational Analytics API, you can first review the architecture and key
         concepts (/gemini/docs/conversational-analytics-api/key-concepts) documentation to understand
         how agents process requests, the workflows for agent creators and users, conversation
         modes, and Identity and Access Management (IAM) roles. Then, to start building data agents,
         you can choose between a guided experience with the Colaboratory notebooks
         (#interactive-colab-notebooks) or a self-driven approach by following the steps in Setup and
         prerequisites (#setup).



         Interactive Colaboratory notebooks
         For an interactive, step-by-step guide to setting up your environment, building a data agent, and
         making API calls, see the following Colaboratory notebooks:

                  Conversational Analytics API HTTP Colaboratory notebook
                    (https://colab.research.google.com/github/GoogleCloudPlatform/generative-
                  ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_http.ipynb)

                  Conversational Analytics API SDK Colaboratory notebook
                    (https://colab.research.google.com/github/GoogleCloudPlatform/generative-
                  ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_sdk.ipynb)



         Setup and prerequisites
         Before you use the API or the examples, complete the following steps:

                  Enable the Conversational Analytics API
                    (/gemini/docs/conversational-analytics-api/enable-the-api): Describes prerequisites to enable
                  the Conversational Analytics API.

                  Grant Conversational Analytics API IAM roles and permissions
                    (/gemini/docs/conversational-analytics-api/access-control): Describes the predefined IAM roles
                  for managing access to data agents.

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 2/7 9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

                  Authenticate and connect to a data source with the Conversational Analytics API
                    (/gemini/docs/conversational-analytics-api/authentication): Provides instructions for
                  authenticating to the API and configuring connections to your BigQuery, Looker, and
                  Looker Studio data.



         Build and interact with a data agent
         After completing the previous steps, use the Conversational Analytics API to build and interact
         with a data agent by following these steps:

                  Build a data agent using HTTP (/gemini/docs/conversational-analytics-api/build-agent-http):
                  Provides a complete example of building and interacting with a data agent by using
                  direct HTTP requests with Python.

                  Build a data agent using the Python SDK
                    (/gemini/docs/conversational-analytics-api/build-agent-sdk): Provides a complete example of
                  building and interacting with a data agent by using the Python SDK.

                  Write effective system instructions
                    (/gemini/docs/conversational-analytics-api/data-agent-system-instructions): Learn how to
                  structure the YAML content for the system_instruction parameter to guide agent
                  behavior and improve response accuracy. You can also view examples of system
                  instructions in BigQuery data sources
                    (/gemini/docs/conversational-analytics-api/data-agent-authored-context-bq) and in Looker data
                  sources (/gemini/docs/conversational-analytics-api/data-agent-authored-context-looker).

                  Render a Conversational Analytics API agent response as a visualization
                    (/gemini/docs/conversational-analytics-api/render-visualization): Provides an example of
                  processing chart specifications from API responses and rendering them as visualizations
                  by using the Python SDK and the Vega-Altair library.




         Best practices
                  Manage BigQuery costs for your agents
                    (/gemini/docs/conversational-analytics-api/manage-costs): Learn how to monitor and manage
                  BigQuery costs for your Conversational Analytics API agents by setting project-level,
                  user-level, and query-level spending limits.

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 3/7 9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

         Key API operations
         The API provides the following core endpoints for managing data agents and conversations:


                            HTTP
         Operation                      Endpoint                                                                                                 Descriptio
                            method

         Create an          POST        /v1beta/projects/*/locations/*/dataAgents                                                                Creates a
         agent

         Get an agent GET               /v1beta/projects/*/locations/*/dataAgents/*                                                              Retrieves t
                                                                                                                                                 specific da

         Get Identity       POST        /v1beta/projects/*/locations/*/dataAgents/*:getIamPolicyGets the Id
         and Access                                                                                                                              Manageme
         Management                                                                                                                              are assign
         policy                                                                                                                                  specific da
                                                                                                                                                 a Data Age
                                                                                                                                                     (/gemini/d
                                                                                                                                                 analytics-a
                                                                                                                                                 control#da
                                                                                                                                                 can call th
                                                                                                                                                 the data ag
                                                                                                                                                 Access Ma
                                                                                                                                                 before usin
                                                                                                                                                 setIAMpo
                                                                                                                                                 share a da
                                                                                                                                                 users.

         Set Identity       POST        /v1beta/projects/*/locations/*/dataAgents/*:setIamPolicySets the Id
         and Access                                                                                                                              Manageme
         Management                                                                                                                              specific da
         policy                                                                                                                                  a Data Age
                                                                                                                                                     (/gemini/d
                                                                                                                                                 analytics-a
                                                                                                                                                 control#da
                                                                                                                                                 should cal
                                                                                                                                                 share a da
                                                                                                                                                 users, whic
                                                                                                                                                 updates th
                                                                                                                                                 and Acces
                                                                                                                                                 permission

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 4/7 9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

                            HTTP
         Operation                      Endpoint                                                                                                 Descriptio
                            method

         Update an          PATCH /v1beta/projects/*/locations/*/dataAgents/*                                                                    Modifies a
         agent                                                                                                                                   agent.

         List agents        GET         /v1beta/projects/*/locations/*/dataAgents                                                                Lists availa
                                                                                                                                                 project.

         List               GET         /v1beta/projects/*/locations/*/dataAgents:listaccessibleLists acce
         accessible                                                                                                                              a project. A
         agents                                                                                                                                  considered
                                                                                                                                                 user that in
                                                                                                                                                 the get pe
                                                                                                                                                 agent. You
                                                                                                                                                 creator_
                                                                                                                                                 manage w
                                                                                                                                                 method re

                                                                                                                                                     NONE (d
                                                                                                                                                     data ag
                                                                                                                                                     access
                                                                                                                                                     regardl
                                                                                                                                                     the age

                                                                                                                                                     CREATO
                                                                                                                                                     only the
                                                                                                                                                     are acc
                                                                                                                                                     and tha
                                                                                                                                                     that us

                                                                                                                                                     NOT_CR
                                                                                                                                                     Returns
                                                                                                                                                     agents
                                                                                                                                                     to the u
                                                                                                                                                     created

         Delete an          DELETE/v1beta/projects/*/locations/*/dataAgents/*                                                                    Removes a
         agent

         Create a           POST        /v1beta/projects/*/locations/*/conversations                                                             Starts a ne
         conversation                                                                                                                            conversati

         Chat by using POST             /v1beta/projects/*/locations/*:chat                                                                      Continues
         a                                                                                                                                       conversati
         conversation                                                                                                                            message t
         reference                                                                                                                               existing co

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 5/7 9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

                            HTTP
         Operation                      Endpoint                                                                                                 Descriptio
                            method

                                                                                                                                                 associated
                                                                                                                                                 multi-turn
                                                                                                                                                 Google Clo
                                                                                                                                                 manages t
                                                                                                                                                 history.

         Chat by using POST             /v1beta/projects/*/locations/*:chat                                                                      Sends a st
         a data agent                                                                                                                            message t
         reference                                                                                                                               saved data
                                                                                                                                                 For multi-t
                                                                                                                                                 your applic
                                                                                                                                                 and provid
                                                                                                                                                 history wit

         Chat by using POST             /v1beta/projects/*/locations/*:chat                                                                      Sends a st
         inline context                                                                                                                          message b
                                                                                                                                                 context dir
                                                                                                                                                 without us
                                                                                                                                                 agent. For
                                                                                                                                                 conversati
                                                                                                                                                 must man
                                                                                                                                                 conversati
                                                                                                                                                 request.

         Get a              GET         /v1beta/projects/*/locations/*/conversations/*                                                           Retrieves t
         conversation                                                                                                                            specific co

         List               GET         /v1beta/projects/*/locations/*/conversations                                                             Lists the c
         conversations                                                                                                                           specific pr

         List               GET         /v1beta/projects/*/locations/*/conversations/*/messages Lists mess
         messages in                                                                                                                             specific co
         a
         conversation




         Send feedback
         Use the following links to file a bug or request a feature.

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 6/7 9/13/25, 12:06 PM Conversational Analytics API: Build data agents and chat with your data \| Gemini for Google Cloud

                  File a bug report
                    (https://issuetracker.google.com/issues/new?component=1747873&template=2128893)

                  File a feature request
                    (https://issuetracker.google.com/issues/new?component=1747873&template=2131795)




         Additional resources
                  Conversational Analytics API reference documentation
                    (/gemini/docs/conversational-analytics-api/reference/rest): Provides detailed descriptions of
                  methods, endpoints, and type definitions for request and response structures.

                  Troubleshoot Conversation Analytics API errors
                    (/gemini/docs/conversational-analytics-api/troubleshoot-ca-errors): Troubleshoot common
                  Conversation Analytics API errors.


         Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License
         (https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the Apache 2.0 License
         (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies
         (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

         Last updated 2025-09-12 UTC.

https://cloud.google.com/gemini/docs/conversational-analytics-api/overview 7/7 
