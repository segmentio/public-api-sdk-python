# segment_public_api.CatalogApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_destination_metadata**](CatalogApi.md#get_destination_metadata) | **GET** /catalog/destinations/{destinationMetadataId} | Get Destination Metadata
[**get_destinations_catalog**](CatalogApi.md#get_destinations_catalog) | **GET** /catalog/destinations | Get Destinations Catalog
[**get_source_metadata**](CatalogApi.md#get_source_metadata) | **GET** /catalog/sources/{sourceMetadataId} | Get Source Metadata
[**get_sources_catalog**](CatalogApi.md#get_sources_catalog) | **GET** /catalog/sources | Get Sources Catalog
[**get_warehouse_metadata**](CatalogApi.md#get_warehouse_metadata) | **GET** /catalog/warehouses/{warehouseMetadataId} | Get Warehouse Metadata
[**get_warehouses_catalog**](CatalogApi.md#get_warehouses_catalog) | **GET** /catalog/warehouses | Get Warehouses Catalog



## Operation: get_destination_metadata

> GetDestinationMetadata200Response get_destination_metadata(destination_metadata_id)

Get Destination Metadata

Returns a Destination catalog item by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_destination_metadata200_response import GetDestinationMetadata200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CatalogApi(api_client)
    destination_metadata_id = '54521fd525e721e32a72ee91' # str | 

    try:
        # Get Destination Metadata
        api_response = api_instance.get_destination_metadata(destination_metadata_id)
        print("The response of CatalogApi->get_destination_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_destination_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_metadata_id** | **str**|  | 

### Return type

[**GetDestinationMetadata200Response**](GetDestinationMetadata200Response.md)

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


## Operation: get_destinations_catalog

> GetDestinationsCatalog200Response get_destinations_catalog(pagination=pagination)

Get Destinations Catalog

Returns a list of all available Destinations in the Segment catalog.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_destinations_catalog200_response import GetDestinationsCatalog200Response
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
    api_instance = segment_public_api.CatalogApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Required pagination parameters used to filter the Destinations catalog.  This parameter exists in v1. (optional)

    try:
        # Get Destinations Catalog
        api_response = api_instance.get_destinations_catalog(pagination=pagination)
        print("The response of CatalogApi->get_destinations_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_destinations_catalog: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Required pagination parameters used to filter the Destinations catalog.  This parameter exists in v1. | [optional] 

### Return type

[**GetDestinationsCatalog200Response**](GetDestinationsCatalog200Response.md)

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


## Operation: get_source_metadata

> GetSourceMetadata200Response get_source_metadata(source_metadata_id)

Get Source Metadata

Returns a Source catalog item by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_source_metadata200_response import GetSourceMetadata200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CatalogApi(api_client)
    source_metadata_id = '1bow82lmk' # str | 

    try:
        # Get Source Metadata
        api_response = api_instance.get_source_metadata(source_metadata_id)
        print("The response of CatalogApi->get_source_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_source_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_metadata_id** | **str**|  | 

### Return type

[**GetSourceMetadata200Response**](GetSourceMetadata200Response.md)

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


## Operation: get_sources_catalog

> GetSourcesCatalog200Response get_sources_catalog(pagination=pagination)

Get Sources Catalog

Returns a list of all available Sources in the Segment catalog.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_sources_catalog200_response import GetSourcesCatalog200Response
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
    api_instance = segment_public_api.CatalogApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # Get Sources Catalog
        api_response = api_instance.get_sources_catalog(pagination=pagination)
        print("The response of CatalogApi->get_sources_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_sources_catalog: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**GetSourcesCatalog200Response**](GetSourcesCatalog200Response.md)

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


## Operation: get_warehouse_metadata

> GetWarehouseMetadata200Response get_warehouse_metadata(warehouse_metadata_id)

Get Warehouse Metadata

Returns a Warehouse catalog item by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_warehouse_metadata200_response import GetWarehouseMetadata200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CatalogApi(api_client)
    warehouse_metadata_id = '55d3d3aea3c' # str | 

    try:
        # Get Warehouse Metadata
        api_response = api_instance.get_warehouse_metadata(warehouse_metadata_id)
        print("The response of CatalogApi->get_warehouse_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_warehouse_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_metadata_id** | **str**|  | 

### Return type

[**GetWarehouseMetadata200Response**](GetWarehouseMetadata200Response.md)

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


## Operation: get_warehouses_catalog

> GetWarehousesCatalog200Response get_warehouses_catalog(pagination=pagination)

Get Warehouses Catalog

Returns a list of all available Warehouses in the Segment catalog.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_warehouses_catalog200_response import GetWarehousesCatalog200Response
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
    api_instance = segment_public_api.CatalogApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Optional pagination params used to filter the Warehouses catalog.  This parameter exists in v1. (optional)

    try:
        # Get Warehouses Catalog
        api_response = api_instance.get_warehouses_catalog(pagination=pagination)
        print("The response of CatalogApi->get_warehouses_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogApi->get_warehouses_catalog: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Optional pagination params used to filter the Warehouses catalog.  This parameter exists in v1. | [optional] 

### Return type

[**GetWarehousesCatalog200Response**](GetWarehousesCatalog200Response.md)

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

