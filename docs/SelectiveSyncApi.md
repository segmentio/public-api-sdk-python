# segment_public_api.SelectiveSyncApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_advanced_sync_schedule_from_warehouse**](SelectiveSyncApi.md#get_advanced_sync_schedule_from_warehouse) | **GET** /warehouses/{warehouseId}/advanced-sync-schedule | Get Advanced Sync Schedule from Warehouse
[**list_selective_syncs_from_warehouse_and_source**](SelectiveSyncApi.md#list_selective_syncs_from_warehouse_and_source) | **GET** /warehouses/{warehouseId}/connected-sources/{sourceId}/selective-syncs | List Selective Syncs from Warehouse And Source
[**list_syncs_from_warehouse**](SelectiveSyncApi.md#list_syncs_from_warehouse) | **GET** /warehouses/{warehouseId}/syncs | List Syncs from Warehouse
[**list_syncs_from_warehouse_and_source**](SelectiveSyncApi.md#list_syncs_from_warehouse_and_source) | **GET** /warehouses/{warehouseId}/connected-sources/{sourceId}/syncs | List Syncs from Warehouse And Source
[**replace_advanced_sync_schedule_for_warehouse**](SelectiveSyncApi.md#replace_advanced_sync_schedule_for_warehouse) | **PUT** /warehouses/{warehouseId}/advanced-sync-schedule | Replace Advanced Sync Schedule for Warehouse
[**update_selective_sync_for_warehouse**](SelectiveSyncApi.md#update_selective_sync_for_warehouse) | **PATCH** /warehouses/{warehouseId}/selective-sync | Update Selective Sync for Warehouse



## Operation: get_advanced_sync_schedule_from_warehouse

> GetAdvancedSyncScheduleFromWarehouse200Response get_advanced_sync_schedule_from_warehouse(warehouse_id)

Get Advanced Sync Schedule from Warehouse

Returns the advanced sync schedule for a Warehouse.   The rate limit for this endpoint is 2 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_advanced_sync_schedule_from_warehouse200_response import GetAdvancedSyncScheduleFromWarehouse200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SelectiveSyncApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 

    try:
        # Get Advanced Sync Schedule from Warehouse
        api_response = api_instance.get_advanced_sync_schedule_from_warehouse(warehouse_id)
        print("The response of SelectiveSyncApi->get_advanced_sync_schedule_from_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectiveSyncApi->get_advanced_sync_schedule_from_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 

### Return type

[**GetAdvancedSyncScheduleFromWarehouse200Response**](GetAdvancedSyncScheduleFromWarehouse200Response.md)

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


## Operation: list_selective_syncs_from_warehouse_and_source

> ListSelectiveSyncsFromWarehouseAndSource200Response list_selective_syncs_from_warehouse_and_source(warehouse_id, source_id, pagination=pagination)

List Selective Syncs from Warehouse And Source

Returns the schema for a Warehouse, including Sources, Collections, and Properties.   The rate limit for this endpoint is 2 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_selective_syncs_from_warehouse_and_source200_response import ListSelectiveSyncsFromWarehouseAndSource200Response
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
    api_instance = segment_public_api.SelectiveSyncApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Selective Syncs from Warehouse And Source
        api_response = api_instance.list_selective_syncs_from_warehouse_and_source(warehouse_id, source_id, pagination=pagination)
        print("The response of SelectiveSyncApi->list_selective_syncs_from_warehouse_and_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectiveSyncApi->list_selective_syncs_from_warehouse_and_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **source_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListSelectiveSyncsFromWarehouseAndSource200Response**](ListSelectiveSyncsFromWarehouseAndSource200Response.md)

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


## Operation: list_syncs_from_warehouse

> ListSyncsFromWarehouse200Response list_syncs_from_warehouse(warehouse_id, pagination=pagination)

List Syncs from Warehouse

Returns the overview of syncs for every Source connected to a Warehouse.   The rate limit for this endpoint is 2 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_syncs_from_warehouse200_response import ListSyncsFromWarehouse200Response
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
    api_instance = segment_public_api.SelectiveSyncApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Syncs from Warehouse
        api_response = api_instance.list_syncs_from_warehouse(warehouse_id, pagination=pagination)
        print("The response of SelectiveSyncApi->list_syncs_from_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectiveSyncApi->list_syncs_from_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListSyncsFromWarehouse200Response**](ListSyncsFromWarehouse200Response.md)

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


## Operation: list_syncs_from_warehouse_and_source

> ListSyncsFromWarehouseAndSource200Response list_syncs_from_warehouse_and_source(warehouse_id, source_id, pagination=pagination)

List Syncs from Warehouse And Source

Returns the overview of syncs for a Source connected to a Warehouse.   The rate limit for this endpoint is 2 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_syncs_from_warehouse_and_source200_response import ListSyncsFromWarehouseAndSource200Response
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
    api_instance = segment_public_api.SelectiveSyncApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Syncs from Warehouse And Source
        api_response = api_instance.list_syncs_from_warehouse_and_source(warehouse_id, source_id, pagination=pagination)
        print("The response of SelectiveSyncApi->list_syncs_from_warehouse_and_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectiveSyncApi->list_syncs_from_warehouse_and_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **source_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListSyncsFromWarehouseAndSource200Response**](ListSyncsFromWarehouseAndSource200Response.md)

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


## Operation: replace_advanced_sync_schedule_for_warehouse

> ReplaceAdvancedSyncScheduleForWarehouse200Response replace_advanced_sync_schedule_for_warehouse(warehouse_id, replace_advanced_sync_schedule_for_warehouse_v1_input)

Replace Advanced Sync Schedule for Warehouse

Updates the advanced sync schedule for a Warehouse, replacing the sync schedule with a new schedule.   The rate limit for this endpoint is 2 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_advanced_sync_schedule_for_warehouse200_response import ReplaceAdvancedSyncScheduleForWarehouse200Response
from segment_public_api.models.replace_advanced_sync_schedule_for_warehouse_v1_input import ReplaceAdvancedSyncScheduleForWarehouseV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SelectiveSyncApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    replace_advanced_sync_schedule_for_warehouse_v1_input = {"enabled":true,"schedule":{"times":[{"enabled":true,"hourOfDay":7},{"enabled":false,"hourOfDay":5},{"enabled":true,"hourOfDay":23}],"timezone":"America/Vancouver"}} # ReplaceAdvancedSyncScheduleForWarehouseV1Input | 

    try:
        # Replace Advanced Sync Schedule for Warehouse
        api_response = api_instance.replace_advanced_sync_schedule_for_warehouse(warehouse_id, replace_advanced_sync_schedule_for_warehouse_v1_input)
        print("The response of SelectiveSyncApi->replace_advanced_sync_schedule_for_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectiveSyncApi->replace_advanced_sync_schedule_for_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **replace_advanced_sync_schedule_for_warehouse_v1_input** | [**ReplaceAdvancedSyncScheduleForWarehouseV1Input**](ReplaceAdvancedSyncScheduleForWarehouseV1Input.md)|  | 

### Return type

[**ReplaceAdvancedSyncScheduleForWarehouse200Response**](ReplaceAdvancedSyncScheduleForWarehouse200Response.md)

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


## Operation: update_selective_sync_for_warehouse

> UpdateSelectiveSyncForWarehouse200Response update_selective_sync_for_warehouse(warehouse_id, update_selective_sync_for_warehouse_v1_input)

Update Selective Sync for Warehouse

Configures the schema for a Warehouse, including Sources, Collections, and Properties.    • When called, this endpoint may generate the `Storage Destination Modified` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 2 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_selective_sync_for_warehouse200_response import UpdateSelectiveSyncForWarehouse200Response
from segment_public_api.models.update_selective_sync_for_warehouse_v1_input import UpdateSelectiveSyncForWarehouseV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SelectiveSyncApi(api_client)
    warehouse_id = 'kjU72LCJexvrqL7G4TMHHN' # str | 
    update_selective_sync_for_warehouse_v1_input = {"syncOverrides":[{"sourceId":"rh5BDZp6QDHvXFCkibm1pR","enabled":true,"collection":"checkout_started","property":"context_ip"}]} # UpdateSelectiveSyncForWarehouseV1Input | 

    try:
        # Update Selective Sync for Warehouse
        api_response = api_instance.update_selective_sync_for_warehouse(warehouse_id, update_selective_sync_for_warehouse_v1_input)
        print("The response of SelectiveSyncApi->update_selective_sync_for_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SelectiveSyncApi->update_selective_sync_for_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **str**|  | 
 **update_selective_sync_for_warehouse_v1_input** | [**UpdateSelectiveSyncForWarehouseV1Input**](UpdateSelectiveSyncForWarehouseV1Input.md)|  | 

### Return type

[**UpdateSelectiveSyncForWarehouse200Response**](UpdateSelectiveSyncForWarehouse200Response.md)

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

