# segment_public_api.JourneysApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_journey**](JourneysApi.md#create_journey) | **POST** /spaces/{spaceId}/journeys | Create Journey
[**get_journey**](JourneysApi.md#get_journey) | **GET** /spaces/{spaceId}/journeys/{containerId} | Get Journey
[**get_journey_analytics**](JourneysApi.md#get_journey_analytics) | **GET** /spaces/{spaceId}/journeys/{containerId}/analytics | Get Journey Analytics
[**remove_journey_from_space**](JourneysApi.md#remove_journey_from_space) | **DELETE** /spaces/{spaceId}/journeys/{containerId} | Remove Journey from Space
[**replace_steps_for_journey**](JourneysApi.md#replace_steps_for_journey) | **PUT** /spaces/{spaceId}/journeys/{containerId}/steps | Replace Steps for Journey
[**update_destinations_for_journey**](JourneysApi.md#update_destinations_for_journey) | **PATCH** /spaces/{spaceId}/journeys/{containerId}/destinations | Update Destinations for Journey
[**update_status_for_journey**](JourneysApi.md#update_status_for_journey) | **PATCH** /spaces/{spaceId}/journeys/{containerId}/status | Update Status for Journey



## Operation: create_journey

> CreateJourney201Response create_journey(space_id, create_journey_alpha_input)

Create Journey

Creates Journey.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_journey201_response import CreateJourney201Response
from segment_public_api.models.create_journey_alpha_input import CreateJourneyAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'space_id' # str | 
    create_journey_alpha_input = {"name":"Journey from API","description":"This is a journey created from the API","definition":{"entryRules":{"type":"MULTIPLE","concurrency":{"enabled":true,"concurrencyKey":"applicationId"}},"exitRules":{"enabled":true,"rules":[{"key":{"id":"exitRuleExit_12345"},"type":"EXIT_RULE","exitType":"EVENT_PERFORMED","condition":"event('Credit Card Application Discarded').count() = 1","enabled":true,"concurrencyEnabled":true,"connectedDestinations":["destination_5678"]},{"key":{"id":"exitRuleExit_22345"},"type":"EXIT_RULE","exitType":"AUDIENCE_MEMBERSHIP_CHANGE","enabled":true,"concurrencyEnabled":false,"audienceId":"aud_12345"}],"relatedDestinations":[{"type":"DESTINATION","key":{"id":"destination_5678"},"destinations":[{"destinationId":"67644425c7c427181c2dcb6a","activations":[{"id":"4R7udgi1oiCH8AooG3mC5","eventName":"Credit Card Application Approved in journey","actionDefinition":{"id":"ddond619L9vRgb1eAMhuKm","name":"Send","enabled":true,"actionId":"ddond619L9vRgb1eAMhuKm","mappings":{"url":"https://webhook.site/1920a88d-fd67-429b-ba36-0f421581e67b","method":"POST","batch_size":0,"data":{"@path":"$."},"enable_batching":false}},"propertySelections":{"profile":["phone","name","whatsapp","email"]}}]}]}]},"initialState":"entry_12345","states":[{"key":{"id":"entry_12345"},"type":"EVENT_ENTRY","transitions":[{"next":"exit_12345"}],"condition":"event('Credit Card Application Discarded').count() = 1"},{"key":{"id":"exit_12345"},"type":"EXIT"}]}} # CreateJourneyAlphaInput | 

    try:
        # Create Journey
        api_response = api_instance.create_journey(space_id, create_journey_alpha_input)
        print("The response of JourneysApi->create_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->create_journey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_journey_alpha_input** | [**CreateJourneyAlphaInput**](CreateJourneyAlphaInput.md)|  | 

### Return type

[**CreateJourney201Response**](CreateJourney201Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_journey

> GetJourney200Response get_journey(space_id, container_id)

Get Journey

Returns the journey by containerId  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_journey200_response import GetJourney200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'space_id' # str | 
    container_id = 'jcon_2tG95HZh4oPsgHfcOlznyfcDDAg' # str | 

    try:
        # Get Journey
        api_response = api_instance.get_journey(space_id, container_id)
        print("The response of JourneysApi->get_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->get_journey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **container_id** | **str**|  | 

### Return type

[**GetJourney200Response**](GetJourney200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_journey_analytics

> GetJourneyAnalytics200Response get_journey_analytics(space_id, container_id, version, from_date, to_date=to_date)

Get Journey Analytics

Get Analytics for a journey  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_journey_analytics200_response import GetJourneyAnalytics200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'spaceId' # str | 
    container_id = 'jcon_2tG95HZh4oPsgHfcOlznyfcDDAg' # str | 
    version = 1 # float | The journey version.  This parameter exists in alpha.
    from_date = '2006-01-02T15:04:05.000Z' # str | This parameter exists in alpha.
    to_date = '2006-01-02T15:04:05.000Z' # str | This parameter exists in alpha. (optional)

    try:
        # Get Journey Analytics
        api_response = api_instance.get_journey_analytics(space_id, container_id, version, from_date, to_date=to_date)
        print("The response of JourneysApi->get_journey_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->get_journey_analytics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **container_id** | **str**|  | 
 **version** | **float**| The journey version.  This parameter exists in alpha. | 
 **from_date** | **str**| This parameter exists in alpha. | 
 **to_date** | **str**| This parameter exists in alpha. | [optional] 

### Return type

[**GetJourneyAnalytics200Response**](GetJourneyAnalytics200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: remove_journey_from_space

> RemoveJourneyFromSpace200Response remove_journey_from_space(space_id, container_id, version)

Remove Journey from Space

Delete a journey  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_journey_from_space200_response import RemoveJourneyFromSpace200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'spaceId' # str | 
    container_id = 'jcon_2tG95HZh4oPsgHfcOlznyfcDDAg' # str | 
    version = 1 # float | The journey version.  This parameter exists in alpha.

    try:
        # Remove Journey from Space
        api_response = api_instance.remove_journey_from_space(space_id, container_id, version)
        print("The response of JourneysApi->remove_journey_from_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->remove_journey_from_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **container_id** | **str**|  | 
 **version** | **float**| The journey version.  This parameter exists in alpha. | 

### Return type

[**RemoveJourneyFromSpace200Response**](RemoveJourneyFromSpace200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: replace_steps_for_journey

> ReplaceStepsForJourney200Response replace_steps_for_journey(space_id, container_id, replace_steps_for_journey_alpha_input)

Replace Steps for Journey

Replace steps for a journey  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_steps_for_journey200_response import ReplaceStepsForJourney200Response
from segment_public_api.models.replace_steps_for_journey_alpha_input import ReplaceStepsForJourneyAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'spaceId' # str | 
    container_id = 'jcon_2tG95HZh4oPsgHfcOlznyfcDDAg' # str | 
    replace_steps_for_journey_alpha_input = {"initialState":"entry_12345","states":[{"key":{"id":"exit_12345"},"type":"EXIT"},{"key":{"id":"exit_22345"},"type":"EXIT"},{"key":{"id":"entry_12345"},"type":"EVENT_ENTRY","transitions":[{"next":"split_12345"}],"condition":"event('Credit Card Application Discarded').count() = 1"},{"key":{"id":"split_12345","name":"wait for event modified"},"type":"EVENT_SPLIT","transitions":[{"type":"CONDITION","next":"destination_12345","condition":"event('Credit Card Application Approved').count() = 1"},{"type":"TIMEOUT","next":"exit_12345","duration":"2h"}]},{"key":{"id":"destination_12345","name":"Send to Twilio Omni channel"},"type":"DESTINATION","transitions":[{"next":"exit_22345"}],"destinations":[]}]} # ReplaceStepsForJourneyAlphaInput | 

    try:
        # Replace Steps for Journey
        api_response = api_instance.replace_steps_for_journey(space_id, container_id, replace_steps_for_journey_alpha_input)
        print("The response of JourneysApi->replace_steps_for_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->replace_steps_for_journey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **container_id** | **str**|  | 
 **replace_steps_for_journey_alpha_input** | [**ReplaceStepsForJourneyAlphaInput**](ReplaceStepsForJourneyAlphaInput.md)|  | 

### Return type

[**ReplaceStepsForJourney200Response**](ReplaceStepsForJourney200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_destinations_for_journey

> UpdateDestinationsForJourney200Response update_destinations_for_journey(space_id, container_id, update_destinations_for_journey_alpha_input)

Update Destinations for Journey

Update DESTINATIONS for a journey  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_destinations_for_journey200_response import UpdateDestinationsForJourney200Response
from segment_public_api.models.update_destinations_for_journey_alpha_input import UpdateDestinationsForJourneyAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'spaceId' # str | 
    container_id = 'jcon_2tG95HZh4oPsgHfcOlznyfcDDAg' # str | 
    update_destinations_for_journey_alpha_input = {"stateDestinations":[{"stateId":"destination_12345","destinations":[{"destinationId":"67644425c7c427181c2dcb6a","activations":[{"eventName":"Credit Card Application Approved in journey","actionDefinition":{"actionId":"ddond619L9vRgb1eAMhuKm","useDefaultMappings":true,"mappings":{"url":"https://webhook.site/1920a88d-fd67-429b-ba36-0f421581e67b"}},"propertySelections":{"profile":["email","name","phone","whatsapp"]}}]}]}]} # UpdateDestinationsForJourneyAlphaInput | 

    try:
        # Update Destinations for Journey
        api_response = api_instance.update_destinations_for_journey(space_id, container_id, update_destinations_for_journey_alpha_input)
        print("The response of JourneysApi->update_destinations_for_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->update_destinations_for_journey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **container_id** | **str**|  | 
 **update_destinations_for_journey_alpha_input** | [**UpdateDestinationsForJourneyAlphaInput**](UpdateDestinationsForJourneyAlphaInput.md)|  | 

### Return type

[**UpdateDestinationsForJourney200Response**](UpdateDestinationsForJourney200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_status_for_journey

> UpdateStatusForJourney200Response update_status_for_journey(space_id, container_id, update_status_for_journey_alpha_input)

Update Status for Journey

Update status of the journey   • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Journeys feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_status_for_journey200_response import UpdateStatusForJourney200Response
from segment_public_api.models.update_status_for_journey_alpha_input import UpdateStatusForJourneyAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = 'spaceId' # str | 
    container_id = 'jcon_2tG95HZh4oPsgHfcOlznyfcDDAg' # str | 
    update_status_for_journey_alpha_input = {"action":"PUBLISH","version":1} # UpdateStatusForJourneyAlphaInput | 

    try:
        # Update Status for Journey
        api_response = api_instance.update_status_for_journey(space_id, container_id, update_status_for_journey_alpha_input)
        print("The response of JourneysApi->update_status_for_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->update_status_for_journey: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **container_id** | **str**|  | 
 **update_status_for_journey_alpha_input** | [**UpdateStatusForJourneyAlphaInput**](UpdateStatusForJourneyAlphaInput.md)|  | 

### Return type

[**UpdateStatusForJourney200Response**](UpdateStatusForJourney200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

