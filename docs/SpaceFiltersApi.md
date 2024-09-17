# segment_public_api.SpaceFiltersApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter_for_space**](SpaceFiltersApi.md#create_filter_for_space) | **POST** /filters | Create Filter for Space
[**delete_filter_by_id**](SpaceFiltersApi.md#delete_filter_by_id) | **DELETE** /filters/{id} | Delete Filter By Id
[**get_filter_by_id**](SpaceFiltersApi.md#get_filter_by_id) | **GET** /filters/{id} | Get Filter By Id
[**list_filters_for_space**](SpaceFiltersApi.md#list_filters_for_space) | **GET** /filters | List Filters for Space
[**update_filter_by_id**](SpaceFiltersApi.md#update_filter_by_id) | **PATCH** /filters/{id} | Update Filter By Id



## Operation: create_filter_for_space

> CreateFilterForSpace200Response create_filter_for_space(create_filter_for_space_input)

Create Filter for Space

Creates a filter for a space. A space filter applies to events coming from all Sources connected to a space.    • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.    • In order to successfully call this endpoint, the specified Workspace needs to have the Space Filters feature enabled. Please reach out to your customer success manager for more information.   • When called, this endpoint may generate the `Filter Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_filter_for_space200_response import CreateFilterForSpace200Response
from segment_public_api.models.create_filter_for_space_input import CreateFilterForSpaceInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceFiltersApi(api_client)
    create_filter_for_space_input = {"integrationId":"<id>","name":"Test filter","if":"type = \"track\""} # CreateFilterForSpaceInput | 

    try:
        # Create Filter for Space
        api_response = api_instance.create_filter_for_space(create_filter_for_space_input)
        print("The response of SpaceFiltersApi->create_filter_for_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceFiltersApi->create_filter_for_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_filter_for_space_input** | [**CreateFilterForSpaceInput**](CreateFilterForSpaceInput.md)|  | 

### Return type

[**CreateFilterForSpace200Response**](CreateFilterForSpace200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_filter_by_id

> DeleteFilterById200Response delete_filter_by_id(id)

Delete Filter By Id

Deletes a filter by id.    • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.    • In order to successfully call this endpoint, the specified Workspace needs to have the Space Filters feature enabled. Please reach out to your customer success manager for more information.   • When called, this endpoint may generate the `Filter Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_filter_by_id200_response import DeleteFilterById200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceFiltersApi(api_client)
    id = '<id>' # str | 

    try:
        # Delete Filter By Id
        api_response = api_instance.delete_filter_by_id(id)
        print("The response of SpaceFiltersApi->delete_filter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceFiltersApi->delete_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DeleteFilterById200Response**](DeleteFilterById200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_filter_by_id

> GetFilterById200Response get_filter_by_id(id)

Get Filter By Id

Gets a filter by id.  • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Space Filters feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_filter_by_id200_response import GetFilterById200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceFiltersApi(api_client)
    id = '<id>' # str | 

    try:
        # Get Filter By Id
        api_response = api_instance.get_filter_by_id(id)
        print("The response of SpaceFiltersApi->get_filter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceFiltersApi->get_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetFilterById200Response**](GetFilterById200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: list_filters_for_space

> ListFiltersForSpace200Response list_filters_for_space(integration_id, pagination=pagination)

List Filters for Space

Lists filters for a space.  • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Space Filters feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_filters_for_space200_response import ListFiltersForSpace200Response
from segment_public_api.models.list_filters_pagination_input import ListFiltersPaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceFiltersApi(api_client)
    integration_id = '<id>' # str | The Space Id for which to fetch filters  This parameter exists in beta.
    pagination = segment_public_api.ListFiltersPaginationInput() # ListFiltersPaginationInput | Pagination parameters.  This parameter exists in beta. (optional)

    try:
        # List Filters for Space
        api_response = api_instance.list_filters_for_space(integration_id, pagination=pagination)
        print("The response of SpaceFiltersApi->list_filters_for_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceFiltersApi->list_filters_for_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The Space Id for which to fetch filters  This parameter exists in beta. | 
 **pagination** | [**ListFiltersPaginationInput**](.md)| Pagination parameters.  This parameter exists in beta. | [optional] 

### Return type

[**ListFiltersForSpace200Response**](ListFiltersForSpace200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_filter_by_id

> UpdateFilterById200Response update_filter_by_id(id, update_filter_by_id_input)

Update Filter By Id

Updates a filter by id and replaces the existing filter.    • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.    • In order to successfully call this endpoint, the specified Workspace needs to have the Space Filters feature enabled. Please reach out to your customer success manager for more information.   • When called, this endpoint may generate the `Filter Updated` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_filter_by_id200_response import UpdateFilterById200Response
from segment_public_api.models.update_filter_by_id_input import UpdateFilterByIdInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceFiltersApi(api_client)
    id = '<id>' # str | 
    update_filter_by_id_input = {"integrationId":"<id>","if":"!(type = \"track\")","name":"Test name","enabled":true,"description":"Changed description"} # UpdateFilterByIdInput | 

    try:
        # Update Filter By Id
        api_response = api_instance.update_filter_by_id(id, update_filter_by_id_input)
        print("The response of SpaceFiltersApi->update_filter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceFiltersApi->update_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_filter_by_id_input** | [**UpdateFilterByIdInput**](UpdateFilterByIdInput.md)|  | 

### Return type

[**UpdateFilterById200Response**](UpdateFilterById200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

