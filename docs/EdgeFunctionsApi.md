# segment_public_api.EdgeFunctionsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_edge_function**](EdgeFunctionsApi.md#create_edge_function) | **POST** /sources/{sourceId}/edge-functions/create | Create Edge Function
[**delete_edge_function_code**](EdgeFunctionsApi.md#delete_edge_function_code) | **DELETE** /sources/{sourceId}/edge-functions/delete-code | Delete Edge Function Code
[**disable_edge_functions**](EdgeFunctionsApi.md#disable_edge_functions) | **PATCH** /sources/{sourceId}/edge-functions/disable | Disable Edge Functions
[**generate_upload_url_for_edge_functions**](EdgeFunctionsApi.md#generate_upload_url_for_edge_functions) | **POST** /sources/{sourceId}/edge-functions/upload-url | Generate Upload URL for Edge Functions
[**get_latest_from_edge_functions**](EdgeFunctionsApi.md#get_latest_from_edge_functions) | **GET** /sources/{sourceId}/edge-functions/latest | Get Latest from Edge Functions



## Operation: create_edge_function

> CreateEdgeFunction200Response create_edge_function(source_id, create_edge_function_alpha_input)

Create Edge Function

Creates or updates an Edge Function for your Source with given code.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_edge_function200_response import CreateEdgeFunction200Response
from segment_public_api.models.create_edge_function_alpha_input import CreateEdgeFunctionAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.EdgeFunctionsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    create_edge_function_alpha_input = {"code":"console.log('Hello, World!');"} # CreateEdgeFunctionAlphaInput | 

    try:
        # Create Edge Function
        api_response = api_instance.create_edge_function(source_id, create_edge_function_alpha_input)
        print("The response of EdgeFunctionsApi->create_edge_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->create_edge_function: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **create_edge_function_alpha_input** | [**CreateEdgeFunctionAlphaInput**](CreateEdgeFunctionAlphaInput.md)|  | 

### Return type

[**CreateEdgeFunction200Response**](CreateEdgeFunction200Response.md)

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


## Operation: delete_edge_function_code

> DeleteEdgeFunctionCode200Response delete_edge_function_code(source_id)

Delete Edge Function Code

Delete the Edge Function code for a Source. This will not disable Edge Functions for the Source, but will remove any existing code.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_edge_function_code200_response import DeleteEdgeFunctionCode200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.EdgeFunctionsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Delete Edge Function Code
        api_response = api_instance.delete_edge_function_code(source_id)
        print("The response of EdgeFunctionsApi->delete_edge_function_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->delete_edge_function_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**DeleteEdgeFunctionCode200Response**](DeleteEdgeFunctionCode200Response.md)

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


## Operation: disable_edge_functions

> DisableEdgeFunctions200Response disable_edge_functions(source_id)

Disable Edge Functions

Disable Edge Functions for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.disable_edge_functions200_response import DisableEdgeFunctions200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.EdgeFunctionsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Disable Edge Functions
        api_response = api_instance.disable_edge_functions(source_id)
        print("The response of EdgeFunctionsApi->disable_edge_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->disable_edge_functions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**DisableEdgeFunctions200Response**](DisableEdgeFunctions200Response.md)

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


## Operation: generate_upload_url_for_edge_functions

> GenerateUploadURLForEdgeFunctions200Response generate_upload_url_for_edge_functions(source_id)

Generate Upload URL for Edge Functions

Generate a temporary upload URL that can be used to upload an Edge Functions bundle.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.generate_upload_url_for_edge_functions200_response import GenerateUploadURLForEdgeFunctions200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.EdgeFunctionsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Generate Upload URL for Edge Functions
        api_response = api_instance.generate_upload_url_for_edge_functions(source_id)
        print("The response of EdgeFunctionsApi->generate_upload_url_for_edge_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->generate_upload_url_for_edge_functions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**GenerateUploadURLForEdgeFunctions200Response**](GenerateUploadURLForEdgeFunctions200Response.md)

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


## Operation: get_latest_from_edge_functions

> GetLatestFromEdgeFunctions200Response get_latest_from_edge_functions(source_id)

Get Latest from Edge Functions

Get the latest Edge Functions for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_latest_from_edge_functions200_response import GetLatestFromEdgeFunctions200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.EdgeFunctionsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Get Latest from Edge Functions
        api_response = api_instance.get_latest_from_edge_functions(source_id)
        print("The response of EdgeFunctionsApi->get_latest_from_edge_functions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->get_latest_from_edge_functions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**GetLatestFromEdgeFunctions200Response**](GetLatestFromEdgeFunctions200Response.md)

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

