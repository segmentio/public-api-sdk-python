# segment_public_api.FiltersApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filter**](FiltersApi.md#create_filter) | **POST** /filters/create/{integrationId} | Create Filter
[**delete_filter_by_id**](FiltersApi.md#delete_filter_by_id) | **DELETE** /filters/delete/{id} | Delete Filter By Id
[**get_filter_by_id**](FiltersApi.md#get_filter_by_id) | **GET** /filters/filter/{id} | Get Filter By Id
[**list_filters_by_integration_id**](FiltersApi.md#list_filters_by_integration_id) | **GET** /filters/{integrationId} | List Filters By Integration Id
[**update_filter_by_id**](FiltersApi.md#update_filter_by_id) | **PATCH** /filters/update/{id} | Update Filter By Id



## Operation: create_filter

> create_filter(integration_id, create_filter_input)

Create Filter

Creates a filter.    • When called, this endpoint may generate the `Filter Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_filter_input import CreateFilterInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FiltersApi(api_client)
    integration_id = '<id>' # str | 
    create_filter_input = {"name":"Test filter","if":"type = \"track\""} # CreateFilterInput | 

    try:
        # Create Filter
        api_instance.create_filter(integration_id, create_filter_input)
    except Exception as e:
        print("Exception when calling FiltersApi->create_filter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **create_filter_input** | [**CreateFilterInput**](CreateFilterInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_filter_by_id

> delete_filter_by_id(id, product_area)

Delete Filter By Id

Deletes a filter by id.    • When called, this endpoint may generate the `Filter Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FiltersApi(api_client)
    id = '<id>' # str | 
    product_area = 'spaces' # str | The product area of the filter  This parameter exists in alpha.

    try:
        # Delete Filter By Id
        api_instance.delete_filter_by_id(id, product_area)
    except Exception as e:
        print("Exception when calling FiltersApi->delete_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **product_area** | **str**| The product area of the filter  This parameter exists in alpha. | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_filter_by_id

> get_filter_by_id(id, product_area)

Get Filter By Id

Gets a filter by id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FiltersApi(api_client)
    id = '<id>' # str | 
    product_area = 'spaces' # str | The product area of the filter, which should be spaces (endpoint table should be able to determine the resource)  This parameter exists in alpha.

    try:
        # Get Filter By Id
        api_instance.get_filter_by_id(id, product_area)
    except Exception as e:
        print("Exception when calling FiltersApi->get_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **product_area** | **str**| The product area of the filter, which should be spaces (endpoint table should be able to determine the resource)  This parameter exists in alpha. | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: list_filters_by_integration_id

> list_filters_by_integration_id(integration_id, product_area, pagination=pagination)

List Filters By Integration Id

Lists filters by integration id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
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
    api_instance = segment_public_api.FiltersApi(api_client)
    integration_id = '<id>' # str | 
    product_area = 'spaces' # str | The product area of the filter, which should be spaces (endpoint table should be able to determine the resource)  This parameter exists in alpha.
    pagination = segment_public_api.ListFiltersPaginationInput() # ListFiltersPaginationInput | Pagination parameters.  This parameter exists in alpha. (optional)

    try:
        # List Filters By Integration Id
        api_instance.list_filters_by_integration_id(integration_id, product_area, pagination=pagination)
    except Exception as e:
        print("Exception when calling FiltersApi->list_filters_by_integration_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **product_area** | **str**| The product area of the filter, which should be spaces (endpoint table should be able to determine the resource)  This parameter exists in alpha. | 
 **pagination** | [**ListFiltersPaginationInput**](.md)| Pagination parameters.  This parameter exists in alpha. | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_filter_by_id

> update_filter_by_id(id, update_filter_by_id_input)

Update Filter By Id

Updates a filter by id.    • When called, this endpoint may generate the `Filter Updated` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
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
    api_instance = segment_public_api.FiltersApi(api_client)
    id = '<id>' # str | 
    update_filter_by_id_input = {"integrationId":"<id>","name":"Test name","enabled":true,"description":"Changed description"} # UpdateFilterByIdInput | 

    try:
        # Update Filter By Id
        api_instance.update_filter_by_id(id, update_filter_by_id_input)
    except Exception as e:
        print("Exception when calling FiltersApi->update_filter_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_filter_by_id_input** | [**UpdateFilterByIdInput**](UpdateFilterByIdInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

