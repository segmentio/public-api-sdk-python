# segment_public_api.DeletionAndSuppressionApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_source_regulation**](DeletionAndSuppressionApi.md#create_cloud_source_regulation) | **POST** /regulations/cloudsources/{sourceId} | Create Cloud Source Regulation
[**create_source_regulation**](DeletionAndSuppressionApi.md#create_source_regulation) | **POST** /regulations/sources/{sourceId} | Create Source Regulation
[**create_workspace_regulation**](DeletionAndSuppressionApi.md#create_workspace_regulation) | **POST** /regulations | Create Workspace Regulation
[**delete_regulation**](DeletionAndSuppressionApi.md#delete_regulation) | **DELETE** /regulations/{regulateId} | Delete Regulation
[**get_regulation**](DeletionAndSuppressionApi.md#get_regulation) | **GET** /regulations/{regulateId} | Get Regulation
[**list_regulations_from_source**](DeletionAndSuppressionApi.md#list_regulations_from_source) | **GET** /regulations/sources/{sourceId} | List Regulations from Source
[**list_suppressions**](DeletionAndSuppressionApi.md#list_suppressions) | **GET** /suppressions | List Suppressions
[**list_workspace_regulations**](DeletionAndSuppressionApi.md#list_workspace_regulations) | **GET** /regulations | List Workspace Regulations



## Operation: create_cloud_source_regulation

> CreateCloudSourceRegulation200Response create_cloud_source_regulation(source_id, create_cloud_source_regulation_v1_input)

Create Cloud Source Regulation

Creates a Source-scoped regulation.    Please Note: Suppression rules at the Workspace level take precedence over those at the Source level. If a user has been suppressed at the Workspace level, any attempt to un-suppress at the Source level is not supported and the processing of the request will fail in Segment    Config API omitted fields: - `attributes`, - `userAgent`  Rate limit headers: - X-Regulation-RateLimit-Remaining: Remaining requests in the current period (stringified integer) - X-Regulation-RateLimit-Quota-Reset: ISO 8601 timestamp for when the quota resets (e.g., 2024-12-31T23:59:59.000Z)   

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_cloud_source_regulation200_response import CreateCloudSourceRegulation200Response
from segment_public_api.models.create_cloud_source_regulation_v1_input import CreateCloudSourceRegulationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    create_cloud_source_regulation_v1_input = {"regulationType":"SUPPRESS_ONLY","subjectType":"OBJECT_ID","subjectIds":["test_object_id"],"collection":"some-app-collection"} # CreateCloudSourceRegulationV1Input | 

    try:
        # Create Cloud Source Regulation
        api_response = api_instance.create_cloud_source_regulation(source_id, create_cloud_source_regulation_v1_input)
        print("The response of DeletionAndSuppressionApi->create_cloud_source_regulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->create_cloud_source_regulation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **create_cloud_source_regulation_v1_input** | [**CreateCloudSourceRegulationV1Input**](CreateCloudSourceRegulationV1Input.md)|  | 

### Return type

[**CreateCloudSourceRegulation200Response**](CreateCloudSourceRegulation200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Regulation-RateLimit-Remaining - Remaining requests in the current period <br>  * X-Regulation-RateLimit-Quota-Reset - ISO 8601 timestamp for when the quota resets <br>  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: create_source_regulation

> CreateSourceRegulation200Response create_source_regulation(source_id, create_source_regulation_v1_input)

Create Source Regulation

Creates a Source-scoped regulation.    Please Note: Suppression rules at the Workspace level take precedence over those at the Source level. If a user has been suppressed at the Workspace level, any attempt to un-suppress at the Source level is not supported and the processing of the request will fail in Segment    • When called, this endpoint may generate the `Source Regulation Created` event in the [audit trail](/tag/Audit-Trail).  Config API omitted fields: - `attributes`, - `userAgent`  Rate limit headers: - X-Regulation-RateLimit-Remaining: Remaining requests in the current period (stringified integer) - X-Regulation-RateLimit-Quota-Reset: ISO 8601 timestamp for when the quota resets (e.g., 2024-12-31T23:59:59.000Z)   

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_source_regulation200_response import CreateSourceRegulation200Response
from segment_public_api.models.create_source_regulation_v1_input import CreateSourceRegulationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    create_source_regulation_v1_input = {"regulationType":"SUPPRESS_ONLY","subjectType":"USER_ID","subjectIds":["test_user_id_1"]} # CreateSourceRegulationV1Input | 

    try:
        # Create Source Regulation
        api_response = api_instance.create_source_regulation(source_id, create_source_regulation_v1_input)
        print("The response of DeletionAndSuppressionApi->create_source_regulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->create_source_regulation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **create_source_regulation_v1_input** | [**CreateSourceRegulationV1Input**](CreateSourceRegulationV1Input.md)|  | 

### Return type

[**CreateSourceRegulation200Response**](CreateSourceRegulation200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Regulation-RateLimit-Remaining - Remaining requests in the current period <br>  * X-Regulation-RateLimit-Quota-Reset - ISO 8601 timestamp for when the quota resets <br>  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: create_workspace_regulation

> CreateWorkspaceRegulation200Response create_workspace_regulation(create_workspace_regulation_v1_input)

Create Workspace Regulation

Creates a Workspace-scoped regulation.    • When called, this endpoint may generate the `Workspace Regulation Created` event in the [audit trail](/tag/Audit-Trail).  Config API omitted fields: - `attributes`, - `userAgent`  Rate limit headers: - X-Regulation-RateLimit-Remaining: Remaining requests in the current period (stringified integer) - X-Regulation-RateLimit-Quota-Reset: ISO 8601 timestamp for when the quota resets (e.g., 2024-12-31T23:59:59.000Z)   

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_workspace_regulation200_response import CreateWorkspaceRegulation200Response
from segment_public_api.models.create_workspace_regulation_v1_input import CreateWorkspaceRegulationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    create_workspace_regulation_v1_input = {"regulationType":"SUPPRESS_ONLY","subjectType":"USER_ID","subjectIds":["test_user_id_1"]} # CreateWorkspaceRegulationV1Input | 

    try:
        # Create Workspace Regulation
        api_response = api_instance.create_workspace_regulation(create_workspace_regulation_v1_input)
        print("The response of DeletionAndSuppressionApi->create_workspace_regulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->create_workspace_regulation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_workspace_regulation_v1_input** | [**CreateWorkspaceRegulationV1Input**](CreateWorkspaceRegulationV1Input.md)|  | 

### Return type

[**CreateWorkspaceRegulation200Response**](CreateWorkspaceRegulation200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Regulation-RateLimit-Remaining - Remaining requests in the current period <br>  * X-Regulation-RateLimit-Quota-Reset - ISO 8601 timestamp for when the quota resets <br>  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_regulation

> DeleteRegulation200Response delete_regulation(regulate_id)

Delete Regulation

Deletes a regulation from the Workspace. The regulation must be in the initialized state to be deleted.    • When called, this endpoint may generate the `Regulation Deleted` event in the [audit trail](/tag/Audit-Trail).         **DEPRECATED**: this endpoint has been deprecated according to the guidelines, and may experience reduced SLA guarantees.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_regulation200_response import DeleteRegulation200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    regulate_id = '1qJkfE1tpwvQcklImGksLN629wn' # str | 

    try:
        # Delete Regulation
        api_response = api_instance.delete_regulation(regulate_id)
        print("The response of DeletionAndSuppressionApi->delete_regulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->delete_regulation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regulate_id** | **str**|  | 

### Return type

[**DeleteRegulation200Response**](DeleteRegulation200Response.md)

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


## Operation: get_regulation

> GetRegulation200Response get_regulation(regulate_id)

Get Regulation

Gets a regulation from the Workspace.        Config API omitted fields: - `parent`       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_regulation200_response import GetRegulation200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    regulate_id = '1qJkfE1tpwvQcklImGksLN629wn' # str | 

    try:
        # Get Regulation
        api_response = api_instance.get_regulation(regulate_id)
        print("The response of DeletionAndSuppressionApi->get_regulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->get_regulation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regulate_id** | **str**|  | 

### Return type

[**GetRegulation200Response**](GetRegulation200Response.md)

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


## Operation: list_regulations_from_source

> ListRegulationsFromSource200Response list_regulations_from_source(source_id, status=status, regulation_types=regulation_types, pagination=pagination)

List Regulations from Source

Lists all Source-scoped regulations.    Please note: List regulations for Source only returns deletion requests from the past 90 days. Deletion requests older than 90 days are not retained and will result in 404 resource not found.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_regulations_from_source200_response import ListRegulationsFromSource200Response
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
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    status = 'status_example' # str | The status on which to filter returned regulations.  This parameter exists in v1. (optional)
    regulation_types = ['regulation_types_example'] # List[str] | The regulation types on which to filter returned regulations.  This parameter exists in v1. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Regulations from Source
        api_response = api_instance.list_regulations_from_source(source_id, status=status, regulation_types=regulation_types, pagination=pagination)
        print("The response of DeletionAndSuppressionApi->list_regulations_from_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->list_regulations_from_source: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **status** | **str**| The status on which to filter returned regulations.  This parameter exists in v1. | [optional] 
 **regulation_types** | [**List[str]**](str.md)| The regulation types on which to filter returned regulations.  This parameter exists in v1. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListRegulationsFromSource200Response**](ListRegulationsFromSource200Response.md)

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


## Operation: list_suppressions

> ListSuppressions200Response list_suppressions(pagination=pagination)

List Suppressions

Lists all suppressions in a given Workspace.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_suppressions200_response import ListSuppressions200Response
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
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Suppressions
        api_response = api_instance.list_suppressions(pagination=pagination)
        print("The response of DeletionAndSuppressionApi->list_suppressions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->list_suppressions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListSuppressions200Response**](ListSuppressions200Response.md)

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


## Operation: list_workspace_regulations

> ListWorkspaceRegulations200Response list_workspace_regulations(status=status, regulation_types=regulation_types, pagination=pagination)

List Workspace Regulations

Lists all Workspace-scoped regulations.    Please note: List Workspace regulations only returns deletion requests from the past 90 days. Deletion requests older than 90 days are not retained and will result in 404 resource not found.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_workspace_regulations200_response import ListWorkspaceRegulations200Response
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
    api_instance = segment_public_api.DeletionAndSuppressionApi(api_client)
    status = 'status_example' # str | The status on which to filter the returned regulations.  This parameter exists in v1. (optional)
    regulation_types = ['regulation_types_example'] # List[str] | The regulation types on which to filter returned regulations.  This parameter exists in v1. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Workspace Regulations
        api_response = api_instance.list_workspace_regulations(status=status, regulation_types=regulation_types, pagination=pagination)
        print("The response of DeletionAndSuppressionApi->list_workspace_regulations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeletionAndSuppressionApi->list_workspace_regulations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| The status on which to filter the returned regulations.  This parameter exists in v1. | [optional] 
 **regulation_types** | [**List[str]**](str.md)| The regulation types on which to filter returned regulations.  This parameter exists in v1. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListWorkspaceRegulations200Response**](ListWorkspaceRegulations200Response.md)

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

