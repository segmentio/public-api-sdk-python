# segment_public_api.SpacesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_query_messaging_subscriptions_for_space**](SpacesApi.md#batch_query_messaging_subscriptions_for_space) | **POST** /spaces/{spaceId}/messaging-subscriptions/batch | Batch Query Messaging Subscriptions for Space
[**get_space**](SpacesApi.md#get_space) | **GET** /spaces/{spaceId} | Get Space
[**list_spaces**](SpacesApi.md#list_spaces) | **GET** /spaces | List Spaces
[**replace_messaging_subscriptions_in_spaces**](SpacesApi.md#replace_messaging_subscriptions_in_spaces) | **PUT** /spaces/{spaceId}/messaging-subscriptions | Replace Messaging Subscriptions in Spaces



## Operation: batch_query_messaging_subscriptions_for_space

> BatchQueryMessagingSubscriptionsForSpace200Response batch_query_messaging_subscriptions_for_space(space_id, batch_query_messaging_subscriptions_for_space_alpha_input)

Batch Query Messaging Subscriptions for Space

 <div style=\"background-color: #fff3cd; border: 1px solid #ffc107; border-radius: 6px; padding: 16px; margin: 16px 0; color: #856404; display: flex; align-items: center; gap: 12px; line-height: 1.5;\">   <span style=\"color: #ff9800; font-size: 16px; flex-shrink: 0;\">⚠️</span>   <div style=\"line-height: 1.5;\">     <div style=\"font-weight: 600; font-size: 14px; margin-bottom: 6px;\">       Engage Premier features will no longer be available after December 15, 2025.     </div>     <div style=\"font-size: 13px;\">       This API will be deactivated after this date.     </div>   </div> </div> Get Messaging Subscriptions for space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.batch_query_messaging_subscriptions_for_space200_response import BatchQueryMessagingSubscriptionsForSpace200Response
from segment_public_api.models.batch_query_messaging_subscriptions_for_space_alpha_input import BatchQueryMessagingSubscriptionsForSpaceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpacesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    batch_query_messaging_subscriptions_for_space_alpha_input = {"subscriptions":[{"key":"jacob@exmple.com","type":"EMAIL"},{"key":"jane@exmple.com","type":"EMAIL"},{"key":"pgibbonsexample.com","type":"EMAIL"},{"key":"+12162226233","type":"SMS"}]} # BatchQueryMessagingSubscriptionsForSpaceAlphaInput | 

    try:
        # Batch Query Messaging Subscriptions for Space
        api_response = api_instance.batch_query_messaging_subscriptions_for_space(space_id, batch_query_messaging_subscriptions_for_space_alpha_input)
        print("The response of SpacesApi->batch_query_messaging_subscriptions_for_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->batch_query_messaging_subscriptions_for_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **batch_query_messaging_subscriptions_for_space_alpha_input** | [**BatchQueryMessagingSubscriptionsForSpaceAlphaInput**](BatchQueryMessagingSubscriptionsForSpaceAlphaInput.md)|  | 

### Return type

[**BatchQueryMessagingSubscriptionsForSpace200Response**](BatchQueryMessagingSubscriptionsForSpace200Response.md)

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


## Operation: get_space

> GetSpace200Response get_space(space_id)

Get Space

Returns the Space by id.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_space200_response import GetSpace200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpacesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 

    try:
        # Get Space
        api_response = api_instance.get_space(space_id)
        print("The response of SpacesApi->get_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->get_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 

### Return type

[**GetSpace200Response**](GetSpace200Response.md)

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


## Operation: list_spaces

> ListSpaces200Response list_spaces(pagination=pagination)

List Spaces

List Spaces.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_spaces200_response import ListSpaces200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpacesApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params  This parameter exists in alpha. (optional)

    try:
        # List Spaces
        api_response = api_instance.list_spaces(pagination=pagination)
        print("The response of SpacesApi->list_spaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->list_spaces: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination params  This parameter exists in alpha. | [optional] 

### Return type

[**ListSpaces200Response**](ListSpaces200Response.md)

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


## Operation: replace_messaging_subscriptions_in_spaces

> ReplaceMessagingSubscriptionsInSpaces200Response replace_messaging_subscriptions_in_spaces(space_id, replace_messaging_subscriptions_in_spaces_alpha_input)

Replace Messaging Subscriptions in Spaces

 <div style=\"background-color: #fff3cd; border: 1px solid #ffc107; border-radius: 6px; padding: 16px; margin: 16px 0; color: #856404; display: flex; align-items: center; gap: 12px; line-height: 1.5;\">   <span style=\"color: #ff9800; font-size: 16px; flex-shrink: 0;\">⚠️</span>   <div style=\"line-height: 1.5;\">     <div style=\"font-weight: 600; font-size: 14px; margin-bottom: 6px;\">       Engage Premier features will no longer be available after December 15, 2025.     </div>     <div style=\"font-size: 13px;\">       This API will be deactivated after this date.     </div>   </div> </div> Replace Messaging Subscriptions in Spaces.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_messaging_subscriptions_in_spaces200_response import ReplaceMessagingSubscriptionsInSpaces200Response
from segment_public_api.models.replace_messaging_subscriptions_in_spaces_alpha_input import ReplaceMessagingSubscriptionsInSpacesAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpacesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    replace_messaging_subscriptions_in_spaces_alpha_input = {"subscriptions":[{"key":"jacob@exmple.com","type":"EMAIL","status":"SUBSCRIBED"},{"key":"jane@exmple.com","type":"EMAIL","status":"SUBSCRIBED","groups":[{"name":"promotions","status":"SUBSCRIBED"}]},{"key":"pgibbonsexample.com","type":"EMAIL","status":"UNSUBSCRIBED"},{"key":"+12162226233","type":"SMS","status":"DID_NOT_SUBSCRIBE"}]} # ReplaceMessagingSubscriptionsInSpacesAlphaInput | 

    try:
        # Replace Messaging Subscriptions in Spaces
        api_response = api_instance.replace_messaging_subscriptions_in_spaces(space_id, replace_messaging_subscriptions_in_spaces_alpha_input)
        print("The response of SpacesApi->replace_messaging_subscriptions_in_spaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacesApi->replace_messaging_subscriptions_in_spaces: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **replace_messaging_subscriptions_in_spaces_alpha_input** | [**ReplaceMessagingSubscriptionsInSpacesAlphaInput**](ReplaceMessagingSubscriptionsInSpacesAlphaInput.md)|  | 

### Return type

[**ReplaceMessagingSubscriptionsInSpaces200Response**](ReplaceMessagingSubscriptionsInSpaces200Response.md)

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

