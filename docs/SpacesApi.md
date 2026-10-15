# segment_public_api.SpacesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_space**](SpacesApi.md#get_space) | **GET** /spaces/{spaceId} | Get Space
[**list_spaces**](SpacesApi.md#list_spaces) | **GET** /spaces | List Spaces



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
**429** | Too many requests |  * Retry-After - Number of whole seconds to wait before retrying. Sent when the request was rejected because the authentication token is rate limited. Prefer this over your own backoff schedule when present. <br>  |

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
**429** | Too many requests |  * Retry-After - Number of whole seconds to wait before retrying. Sent when the request was rejected because the authentication token is rate limited. Prefer this over your own backoff schedule when present. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

