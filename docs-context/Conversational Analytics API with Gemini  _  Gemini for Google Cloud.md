9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Conversational Analytics API with
         Gemini

         Service: geminidataanalytics.googleapis.com
         To call this service, we recommend that you use the Google-provided client libraries
          (https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your
         own libraries to call this service, use the following information when you make the API
         requests.



         Discovery document
         A Discovery Document (https://developers.google.com/discovery/v1/reference/apis) is a machine-
         readable specification for describing and consuming REST APIs. It is used to build client
         libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide
         multiple discovery documents. This service provides the following discovery documents:

                  https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1beta
                    (https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1beta)

                  https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1alpha
                    (https://geminidataanalytics.googleapis.com/$discovery/rest?version=v1alpha)



         Service endpoint
         A service endpoint (https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base
         URL that specifies the network address of an API service. One service might have multiple
         service endpoints. This service has the following service endpoint and all URIs below are
         relative to this service endpoint:

                  https://geminidataanalytics.googleapis.com



         REST Resource: v1beta.projects.locations
          (/gemini/docs/conversational-analytics-api/reference/rest/v1beta/projects.locations)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 1/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         chat                      POST /v1beta/{parent=projects/*/locations/*}:chat
          (/gemini/docs/conversati Answers a data question by generating a stream of Message
         onal-analytics-                         (/gemini/docs/conversational-analytics-api/reference/rest/v1alpha/Message)
         api/reference/rest/v1beta/ objects.
         projects.locations/chat)

         get                                    GET /v1beta/{name=projects/*/locations/*}
          (/gemini/docs/conversati Gets information about a location.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations/get)

         list                                   GET /v1beta/{name=projects/*}/locations
          (/gemini/docs/conversati Lists information about the supported locations for this service.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations/list)




         REST Resource: v1beta.projects.locations.conversations
          (/gemini/docs/conversational-analytics-api/reference/rest/v1beta/projects.locations.conversations)



         Methods


         create                                 POST /v1beta/{parent=projects/*/locations/*}/conversations
          (/gemini/docs/conversati Creates a new conversation to persist the conversation history.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.convers
         ations/create)

         get                                    GET /v1beta/{name=projects/*/locations/*/conversations/*}
          (/gemini/docs/conversati Gets details of a single conversation by using conversation id and parent.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.convers
         ations/get)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 2/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         list                                   GET /v1beta/{parent=projects/*/locations/*}/conversations
          (/gemini/docs/conversati Lists all conversations for a given parent.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.convers
         ations/list)




         REST Resource: v1beta.projects.locations.conversations.
         messages
          (/gemini/docs/conversational-analytics-
         api/reference/rest/v1beta/projects.locations.conversations.messages)




         Methods


         list                                   GET /v1beta/{parent=projects/*/locations/*/conversations/
          (/gemini/docs/conversati *}/messages
         onal-analytics-                        Lists all messages for a given conversation.
         api/reference/rest/v1beta/
         projects.locations.convers
         ations.messages/list)




         REST Resource: v1beta.projects.locations.dataAgents
          (/gemini/docs/conversational-analytics-api/reference/rest/v1beta/projects.locations.dataAgents)



         Methods


         create                                 POST /v1beta/{parent=projects/*/locations/*}/dataAgents
          (/gemini/docs/conversati Creates a new DataAgent in a given project and location.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/create)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 3/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         delete                                 DELETE /v1beta/{name=projects/*/locations/*/dataAgents/*}
          (/gemini/docs/conversati Deletes a single DataAgent.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/delete)

         get                                    GET /v1beta/{name=projects/*/locations/*/dataAgents/*}
          (/gemini/docs/conversati Gets details of a single DataAgent.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/get)

         getIamPolicy              POST /v1beta/{resource=projects/*/locations/*/dataAgents/
          (/gemini/docs/conversati *}:getIamPolicy
         onal-analytics-                        Gets the IAM policy for DataAgent
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/getIamPolicy)

         list                                   GET /v1beta/{parent=projects/*/locations/*}/dataAgents
          (/gemini/docs/conversati Lists DataAgents in a given project and location.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/list)

         listAccessible            GET /v1beta/{parent=projects/*/locations/*}/dataAgents:list
          (/gemini/docs/conversati Accessible
         onal-analytics-                        Lists DataAgents that are accessible to the caller in a given project and location.
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/listAccessible)

         patch                     PATCH /v1beta/{dataAgent.name=projects/*/locations/*/data
          (/gemini/docs/conversati Agents/*}
         onal-analytics-                        Updates the parameters of a single DataAgent.
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/patch)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 4/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         setIamPolicy              POST /v1beta/{resource=projects/*/locations/*/dataAgents/
          (/gemini/docs/conversati *}:setIamPolicy
         onal-analytics-                        Sets the IAM policy for a DataAgent.
         api/reference/rest/v1beta/
         projects.locations.dataAge
         nts/setIamPolicy)




         REST Resource: v1beta.projects.locations.operations
          (/gemini/docs/conversational-analytics-api/reference/rest/v1beta/projects.locations.operations)



         Methods


         cancel                    POST /v1beta/{name=projects/*/locations/*/operations/
          (/gemini/docs/conversati *}:cancel
         onal-analytics-                        Starts asynchronous cancellation on a long-running operation.
         api/reference/rest/v1beta/
         projects.locations.operatio
         ns/cancel)

         delete                                 DELETE /v1beta/{name=projects/*/locations/*/operations/*}
          (/gemini/docs/conversati Deletes a long-running operation.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.operatio
         ns/delete)

         get                                    GET /v1beta/{name=projects/*/locations/*/operations/*}
          (/gemini/docs/conversati Gets the latest state of a long-running operation.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.operatio
         ns/get)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 5/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         list                                   GET /v1beta/{name=projects/*/locations/*}/operations
          (/gemini/docs/conversati Lists operations that match the specified filter in the request.
         onal-analytics-
         api/reference/rest/v1beta/
         projects.locations.operatio
         ns/list)




         REST Resource: v1alpha.projects.locations
          (/gemini/docs/conversational-analytics-api/reference/rest/v1alpha/projects.locations)



         Methods


         chat                      POST /v1alpha/{parent=projects/*/locations/*}:chat
          (/gemini/docs/conversati Answers a data question by generating a stream of Message
         onal-analytics-                         (/gemini/docs/conversational-analytics-api/reference/rest/v1alpha/Message)
         api/reference/rest/v1alpha objects.
         /projects.locations/chat)

         get                                    GET /v1alpha/{name=projects/*/locations/*}
          (/gemini/docs/conversati Gets information about a location.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations/get)

         list                                   GET /v1alpha/{name=projects/*}/locations
          (/gemini/docs/conversati Lists information about the supported locations for this service.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations/list)




         REST Resource: v1alpha.projects.locations.conversations
          (/gemini/docs/conversational-analytics-api/reference/rest/v1alpha/projects.locations.conversations)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 6/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         create                                 POST /v1alpha/{parent=projects/*/locations/*}/conversations
          (/gemini/docs/conversati Creates a new conversation to persist the conversation history.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.conver
         sations/create)

         get                                    GET /v1alpha/{name=projects/*/locations/*/conversations/*}
          (/gemini/docs/conversati Gets details of a single conversation by using conversation id and parent.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.conver
         sations/get)

         list                                   GET /v1alpha/{parent=projects/*/locations/*}/conversations
          (/gemini/docs/conversati Lists all conversations for a given parent.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.conver
         sations/list)




         REST Resource: v1alpha.projects.locations.conversations.
         messages
          (/gemini/docs/conversational-analytics-
         api/reference/rest/v1alpha/projects.locations.conversations.messages)




         Methods


         list                                   GET /v1alpha/{parent=projects/*/locations/*/conversations/
          (/gemini/docs/conversati *}/messages
         onal-analytics-                        Lists all messages for a given conversation.
         api/reference/rest/v1alpha
         /projects.locations.conver
         sations.messages/list)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 7/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         REST Resource: v1alpha.projects.locations.dataAgents
          (/gemini/docs/conversational-analytics-api/reference/rest/v1alpha/projects.locations.dataAgents)



         Methods


         create                                 POST /v1alpha/{parent=projects/*/locations/*}/dataAgents
          (/gemini/docs/conversati Creates a new DataAgent in a given project and location.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/create)

         delete                                 DELETE /v1alpha/{name=projects/*/locations/*/dataAgents/*}
          (/gemini/docs/conversati Deletes a single DataAgent.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/delete)

         get                                    GET /v1alpha/{name=projects/*/locations/*/dataAgents/*}
          (/gemini/docs/conversati Gets details of a single DataAgent.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/get)

         getIamPolicy              POST /v1alpha/{resource=projects/*/locations/*/dataAgents/
          (/gemini/docs/conversati *}:getIamPolicy
         onal-analytics-                        Gets the IAM policy for DataAgent
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/getIamPolicy)

         list                                   GET /v1alpha/{parent=projects/*/locations/*}/dataAgents
          (/gemini/docs/conversati Lists DataAgents in a given project and location.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/list)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 8/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         listAccessible            GET /v1alpha/{parent=projects/*/locations/*}/data
          (/gemini/docs/conversati Agents:listAccessible
         onal-analytics-                        Lists DataAgents that are accessible to the caller in a given project and location.
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/listAccessible)

         patch                     PATCH /v1alpha/{dataAgent.name=projects/*/locations/*/data
          (/gemini/docs/conversati Agents/*}
         onal-analytics-                        Updates the parameters of a single DataAgent.
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/patch)

         setIamPolicy              POST /v1alpha/{resource=projects/*/locations/*/dataAgents/
          (/gemini/docs/conversati *}:setIamPolicy
         onal-analytics-                        Sets the IAM policy for a DataAgent.
         api/reference/rest/v1alpha
         /projects.locations.dataAg
         ents/setIamPolicy)




         REST Resource: v1alpha.projects.locations.operations
          (/gemini/docs/conversational-analytics-api/reference/rest/v1alpha/projects.locations.operations)



         Methods


         cancel                    POST /v1alpha/{name=projects/*/locations/*/operations/
          (/gemini/docs/conversati *}:cancel
         onal-analytics-                        Starts asynchronous cancellation on a long-running operation.
         api/reference/rest/v1alpha
         /projects.locations.operati
         ons/cancel)

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 9/10 9/13/25, 12:09 PM Conversational Analytics API with Gemini \| Gemini for Google Cloud

         Methods


         delete                                 DELETE /v1alpha/{name=projects/*/locations/*/operations/*}
          (/gemini/docs/conversati Deletes a long-running operation.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.operati
         ons/delete)

         get                                    GET /v1alpha/{name=projects/*/locations/*/operations/*}
          (/gemini/docs/conversati Gets the latest state of a long-running operation.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.operati
         ons/get)

         list                                   GET /v1alpha/{name=projects/*/locations/*}/operations
          (/gemini/docs/conversati Lists operations that match the specified filter in the request.
         onal-analytics-
         api/reference/rest/v1alpha
         /projects.locations.operati
         ons/list)


         Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License
          (https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the Apache 2.0 License
          (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies
          (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

         Last updated 2025-09-12 UTC.

https://cloud.google.com/gemini/docs/conversational-analytics-api/reference/rest 10/10 
