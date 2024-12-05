# segment_public_api.ProfilesSyncApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_profiles_warehouse**](ProfilesSyncApi.md#create_profiles_warehouse) | **POST** /spaces/{spaceId}/profiles-warehouses | Create Profiles Warehouse
[**list_profiles_warehouse_in_space**](ProfilesSyncApi.md#list_profiles_warehouse_in_space) | **GET** /spaces/{spaceId}/profiles-warehouses | List Profiles Warehouse in Space
[**list_selective_syncs_from_warehouse_and_space**](ProfilesSyncApi.md#list_selective_syncs_from_warehouse_and_space) | **GET** /spaces/{spaceId}/profiles-warehouses/{warehouseId}/selective-syncs | List Selective Syncs from Warehouse And Space
[**remove_profiles_warehouse_from_space**](ProfilesSyncApi.md#remove_profiles_warehouse_from_space) | **DELETE** /spaces/{spaceId}/profiles-warehouses/{warehouseId} | Remove Profiles Warehouse from Space
[**update_profiles_warehouse_for_space_warehouse**](ProfilesSyncApi.md#update_profiles_warehouse_for_space_warehouse) | **PATCH** /spaces/{spaceId}/profiles-warehouses/{warehouseId} | Update Profiles Warehouse for Space Warehouse
[**update_selective_sync_for_warehouse_and_space**](ProfilesSyncApi.md#update_selective_sync_for_warehouse_and_space) | **PATCH** /spaces/{spaceId}/profiles-warehouses/{warehouseId}/selective-syncs | Update Selective Sync for Warehouse And Space



## Operation: create_profiles_warehouse

> CreateProfilesWarehouse201Response create_profiles_warehouse(space_id, create_profiles_warehouse_alpha_input)

Create Profiles Warehouse

Creates a new Profiles Warehouse.    • When called, this endpoint may generate the `Profiles Sync Warehouse Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_profiles_warehouse201_response import CreateProfilesWarehouse201Response
from segment_public_api.models.create_profiles_warehouse_alpha_input import CreateProfilesWarehouseAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ProfilesSyncApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    create_profiles_warehouse_alpha_input = {"metadataId":"CCIl4HLQPz","settings":{"username":"CONNECTOR_UNIT_TEST_USER","password":"test_password","auth_type":"password_auth","account":"segment","warehouse":"ENGINEERING","database":"TEST_DB"},"enabled":true} # CreateProfilesWarehouseAlphaInput | 

    try:
        # Create Profiles Warehouse
        api_response = api_instance.create_profiles_warehouse(space_id, create_profiles_warehouse_alpha_input)
        print("The response of ProfilesSyncApi->create_profiles_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesSyncApi->create_profiles_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_profiles_warehouse_alpha_input** | [**CreateProfilesWarehouseAlphaInput**](CreateProfilesWarehouseAlphaInput.md)|  | 

### Return type

[**CreateProfilesWarehouse201Response**](CreateProfilesWarehouse201Response.md)

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


## Operation: list_profiles_warehouse_in_space

> ListProfilesWarehouseInSpace200Response list_profiles_warehouse_in_space(space_id, pagination=pagination)

List Profiles Warehouse in Space

Lists all Profile Warehouses for a given space id.    • When called, this endpoint may generate the `Profiles Sync Warehouse Retrieved` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_profiles_warehouse_in_space200_response import ListProfilesWarehouseInSpace200Response
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
    api_instance = segment_public_api.ProfilesSyncApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in alpha. (optional)

    try:
        # List Profiles Warehouse in Space
        api_response = api_instance.list_profiles_warehouse_in_space(space_id, pagination=pagination)
        print("The response of ProfilesSyncApi->list_profiles_warehouse_in_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesSyncApi->list_profiles_warehouse_in_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in alpha. | [optional] 

### Return type

[**ListProfilesWarehouseInSpace200Response**](ListProfilesWarehouseInSpace200Response.md)

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


## Operation: list_selective_syncs_from_warehouse_and_space

> ListSelectiveSyncsFromWarehouseAndSpace200Response list_selective_syncs_from_warehouse_and_space(space_id, warehouse_id, pagination=pagination)

List Selective Syncs from Warehouse And Space

Returns the schema for a Space Warehouse connection, including Collections and Properties.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_selective_syncs_from_warehouse_and_space200_response import ListSelectiveSyncsFromWarehouseAndSpace200Response
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
    api_instance = segment_public_api.ProfilesSyncApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    warehouse_id = 'fQyLbqjfwaqg9mr3hDQ7We' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in alpha. (optional)

    try:
        # List Selective Syncs from Warehouse And Space
        api_response = api_instance.list_selective_syncs_from_warehouse_and_space(space_id, warehouse_id, pagination=pagination)
        print("The response of ProfilesSyncApi->list_selective_syncs_from_warehouse_and_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesSyncApi->list_selective_syncs_from_warehouse_and_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in alpha. | [optional] 

### Return type

[**ListSelectiveSyncsFromWarehouseAndSpace200Response**](ListSelectiveSyncsFromWarehouseAndSpace200Response.md)

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


## Operation: remove_profiles_warehouse_from_space

> RemoveProfilesWarehouseFromSpace200Response remove_profiles_warehouse_from_space(space_id, warehouse_id)

Remove Profiles Warehouse from Space

Deletes an existing Profiles Warehouse.    • When called, this endpoint may generate the `Profiles Sync Warehouse Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_profiles_warehouse_from_space200_response import RemoveProfilesWarehouseFromSpace200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ProfilesSyncApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    warehouse_id = 'qABd3NVTPfTLQ3kXWoBhgi' # str | 

    try:
        # Remove Profiles Warehouse from Space
        api_response = api_instance.remove_profiles_warehouse_from_space(space_id, warehouse_id)
        print("The response of ProfilesSyncApi->remove_profiles_warehouse_from_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesSyncApi->remove_profiles_warehouse_from_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **warehouse_id** | **str**|  | 

### Return type

[**RemoveProfilesWarehouseFromSpace200Response**](RemoveProfilesWarehouseFromSpace200Response.md)

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


## Operation: update_profiles_warehouse_for_space_warehouse

> UpdateProfilesWarehouseForSpaceWarehouse200Response update_profiles_warehouse_for_space_warehouse(space_id, warehouse_id, update_profiles_warehouse_for_space_warehouse_alpha_input)

Update Profiles Warehouse for Space Warehouse

Updates an existing Profiles Warehouse.    • When called, this endpoint may generate the `Profiles Sync Warehouse Updated` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_profiles_warehouse_for_space_warehouse200_response import UpdateProfilesWarehouseForSpaceWarehouse200Response
from segment_public_api.models.update_profiles_warehouse_for_space_warehouse_alpha_input import UpdateProfilesWarehouseForSpaceWarehouseAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ProfilesSyncApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    warehouse_id = '3eadBBqVMQD2DEtaWXSkqA' # str | 
    update_profiles_warehouse_for_space_warehouse_alpha_input = {"settings":{},"enabled":false,"name":"testing"} # UpdateProfilesWarehouseForSpaceWarehouseAlphaInput | 

    try:
        # Update Profiles Warehouse for Space Warehouse
        api_response = api_instance.update_profiles_warehouse_for_space_warehouse(space_id, warehouse_id, update_profiles_warehouse_for_space_warehouse_alpha_input)
        print("The response of ProfilesSyncApi->update_profiles_warehouse_for_space_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesSyncApi->update_profiles_warehouse_for_space_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **update_profiles_warehouse_for_space_warehouse_alpha_input** | [**UpdateProfilesWarehouseForSpaceWarehouseAlphaInput**](UpdateProfilesWarehouseForSpaceWarehouseAlphaInput.md)|  | 

### Return type

[**UpdateProfilesWarehouseForSpaceWarehouse200Response**](UpdateProfilesWarehouseForSpaceWarehouse200Response.md)

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


## Operation: update_selective_sync_for_warehouse_and_space

> UpdateSelectiveSyncForWarehouseAndSpace200Response update_selective_sync_for_warehouse_and_space(space_id, warehouse_id, update_selective_sync_for_warehouse_and_space_alpha_input)

Update Selective Sync for Warehouse And Space

Updates the schema for a Space Warehouse connection, including Collections and Properties.    • When called, this endpoint may generate the `Profiles Sync Warehouse Modified` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_selective_sync_for_warehouse_and_space200_response import UpdateSelectiveSyncForWarehouseAndSpace200Response
from segment_public_api.models.update_selective_sync_for_warehouse_and_space_alpha_input import UpdateSelectiveSyncForWarehouseAndSpaceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ProfilesSyncApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    warehouse_id = 'qABd3NVTPfTLQ3kXWoBhgi' # str | 
    update_selective_sync_for_warehouse_and_space_alpha_input = {"syncOverrides":[{"enabled":true,"collection":"tracks","property":"context_ip"}]} # UpdateSelectiveSyncForWarehouseAndSpaceAlphaInput | 

    try:
        # Update Selective Sync for Warehouse And Space
        api_response = api_instance.update_selective_sync_for_warehouse_and_space(space_id, warehouse_id, update_selective_sync_for_warehouse_and_space_alpha_input)
        print("The response of ProfilesSyncApi->update_selective_sync_for_warehouse_and_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesSyncApi->update_selective_sync_for_warehouse_and_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **warehouse_id** | **str**|  | 
 **update_selective_sync_for_warehouse_and_space_alpha_input** | [**UpdateSelectiveSyncForWarehouseAndSpaceAlphaInput**](UpdateSelectiveSyncForWarehouseAndSpaceAlphaInput.md)|  | 

### Return type

[**UpdateSelectiveSyncForWarehouseAndSpace200Response**](UpdateSelectiveSyncForWarehouseAndSpace200Response.md)

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

