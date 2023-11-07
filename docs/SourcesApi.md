# segment_public_api.SourcesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_labels_to_source**](SourcesApi.md#add_labels_to_source) | **POST** /sources/{sourceId}/labels | Add Labels to Source
[**create_source**](SourcesApi.md#create_source) | **POST** /sources | Create Source
[**delete_source**](SourcesApi.md#delete_source) | **DELETE** /sources/{sourceId} | Delete Source
[**get_source**](SourcesApi.md#get_source) | **GET** /sources/{sourceId} | Get Source
[**list_connected_destinations_from_source**](SourcesApi.md#list_connected_destinations_from_source) | **GET** /sources/{sourceId}/connected-destinations | List Connected Destinations from Source
[**list_connected_warehouses_from_source**](SourcesApi.md#list_connected_warehouses_from_source) | **GET** /sources/{sourceId}/connected-warehouses | List Connected Warehouses from Source
[**list_schema_settings_in_source**](SourcesApi.md#list_schema_settings_in_source) | **GET** /sources/{sourceId}/settings | List Schema Settings in Source
[**list_sources**](SourcesApi.md#list_sources) | **GET** /sources | List Sources
[**replace_labels_in_source**](SourcesApi.md#replace_labels_in_source) | **PUT** /sources/{sourceId}/labels | Replace Labels in Source
[**update_schema_settings_in_source**](SourcesApi.md#update_schema_settings_in_source) | **PATCH** /sources/{sourceId}/settings | Update Schema Settings in Source
[**update_source**](SourcesApi.md#update_source) | **PATCH** /sources/{sourceId} | Update Source



## Operation: add_labels_to_source

> AddLabelsToSource200Response add_labels_to_source(source_id, add_labels_to_source_v1_input)

Add Labels to Source

Adds an existing label to a Source.    • When called, this endpoint may generate the `Source Modified` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_labels_to_source200_response import AddLabelsToSource200Response
from segment_public_api.models.add_labels_to_source_v1_input import AddLabelsToSourceV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | 
    add_labels_to_source_v1_input = {"labels":[{"key":"type","value":"web"}]} # AddLabelsToSourceV1Input | 

    try:
        # Add Labels to Source
        api_response = api_instance.add_labels_to_source(source_id, add_labels_to_source_v1_input)
        print("The response of SourcesApi->add_labels_to_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->add_labels_to_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **add_labels_to_source_v1_input** | [**AddLabelsToSourceV1Input**](AddLabelsToSourceV1Input.md)|  | 

### Return type

[**AddLabelsToSource200Response**](AddLabelsToSource200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: create_source

> CreateSource200Response create_source(create_source_v1_input)

Create Source

Creates a new Source.    • When called, this endpoint may generate the `Source Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_source200_response import CreateSource200Response
from segment_public_api.models.create_source_v1_input import CreateSourceV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    create_source_v1_input = {"slug":"my-test-source-rhpd18","enabled":true,"metadataId":"IqDTy1TpoU","settings":{}} # CreateSourceV1Input | 

    try:
        # Create Source
        api_response = api_instance.create_source(create_source_v1_input)
        print("The response of SourcesApi->create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->create_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_source_v1_input** | [**CreateSourceV1Input**](CreateSourceV1Input.md)|  | 

### Return type

[**CreateSource200Response**](CreateSource200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_source

> DeleteSource200Response delete_source(source_id)

Delete Source

Deletes an existing Source.    • When called, this endpoint may generate the `Source Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_source200_response import DeleteSource200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = '48EFjyXH4zdbKWx4vKiLuE' # str | 

    try:
        # Delete Source
        api_response = api_instance.delete_source(source_id)
        print("The response of SourcesApi->delete_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->delete_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**DeleteSource200Response**](DeleteSource200Response.md)

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


## Operation: get_source

> GetSource200Response get_source(source_id)

Get Source

Returns a Source by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_source200_response import GetSource200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Get Source
        api_response = api_instance.get_source(source_id)
        print("The response of SourcesApi->get_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->get_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**GetSource200Response**](GetSource200Response.md)

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


## Operation: list_connected_destinations_from_source

> ListConnectedDestinationsFromSource200Response list_connected_destinations_from_source(source_id, pagination)

List Connected Destinations from Source

Returns a list of Destinations connected to a Source.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_connected_destinations_from_source200_response import ListConnectedDestinationsFromSource200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    pagination = segment_public_api.PaginationInput() # PaginationInput | Required pagination params for the request.  This parameter exists in alpha.

    try:
        # List Connected Destinations from Source
        api_response = api_instance.list_connected_destinations_from_source(source_id, pagination)
        print("The response of SourcesApi->list_connected_destinations_from_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->list_connected_destinations_from_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Required pagination params for the request.  This parameter exists in alpha. | 

### Return type

[**ListConnectedDestinationsFromSource200Response**](ListConnectedDestinationsFromSource200Response.md)

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


## Operation: list_connected_warehouses_from_source

> ListConnectedWarehousesFromSource200Response list_connected_warehouses_from_source(source_id, pagination)

List Connected Warehouses from Source

Returns a list of Warehouses connected to a Source.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_connected_warehouses_from_source200_response import ListConnectedWarehousesFromSource200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    pagination = segment_public_api.PaginationInput() # PaginationInput | Required pagination params for the request.  This parameter exists in alpha.

    try:
        # List Connected Warehouses from Source
        api_response = api_instance.list_connected_warehouses_from_source(source_id, pagination)
        print("The response of SourcesApi->list_connected_warehouses_from_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->list_connected_warehouses_from_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Required pagination params for the request.  This parameter exists in alpha. | 

### Return type

[**ListConnectedWarehousesFromSource200Response**](ListConnectedWarehousesFromSource200Response.md)

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


## Operation: list_schema_settings_in_source

> ListSchemaSettingsInSource200Response list_schema_settings_in_source(source_id)

List Schema Settings in Source

Retrieves the schema configuration settings for a Source. If Protocols is not enabled for the Source, the configurations specific to Protocols will have default values.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_schema_settings_in_source200_response import ListSchemaSettingsInSource200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # List Schema Settings in Source
        api_response = api_instance.list_schema_settings_in_source(source_id)
        print("The response of SourcesApi->list_schema_settings_in_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->list_schema_settings_in_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**ListSchemaSettingsInSource200Response**](ListSchemaSettingsInSource200Response.md)

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


## Operation: list_sources

> ListSources200Response list_sources(pagination)

List Sources

Returns a list of Sources.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_sources200_response import ListSources200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    pagination = segment_public_api.PaginationInput() # PaginationInput | Defines the pagination parameters.  This parameter exists in alpha.

    try:
        # List Sources
        api_response = api_instance.list_sources(pagination)
        print("The response of SourcesApi->list_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->list_sources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in alpha. | 

### Return type

[**ListSources200Response**](ListSources200Response.md)

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


## Operation: replace_labels_in_source

> ReplaceLabelsInSource200Response replace_labels_in_source(source_id, replace_labels_in_source_v1_input)

Replace Labels in Source

Replaces all labels in a Source.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_labels_in_source200_response import ReplaceLabelsInSource200Response
from segment_public_api.models.replace_labels_in_source_v1_input import ReplaceLabelsInSourceV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | 
    replace_labels_in_source_v1_input = {"labels":[{"key":"environment","value":"prod"}]} # ReplaceLabelsInSourceV1Input | 

    try:
        # Replace Labels in Source
        api_response = api_instance.replace_labels_in_source(source_id, replace_labels_in_source_v1_input)
        print("The response of SourcesApi->replace_labels_in_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->replace_labels_in_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **replace_labels_in_source_v1_input** | [**ReplaceLabelsInSourceV1Input**](ReplaceLabelsInSourceV1Input.md)|  | 

### Return type

[**ReplaceLabelsInSource200Response**](ReplaceLabelsInSource200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_schema_settings_in_source

> UpdateSchemaSettingsInSource200Response update_schema_settings_in_source(source_id, update_schema_settings_in_source_v1_input)

Update Schema Settings in Source

Updates the schema configuration for a Source. If Protocols is not enabled for the Source, any updates to Protocols-specific configurations will not be applied.        Config API omitted fields: - `updateMask`       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_schema_settings_in_source200_response import UpdateSchemaSettingsInSource200Response
from segment_public_api.models.update_schema_settings_in_source_v1_input import UpdateSchemaSettingsInSourceV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    update_schema_settings_in_source_v1_input = {"group":{"allowTraitsOnViolations":false,"allowUnplannedTraits":false,"commonEventOnViolations":"ALLOW"},"identify":{"allowTraitsOnViolations":true,"allowUnplannedTraits":true,"commonEventOnViolations":"BLOCK"},"track":{"allowEventOnViolations":false,"allowPropertiesOnViolations":false,"allowUnplannedEventProperties":false,"allowUnplannedEvents":false,"commonEventOnViolations":"OMIT_PROPERTIES"},"forwardingViolationsTo":"rh5BDZp6QDHvXFCkibm1pR","forwardingBlockedEventsTo":"rh5BDZp6QDHvXFCkibm1pR"} # UpdateSchemaSettingsInSourceV1Input | 

    try:
        # Update Schema Settings in Source
        api_response = api_instance.update_schema_settings_in_source(source_id, update_schema_settings_in_source_v1_input)
        print("The response of SourcesApi->update_schema_settings_in_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_schema_settings_in_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **update_schema_settings_in_source_v1_input** | [**UpdateSchemaSettingsInSourceV1Input**](UpdateSchemaSettingsInSourceV1Input.md)|  | 

### Return type

[**UpdateSchemaSettingsInSource200Response**](UpdateSchemaSettingsInSource200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_source

> UpdateSource200Response update_source(source_id, update_source_v1_input)

Update Source

Updates an existing Source.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Source Modified * Source Enabled * Source Settings Modified * Source Disabled  Config API omitted fields: - `updateMask` 

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_source200_response import UpdateSource200Response
from segment_public_api.models.update_source_v1_input import UpdateSourceV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SourcesApi(api_client)
    source_id = 'piTVHEYNrRgBMM1uQGCPbK' # str | 
    update_source_v1_input = {"name":"My updated source","enabled":false} # UpdateSourceV1Input | 

    try:
        # Update Source
        api_response = api_instance.update_source(source_id, update_source_v1_input)
        print("The response of SourcesApi->update_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->update_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **update_source_v1_input** | [**UpdateSourceV1Input**](UpdateSourceV1Input.md)|  | 

### Return type

[**UpdateSource200Response**](UpdateSource200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

