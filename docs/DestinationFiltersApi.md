# segment_public_api.DestinationFiltersApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter_for_destination**](DestinationFiltersApi.md#create_filter_for_destination) | **POST** /destination/{destinationId}/filters | Create Filter for Destination
[**get_filter_in_destination**](DestinationFiltersApi.md#get_filter_in_destination) | **GET** /destination/{destinationId}/filters/{filterId} | Get Filter in Destination
[**list_filters_from_destination**](DestinationFiltersApi.md#list_filters_from_destination) | **GET** /destination/{destinationId}/filters | List Filters from Destination
[**preview_destination_filter**](DestinationFiltersApi.md#preview_destination_filter) | **POST** /destination/filters/preview | Preview Destination Filter
[**remove_filter_from_destination**](DestinationFiltersApi.md#remove_filter_from_destination) | **DELETE** /destination/{destinationId}/filters/{filterId} | Remove Filter from Destination
[**update_filter_for_destination**](DestinationFiltersApi.md#update_filter_for_destination) | **PATCH** /destination/{destinationId}/filters/{filterId} | Update Filter for Destination



## Operation: create_filter_for_destination

> CreateFilterForDestination200Response create_filter_for_destination(destination_id, create_filter_for_destination_v1_input)

Create Filter for Destination

Creates a filter in a Destination.    • When called, this endpoint may generate the `Destination Filter Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_filter_for_destination200_response import CreateFilterForDestination200Response
from segment_public_api.models.create_filter_for_destination_v1_input import CreateFilterForDestinationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationFiltersApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    create_filter_for_destination_v1_input = {"sourceId":"rh5BDZp6QDHvXFCkibm1pR","title":"Filter \"Identify\" events","description":"Drop Identify tracking from this destination","if":"type = \"identify\"","actions":[{"type":"DROP"}],"enabled":true} # CreateFilterForDestinationV1Input | 

    try:
        # Create Filter for Destination
        api_response = api_instance.create_filter_for_destination(destination_id, create_filter_for_destination_v1_input)
        print("The response of DestinationFiltersApi->create_filter_for_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationFiltersApi->create_filter_for_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **create_filter_for_destination_v1_input** | [**CreateFilterForDestinationV1Input**](CreateFilterForDestinationV1Input.md)|  | 

### Return type

[**CreateFilterForDestination200Response**](CreateFilterForDestination200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_filter_in_destination

> GetFilterInDestination200Response get_filter_in_destination(destination_id, filter_id)

Get Filter in Destination

Gets a Destination filter by id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_filter_in_destination200_response import GetFilterInDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationFiltersApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    filter_id = 'xx6AySGeFExzdv2Gw2EuhV' # str | 

    try:
        # Get Filter in Destination
        api_response = api_instance.get_filter_in_destination(destination_id, filter_id)
        print("The response of DestinationFiltersApi->get_filter_in_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationFiltersApi->get_filter_in_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **filter_id** | **str**|  | 

### Return type

[**GetFilterInDestination200Response**](GetFilterInDestination200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: list_filters_from_destination

> ListFiltersFromDestination200Response list_filters_from_destination(destination_id, pagination)

List Filters from Destination

Lists filters for a Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_filters_from_destination200_response import ListFiltersFromDestination200Response
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
    api_instance = segment_public_api.DestinationFiltersApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination options.  This parameter exists in v1.

    try:
        # List Filters from Destination
        api_response = api_instance.list_filters_from_destination(destination_id, pagination)
        print("The response of DestinationFiltersApi->list_filters_from_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationFiltersApi->list_filters_from_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination options.  This parameter exists in v1. | 

### Return type

[**ListFiltersFromDestination200Response**](ListFiltersFromDestination200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: preview_destination_filter

> PreviewDestinationFilter200Response preview_destination_filter(preview_destination_filter_v1_input)

Preview Destination Filter

Simulates the application of a Destination filter to a provided JSON payload.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.preview_destination_filter200_response import PreviewDestinationFilter200Response
from segment_public_api.models.preview_destination_filter_v1_input import PreviewDestinationFilterV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationFiltersApi(api_client)
    preview_destination_filter_v1_input = {"filter":{"if":"type = \"track\" AND event = \"Order Completed\"","actions":[{"type":"ALLOW_PROPERTIES","fields":{"product":["event","requestedFrom"]}}]},"payload":{"type":"track","event":"Order Completed","product":{"name":"Fake mustache","requestedFrom":"/products/123/checkout","referrer":"www.example.com"}}} # PreviewDestinationFilterV1Input | 

    try:
        # Preview Destination Filter
        api_response = api_instance.preview_destination_filter(preview_destination_filter_v1_input)
        print("The response of DestinationFiltersApi->preview_destination_filter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationFiltersApi->preview_destination_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preview_destination_filter_v1_input** | [**PreviewDestinationFilterV1Input**](PreviewDestinationFilterV1Input.md)|  | 

### Return type

[**PreviewDestinationFilter200Response**](PreviewDestinationFilter200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: remove_filter_from_destination

> RemoveFilterFromDestination200Response remove_filter_from_destination(destination_id, filter_id)

Remove Filter from Destination

Deletes a Destination filter.    • When called, this endpoint may generate the `Destination Filter Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_filter_from_destination200_response import RemoveFilterFromDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationFiltersApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    filter_id = '2DrXi3N7S85LobhzPphZz0uFzJ4' # str | 

    try:
        # Remove Filter from Destination
        api_response = api_instance.remove_filter_from_destination(destination_id, filter_id)
        print("The response of DestinationFiltersApi->remove_filter_from_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationFiltersApi->remove_filter_from_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **filter_id** | **str**|  | 

### Return type

[**RemoveFilterFromDestination200Response**](RemoveFilterFromDestination200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_filter_for_destination

> UpdateFilterForDestination200Response update_filter_for_destination(destination_id, filter_id, update_filter_for_destination_v1_input)

Update Filter for Destination

Updates a filter in a Destination.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Destination Filter Enabled * Destination Filter Disabled       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_filter_for_destination200_response import UpdateFilterForDestination200Response
from segment_public_api.models.update_filter_for_destination_v1_input import UpdateFilterForDestinationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationFiltersApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    filter_id = 'xx6AySGeFExzdv2Gw2EuhV' # str | 
    update_filter_for_destination_v1_input = {"if":"!(type = \"track\")","actions":[{"type":"DROP"}],"title":"Allow Track","description":"Allows track calls through to the destination.","enabled":true} # UpdateFilterForDestinationV1Input | 

    try:
        # Update Filter for Destination
        api_response = api_instance.update_filter_for_destination(destination_id, filter_id, update_filter_for_destination_v1_input)
        print("The response of DestinationFiltersApi->update_filter_for_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationFiltersApi->update_filter_for_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **filter_id** | **str**|  | 
 **update_filter_for_destination_v1_input** | [**UpdateFilterForDestinationV1Input**](UpdateFilterForDestinationV1Input.md)|  | 

### Return type

[**UpdateFilterForDestination200Response**](UpdateFilterForDestination200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

