# segment_public_api.FunctionsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_function**](FunctionsApi.md#create_function) | **POST** /functions | Create Function
[**create_function_deployment**](FunctionsApi.md#create_function_deployment) | **POST** /functions/{functionId}/deploy | Create Function Deployment
[**create_insert_function_instance**](FunctionsApi.md#create_insert_function_instance) | **POST** /insert-function-instances | Create Insert Function Instance
[**create_transformation_function_instance**](FunctionsApi.md#create_transformation_function_instance) | **POST** /transformation-function-instances | Create Transformation Function Instance
[**delete_function**](FunctionsApi.md#delete_function) | **DELETE** /functions/{functionId} | Delete Function
[**delete_insert_function_instance**](FunctionsApi.md#delete_insert_function_instance) | **DELETE** /insert-function-instances/{instanceId} | Delete Insert Function Instance
[**get_function**](FunctionsApi.md#get_function) | **GET** /functions/{functionId} | Get Function
[**get_function_version**](FunctionsApi.md#get_function_version) | **GET** /functions/{functionId}/versions/{versionId} | Get Function Version
[**get_insert_function_instance**](FunctionsApi.md#get_insert_function_instance) | **GET** /insert-function-instances/{instanceId} | Get Insert Function Instance
[**list_function_versions**](FunctionsApi.md#list_function_versions) | **GET** /functions/{functionId}/versions | List Function Versions
[**list_functions**](FunctionsApi.md#list_functions) | **GET** /functions | List Functions
[**list_insert_function_instances**](FunctionsApi.md#list_insert_function_instances) | **GET** /insert-function-instances | List Insert Function Instances
[**restore_function_version**](FunctionsApi.md#restore_function_version) | **POST** /functions/{functionId}/versions | Restore Function Version
[**update_function**](FunctionsApi.md#update_function) | **PATCH** /functions/{functionId} | Update Function
[**update_insert_function_instance**](FunctionsApi.md#update_insert_function_instance) | **PATCH** /insert-function-instances/{instanceId} | Update Insert Function Instance



## Operation: create_function

> CreateFunction200Response create_function(create_function_v1_input)

Create Function

Creates a Function.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_function200_response import CreateFunction200Response
from segment_public_api.models.create_function_v1_input import CreateFunctionV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    create_function_v1_input = {"code":"// Learn more about source functions API at https://segment.com/docs/connections/sources/source-functions","settings":[{"name":"apiKey","label":"api key","type":"STRING","description":"api key","required":false,"sensitive":false},{"name":"mySecret","label":"my secret key","type":"STRING","description":"secret key","required":false,"sensitive":true}],"displayName":"PAPI Source Function","resourceType":"SOURCE","logoUrl":"https://placekitten.com/200/139","description":"My source function"} # CreateFunctionV1Input | 

    try:
        # Create Function
        api_response = api_instance.create_function(create_function_v1_input)
        print("The response of FunctionsApi->create_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_function_v1_input** | [**CreateFunctionV1Input**](CreateFunctionV1Input.md)|  | 

### Return type

[**CreateFunction200Response**](CreateFunction200Response.md)

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


## Operation: create_function_deployment

> CreateFunctionDeployment200Response create_function_deployment(function_id)

Create Function Deployment

Deploys a Function. Only applicable to Source Function instances.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_function_deployment200_response import CreateFunctionDeployment200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfn_rh5BDZp6QDHvXFCkibm1pR' # str | 

    try:
        # Create Function Deployment
        api_response = api_instance.create_function_deployment(function_id)
        print("The response of FunctionsApi->create_function_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_function_deployment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 

### Return type

[**CreateFunctionDeployment200Response**](CreateFunctionDeployment200Response.md)

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


## Operation: create_insert_function_instance

> CreateInsertFunctionInstance200Response create_insert_function_instance(create_insert_function_instance_alpha_input)

Create Insert Function Instance

Creates an insert Function instance connected to the given Destination.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_insert_function_instance200_response import CreateInsertFunctionInstance200Response
from segment_public_api.models.create_insert_function_instance_alpha_input import CreateInsertFunctionInstanceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    create_insert_function_instance_alpha_input = {"functionId":"76365637324e715a67535831","integrationId":"fP7qoQw2HTWt9WdMr718gn","name":"Example insert function instance","settings":{"apiKey":"XYZ"}} # CreateInsertFunctionInstanceAlphaInput | 

    try:
        # Create Insert Function Instance
        api_response = api_instance.create_insert_function_instance(create_insert_function_instance_alpha_input)
        print("The response of FunctionsApi->create_insert_function_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_insert_function_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_insert_function_instance_alpha_input** | [**CreateInsertFunctionInstanceAlphaInput**](CreateInsertFunctionInstanceAlphaInput.md)|  | 

### Return type

[**CreateInsertFunctionInstance200Response**](CreateInsertFunctionInstance200Response.md)

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


## Operation: create_transformation_function_instance

> CreateTransformationFunctionInstance200Response create_transformation_function_instance(create_transformation_function_instance_alpha_input)

Create Transformation Function Instance

Creates a Transformation Function instance connected to the given Integration.  This endpoint is specifically designed for Transformations and includes integration_type as a mandatory field.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_transformation_function_instance200_response import CreateTransformationFunctionInstance200Response
from segment_public_api.models.create_transformation_function_instance_alpha_input import CreateTransformationFunctionInstanceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    create_transformation_function_instance_alpha_input = {"functionId":"76365637324e715a67535831","integrationId":"qtiZHLLqqsHmpvLXNtP5du","integrationType":"DESTINATION","name":"Example transformation function instance","settings":{"apiKey":"XYZ"}} # CreateTransformationFunctionInstanceAlphaInput | 

    try:
        # Create Transformation Function Instance
        api_response = api_instance.create_transformation_function_instance(create_transformation_function_instance_alpha_input)
        print("The response of FunctionsApi->create_transformation_function_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->create_transformation_function_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transformation_function_instance_alpha_input** | [**CreateTransformationFunctionInstanceAlphaInput**](CreateTransformationFunctionInstanceAlphaInput.md)|  | 

### Return type

[**CreateTransformationFunctionInstance200Response**](CreateTransformationFunctionInstance200Response.md)

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


## Operation: delete_function

> DeleteFunction200Response delete_function(function_id)

Delete Function

Deletes a Function.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_function200_response import DeleteFunction200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfnc_wXzcDGFR3KmjLDrtSawNHf' # str | 

    try:
        # Delete Function
        api_response = api_instance.delete_function(function_id)
        print("The response of FunctionsApi->delete_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->delete_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 

### Return type

[**DeleteFunction200Response**](DeleteFunction200Response.md)

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


## Operation: delete_insert_function_instance

> DeleteInsertFunctionInstance200Response delete_insert_function_instance(instance_id)

Delete Insert Function Instance

Deletes an insert Function instance.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_insert_function_instance200_response import DeleteInsertFunctionInstance200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    instance_id = '65c2bdbdde6f2d8297f943da' # str | 

    try:
        # Delete Insert Function Instance
        api_response = api_instance.delete_insert_function_instance(instance_id)
        print("The response of FunctionsApi->delete_insert_function_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->delete_insert_function_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 

### Return type

[**DeleteInsertFunctionInstance200Response**](DeleteInsertFunctionInstance200Response.md)

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


## Operation: get_function

> GetFunction200Response get_function(function_id)

Get Function

Gets a Function.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_function200_response import GetFunction200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfnc_wXzcDGFR3KmjLDrtSawNHf' # str | 

    try:
        # Get Function
        api_response = api_instance.get_function(function_id)
        print("The response of FunctionsApi->get_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 

### Return type

[**GetFunction200Response**](GetFunction200Response.md)

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


## Operation: get_function_version

> GetFunctionVersion200Response get_function_version(function_id, version_id)

Get Function Version

Gets a Function version.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_function_version200_response import GetFunctionVersion200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfnc_wXzcDGFR3KmjLDrtSawNHf' # str | 
    version_id = '2Ma03fahSqLoEzQfV5o2aSfVEHs' # str | 

    try:
        # Get Function Version
        api_response = api_instance.get_function_version(function_id, version_id)
        print("The response of FunctionsApi->get_function_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_function_version: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**GetFunctionVersion200Response**](GetFunctionVersion200Response.md)

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


## Operation: get_insert_function_instance

> GetInsertFunctionInstance200Response get_insert_function_instance(instance_id)

Get Insert Function Instance

Gets an insert Function instance.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_insert_function_instance200_response import GetInsertFunctionInstance200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    instance_id = '65c2bdbcde6f2d8297f943d7' # str | 

    try:
        # Get Insert Function Instance
        api_response = api_instance.get_insert_function_instance(instance_id)
        print("The response of FunctionsApi->get_insert_function_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->get_insert_function_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 

### Return type

[**GetInsertFunctionInstance200Response**](GetInsertFunctionInstance200Response.md)

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


## Operation: list_function_versions

> ListFunctionVersions200Response list_function_versions(function_id, pagination=pagination)

List Function Versions

Lists versions for a Function in a Workspace.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_function_versions200_response import ListFunctionVersions200Response
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
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfnc_wXzcDGFR3KmjLDrtSawNHf' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination parameters.  This parameter exists in alpha. (optional)

    try:
        # List Function Versions
        api_response = api_instance.list_function_versions(function_id, pagination=pagination)
        print("The response of FunctionsApi->list_function_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->list_function_versions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination parameters.  This parameter exists in alpha. | [optional] 

### Return type

[**ListFunctionVersions200Response**](ListFunctionVersions200Response.md)

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


## Operation: list_functions

> ListFunctions200Response list_functions(resource_type, pagination=pagination)

List Functions

Lists all Functions in a Workspace.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_functions200_response import ListFunctions200Response
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
    api_instance = segment_public_api.FunctionsApi(api_client)
    resource_type = 'SOURCE' # str | The Function type.  Config API note: equal to `type`.  This parameter exists in v1.
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Functions
        api_response = api_instance.list_functions(resource_type, pagination=pagination)
        print("The response of FunctionsApi->list_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->list_functions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| The Function type.  Config API note: equal to &#x60;type&#x60;.  This parameter exists in v1. | 
 **pagination** | [**PaginationInput**](.md)| Pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListFunctions200Response**](ListFunctions200Response.md)

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


## Operation: list_insert_function_instances

> ListInsertFunctionInstances200Response list_insert_function_instances(function_id, pagination=pagination)

List Insert Function Instances

Lists all insert Function instances connected to the given insert Function.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_insert_function_instances200_response import ListInsertFunctionInstances200Response
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
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = '76365637324e715a67535831' # str | The insert Function class id to lookup.  This parameter exists in alpha.
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination parameters.  This parameter exists in alpha. (optional)

    try:
        # List Insert Function Instances
        api_response = api_instance.list_insert_function_instances(function_id, pagination=pagination)
        print("The response of FunctionsApi->list_insert_function_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->list_insert_function_instances: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**| The insert Function class id to lookup.  This parameter exists in alpha. | 
 **pagination** | [**PaginationInput**](.md)| Pagination parameters.  This parameter exists in alpha. | [optional] 

### Return type

[**ListInsertFunctionInstances200Response**](ListInsertFunctionInstances200Response.md)

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


## Operation: restore_function_version

> RestoreFunctionVersion200Response restore_function_version(function_id, restore_function_version_alpha_input)

Restore Function Version

Restore an old Function version as the latest version.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.restore_function_version200_response import RestoreFunctionVersion200Response
from segment_public_api.models.restore_function_version_alpha_input import RestoreFunctionVersionAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfnc_wXzcDGFR3KmjLDrtSawNHf' # str | 
    restore_function_version_alpha_input = {"versionId":"2Ma03fahSqLoEzQfV5o2aSfVEHs"} # RestoreFunctionVersionAlphaInput | 

    try:
        # Restore Function Version
        api_response = api_instance.restore_function_version(function_id, restore_function_version_alpha_input)
        print("The response of FunctionsApi->restore_function_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->restore_function_version: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 
 **restore_function_version_alpha_input** | [**RestoreFunctionVersionAlphaInput**](RestoreFunctionVersionAlphaInput.md)|  | 

### Return type

[**RestoreFunctionVersion200Response**](RestoreFunctionVersion200Response.md)

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


## Operation: update_function

> UpdateFunction200Response update_function(function_id, update_function_v1_input)

Update Function

Updates a Function.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.  Config API omitted fields: - `updateMask` 

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_function200_response import UpdateFunction200Response
from segment_public_api.models.update_function_v1_input import UpdateFunctionV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    function_id = 'sfnc_wXzcDGFR3KmjLDrtSawNHf' # str | 
    update_function_v1_input = {"code":"// Learn more about source functions API at https://segment.com/docs/connections/sources/source-functions","logoUrl":"https://placekitten.com/200/139"} # UpdateFunctionV1Input | 

    try:
        # Update Function
        api_response = api_instance.update_function(function_id, update_function_v1_input)
        print("The response of FunctionsApi->update_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->update_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_id** | **str**|  | 
 **update_function_v1_input** | [**UpdateFunctionV1Input**](UpdateFunctionV1Input.md)|  | 

### Return type

[**UpdateFunction200Response**](UpdateFunction200Response.md)

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


## Operation: update_insert_function_instance

> UpdateInsertFunctionInstance200Response update_insert_function_instance(instance_id, update_insert_function_instance_alpha_input)

Update Insert Function Instance

Updates an insert Function instance connected to the given Destination.    • In order to successfully call this endpoint, the specified Workspace needs to have the Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_insert_function_instance200_response import UpdateInsertFunctionInstance200Response
from segment_public_api.models.update_insert_function_instance_alpha_input import UpdateInsertFunctionInstanceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.FunctionsApi(api_client)
    instance_id = '65c2bdbcde6f2d8297f943d8' # str | 
    update_insert_function_instance_alpha_input = {"enabled":false,"settings":{"apiKey":"XYZ-new"}} # UpdateInsertFunctionInstanceAlphaInput | 

    try:
        # Update Insert Function Instance
        api_response = api_instance.update_insert_function_instance(instance_id, update_insert_function_instance_alpha_input)
        print("The response of FunctionsApi->update_insert_function_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FunctionsApi->update_insert_function_instance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **update_insert_function_instance_alpha_input** | [**UpdateInsertFunctionInstanceAlphaInput**](UpdateInsertFunctionInstanceAlphaInput.md)|  | 

### Return type

[**UpdateInsertFunctionInstance200Response**](UpdateInsertFunctionInstance200Response.md)

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

