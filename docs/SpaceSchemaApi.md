# segment_public_api.SpaceSchemaApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_events**](SpaceSchemaApi.md#list_events) | **GET** /spaces/{spaceId}/events | List Events
[**list_properties_from_event**](SpaceSchemaApi.md#list_properties_from_event) | **GET** /spaces/{spaceId}/events/{eventName}/properties | List Properties from Event
[**list_sample_values_from_event_property**](SpaceSchemaApi.md#list_sample_values_from_event_property) | **GET** /spaces/{spaceId}/events/{eventName}/properties/{propertyName}/sample-values | List Sample Values from Event Property



## Operation: list_events

> ListEvents200Response list_events(space_id, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search)

List Events

Returns a list of Events for a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_events200_response import ListEvents200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    sort_by = 'lastSeenAt' # str | Field to sort by. Defaults to 'lastSeenAt'.  This parameter exists in alpha. (optional)
    sort_dir = 'desc' # str | Sort direction. Defaults to 'desc'.  This parameter exists in alpha. (optional)
    search = 'search_example' # str | Filter events by name substring.  This parameter exists in alpha. (optional)

    try:
        # List Events
        api_response = api_instance.list_events(space_id, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search)
        print("The response of SpaceSchemaApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **sort_by** | **str**| Field to sort by. Defaults to &#39;lastSeenAt&#39;.  This parameter exists in alpha. | [optional] 
 **sort_dir** | **str**| Sort direction. Defaults to &#39;desc&#39;.  This parameter exists in alpha. | [optional] 
 **search** | **str**| Filter events by name substring.  This parameter exists in alpha. | [optional] 

### Return type

[**ListEvents200Response**](ListEvents200Response.md)

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


## Operation: list_properties_from_event

> ListPropertiesFromEvent200Response list_properties_from_event(space_id, event_name, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search, include_sample_values=include_sample_values, samples_count=samples_count)

List Properties from Event

Returns a list of Properties for an Event in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_properties_from_event200_response import ListPropertiesFromEvent200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    event_name = 'Order Completed' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    sort_by = 'name' # str | Field to sort by. Defaults to 'lastSeenAt'.  This parameter exists in alpha. (optional)
    sort_dir = 'asc' # str | Sort direction. Defaults to 'desc'.  This parameter exists in alpha. (optional)
    search = 'search_example' # str | Filter properties by name substring.  This parameter exists in alpha. (optional)
    include_sample_values = True # bool | When true, include sample values for each property. Defaults to false.  This parameter exists in alpha. (optional)
    samples_count = 3.4 # float | Max number of sample values to return per property. Defaults to 20, min 1, max 100.  This parameter exists in alpha. (optional)

    try:
        # List Properties from Event
        api_response = api_instance.list_properties_from_event(space_id, event_name, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search, include_sample_values=include_sample_values, samples_count=samples_count)
        print("The response of SpaceSchemaApi->list_properties_from_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_properties_from_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **event_name** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **sort_by** | **str**| Field to sort by. Defaults to &#39;lastSeenAt&#39;.  This parameter exists in alpha. | [optional] 
 **sort_dir** | **str**| Sort direction. Defaults to &#39;desc&#39;.  This parameter exists in alpha. | [optional] 
 **search** | **str**| Filter properties by name substring.  This parameter exists in alpha. | [optional] 
 **include_sample_values** | **bool**| When true, include sample values for each property. Defaults to false.  This parameter exists in alpha. | [optional] 
 **samples_count** | **float**| Max number of sample values to return per property. Defaults to 20, min 1, max 100.  This parameter exists in alpha. | [optional] 

### Return type

[**ListPropertiesFromEvent200Response**](ListPropertiesFromEvent200Response.md)

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


## Operation: list_sample_values_from_event_property

> ListSampleValuesFromEventProperty200Response list_sample_values_from_event_property(space_id, event_name, property_name, property_type)

List Sample Values from Event Property

Returns sample values for an Event Property in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.event_property_type import EventPropertyType
from segment_public_api.models.list_sample_values_from_event_property200_response import ListSampleValuesFromEventProperty200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    event_name = 'Order Completed' # str | 
    property_name = 'revenue' # str | 
    property_type = segment_public_api.EventPropertyType() # EventPropertyType | The property type.  This parameter exists in alpha.

    try:
        # List Sample Values from Event Property
        api_response = api_instance.list_sample_values_from_event_property(space_id, event_name, property_name, property_type)
        print("The response of SpaceSchemaApi->list_sample_values_from_event_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_sample_values_from_event_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **event_name** | **str**|  | 
 **property_name** | **str**|  | 
 **property_type** | [**EventPropertyType**](.md)| The property type.  This parameter exists in alpha. | 

### Return type

[**ListSampleValuesFromEventProperty200Response**](ListSampleValuesFromEventProperty200Response.md)

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

