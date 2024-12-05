# segment_public_api.WarehousesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_connection_from_source_to_warehouse**](WarehousesApi.md#add_connection_from_source_to_warehouse) | **POST** /warehouses/{warehouseId}/connected-sources/{sourceId} | Add Connection from Source to Warehouse
[**create_validation_in_warehouse**](WarehousesApi.md#create_validation_in_warehouse) | **POST** /warehouses/validation | Create Validation in Warehouse
[**create_warehouse**](WarehousesApi.md#create_warehouse) | **POST** /warehouses | Create Warehouse
[**delete_warehouse**](WarehousesApi.md#delete_warehouse) | **DELETE** /warehouses/{warehouseId} | Delete Warehouse
[**get_connection_state_from_warehouse**](WarehousesApi.md#get_connection_state_from_warehouse) | **GET** /warehouses/{warehouseId}/connection-state | Get Connection State from Warehouse
[**get_warehouse**](WarehousesApi.md#get_warehouse) | **GET** /warehouses/{warehouseId} | Get Warehouse
[**list_connected_sources_from_warehouse**](WarehousesApi.md#list_connected_sources_from_warehouse) | **GET** /warehouses/{warehouseId}/connected-sources | List Connected Sources from Warehouse
[**list_warehouses**](WarehousesApi.md#list_warehouses) | **GET** /warehouses | List Warehouses
[**remove_source_connection_from_warehouse**](WarehousesApi.md#remove_source_connection_from_warehouse) | **DELETE** /warehouses/{warehouseId}/connected-sources/{sourceId} | Remove Source Connection from Warehouse
[**update_warehouse**](WarehousesApi.md#update_warehouse) | **PATCH** /warehouses/{warehouseId} | Update Warehouse



## Operation: add_connection_from_source_to_warehouse

> AddConnectionFromSourceToWarehouse201Response add_connection_from_source_to_warehouse(warehouse_id, source_id)

Add Connection from Source to Warehouse

Connects a Source to a Warehouse.    • When called, this endpoint may generate the `Storage Destination Modified` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_connection_from_source_to_warehouse201_response import AddConnectionFromSourceToWarehouse201Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | 

    try:
        # Add Connection from Source to Warehouse
        api_response = api_instance.add_connection_from_source_to_warehouse(warehouse_id, source_id)
        print("The response of WarehousesApi->add_connection_from_source_to_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->add_connection_from_source_to_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **source_id** | **str**|  | 

### Return type

[**AddConnectionFromSourceToWarehouse201Response**](AddConnectionFromSourceToWarehouse201Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: create_validation_in_warehouse

> CreateValidationInWarehouse200Response create_validation_in_warehouse(create_validation_in_warehouse_v1_input)

Create Validation in Warehouse

Validates input settings against a Warehouse.    • When called, this endpoint may generate the `Storage Destination Settings Validation` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_validation_in_warehouse200_response import CreateValidationInWarehouse200Response
from segment_public_api.models.create_validation_in_warehouse_v1_input import CreateValidationInWarehouseV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    create_validation_in_warehouse_v1_input = {"metadataId":"55d3d3aea3c","settings":{"hostname":"address.us-west-2.redshift.amazonaws.com","port":"5439","database":"db","username":"user","password":"test"}} # CreateValidationInWarehouseV1Input | 

    try:
        # Create Validation in Warehouse
        api_response = api_instance.create_validation_in_warehouse(create_validation_in_warehouse_v1_input)
        print("The response of WarehousesApi->create_validation_in_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->create_validation_in_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_validation_in_warehouse_v1_input** | [**CreateValidationInWarehouseV1Input**](CreateValidationInWarehouseV1Input.md)|  | 

### Return type

[**CreateValidationInWarehouse200Response**](CreateValidationInWarehouse200Response.md)

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


## Operation: create_warehouse

> CreateWarehouse201Response create_warehouse(create_warehouse_v1_input)

Create Warehouse

Creates a new Warehouse.    • When called, this endpoint may generate the `Storage Destination Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_warehouse201_response import CreateWarehouse201Response
from segment_public_api.models.create_warehouse_v1_input import CreateWarehouseV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    create_warehouse_v1_input = {"metadataId":"CCIl4HLQPz","settings":{"username":"CONNECTOR_UNIT_TEST_USER","password":"test_pass","auth_type":"password_auth","account":"segment","warehouse":"ENGINEERING","database":"TEST_DB"}} # CreateWarehouseV1Input | 

    try:
        # Create Warehouse
        api_response = api_instance.create_warehouse(create_warehouse_v1_input)
        print("The response of WarehousesApi->create_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->create_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_warehouse_v1_input** | [**CreateWarehouseV1Input**](CreateWarehouseV1Input.md)|  | 

### Return type

[**CreateWarehouse201Response**](CreateWarehouse201Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_warehouse

> DeleteWarehouse200Response delete_warehouse(warehouse_id)

Delete Warehouse

Deletes an existing Warehouse.    • When called, this endpoint may generate the `Storage Destination Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_warehouse200_response import DeleteWarehouse200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'tmiTtiPi58udvDAjcxKUJY' # str | 

    try:
        # Delete Warehouse
        api_response = api_instance.delete_warehouse(warehouse_id)
        print("The response of WarehousesApi->delete_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->delete_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 

### Return type

[**DeleteWarehouse200Response**](DeleteWarehouse200Response.md)

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


## Operation: get_connection_state_from_warehouse

> GetConnectionStateFromWarehouse200Response get_connection_state_from_warehouse(warehouse_id)

Get Connection State from Warehouse

Verifies the state of Warehouse connection settings.   The rate limit for this endpoint is 200 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_connection_state_from_warehouse200_response import GetConnectionStateFromWarehouse200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 

    try:
        # Get Connection State from Warehouse
        api_response = api_instance.get_connection_state_from_warehouse(warehouse_id)
        print("The response of WarehousesApi->get_connection_state_from_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->get_connection_state_from_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 

### Return type

[**GetConnectionStateFromWarehouse200Response**](GetConnectionStateFromWarehouse200Response.md)

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


## Operation: get_warehouse

> GetWarehouse200Response get_warehouse(warehouse_id)

Get Warehouse

Returns a Warehouse by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_warehouse200_response import GetWarehouse200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 

    try:
        # Get Warehouse
        api_response = api_instance.get_warehouse(warehouse_id)
        print("The response of WarehousesApi->get_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->get_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 

### Return type

[**GetWarehouse200Response**](GetWarehouse200Response.md)

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


## Operation: list_connected_sources_from_warehouse

> ListConnectedSourcesFromWarehouse200Response list_connected_sources_from_warehouse(warehouse_id, pagination=pagination)

List Connected Sources from Warehouse

Returns the list of Sources that are connected to a Warehouse.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_connected_sources_from_warehouse200_response import ListConnectedSourcesFromWarehouse200Response
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
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Connected Sources from Warehouse
        api_response = api_instance.list_connected_sources_from_warehouse(warehouse_id, pagination=pagination)
        print("The response of WarehousesApi->list_connected_sources_from_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->list_connected_sources_from_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListConnectedSourcesFromWarehouse200Response**](ListConnectedSourcesFromWarehouse200Response.md)

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


## Operation: list_warehouses

> ListWarehouses200Response list_warehouses(pagination=pagination)

List Warehouses

Returns a list of Warehouses.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_warehouses200_response import ListWarehouses200Response
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
    api_instance = segment_public_api.WarehousesApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Warehouses
        api_response = api_instance.list_warehouses(pagination=pagination)
        print("The response of WarehousesApi->list_warehouses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->list_warehouses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListWarehouses200Response**](ListWarehouses200Response.md)

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


## Operation: remove_source_connection_from_warehouse

> RemoveSourceConnectionFromWarehouse200Response remove_source_connection_from_warehouse(warehouse_id, source_id)

Remove Source Connection from Warehouse

Disconnects a Source from a Warehouse.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_source_connection_from_warehouse200_response import RemoveSourceConnectionFromWarehouse200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | 

    try:
        # Remove Source Connection from Warehouse
        api_response = api_instance.remove_source_connection_from_warehouse(warehouse_id, source_id)
        print("The response of WarehousesApi->remove_source_connection_from_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->remove_source_connection_from_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **source_id** | **str**|  | 

### Return type

[**RemoveSourceConnectionFromWarehouse200Response**](RemoveSourceConnectionFromWarehouse200Response.md)

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


## Operation: update_warehouse

> UpdateWarehouse200Response update_warehouse(warehouse_id, update_warehouse_v1_input)

Update Warehouse

Updates an existing Warehouse.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Storage Destination Modified * Storage Destination Enabled       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_warehouse200_response import UpdateWarehouse200Response
from segment_public_api.models.update_warehouse_v1_input import UpdateWarehouseV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WarehousesApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    update_warehouse_v1_input = {"name":"Redshift Dev","settings":{}} # UpdateWarehouseV1Input | 

    try:
        # Update Warehouse
        api_response = api_instance.update_warehouse(warehouse_id, update_warehouse_v1_input)
        print("The response of WarehousesApi->update_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->update_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **update_warehouse_v1_input** | [**UpdateWarehouseV1Input**](UpdateWarehouseV1Input.md)|  | 

### Return type

[**UpdateWarehouse200Response**](UpdateWarehouse200Response.md)

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

