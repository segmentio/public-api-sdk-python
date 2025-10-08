# segment_public_api.LivePluginsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_live_plugin**](LivePluginsApi.md#create_live_plugin) | **POST** /sources/{sourceId}/live-plugins/create | Create Live Plugin
[**delete_live_plugin_code**](LivePluginsApi.md#delete_live_plugin_code) | **DELETE** /sources/{sourceId}/live-plugins/delete-code | Delete Live Plugin Code
[**get_latest_from_live_plugins**](LivePluginsApi.md#get_latest_from_live_plugins) | **GET** /sources/{sourceId}/live-plugins/latest | Get Latest from Live Plugins



## Operation: create_live_plugin

> CreateLivePlugin200Response create_live_plugin(source_id, create_live_plugin_alpha_input)

Create Live Plugin

Creates or updates a Live Plugin for your Source with given code.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Live Plugins feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_live_plugin200_response import CreateLivePlugin200Response
from segment_public_api.models.create_live_plugin_alpha_input import CreateLivePluginAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.LivePluginsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 
    create_live_plugin_alpha_input = {"code":"console.log('Hello, World!');"} # CreateLivePluginAlphaInput | 

    try:
        # Create Live Plugin
        api_response = api_instance.create_live_plugin(source_id, create_live_plugin_alpha_input)
        print("The response of LivePluginsApi->create_live_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LivePluginsApi->create_live_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 
 **create_live_plugin_alpha_input** | [**CreateLivePluginAlphaInput**](CreateLivePluginAlphaInput.md)|  | 

### Return type

[**CreateLivePlugin200Response**](CreateLivePlugin200Response.md)

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


## Operation: delete_live_plugin_code

> DeleteLivePluginCode200Response delete_live_plugin_code(source_id)

Delete Live Plugin Code

Delete the Live Plugin code for a Source. This will not disable Live Plugins for the Source, but will remove any existing code.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Live Plugins feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_live_plugin_code200_response import DeleteLivePluginCode200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.LivePluginsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Delete Live Plugin Code
        api_response = api_instance.delete_live_plugin_code(source_id)
        print("The response of LivePluginsApi->delete_live_plugin_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LivePluginsApi->delete_live_plugin_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**DeleteLivePluginCode200Response**](DeleteLivePluginCode200Response.md)

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


## Operation: get_latest_from_live_plugins

> GetLatestFromLivePlugins200Response get_latest_from_live_plugins(source_id)

Get Latest from Live Plugins

Get the latest Live Plugins for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Live Plugins feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_latest_from_live_plugins200_response import GetLatestFromLivePlugins200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.LivePluginsApi(api_client)
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | 

    try:
        # Get Latest from Live Plugins
        api_response = api_instance.get_latest_from_live_plugins(source_id)
        print("The response of LivePluginsApi->get_latest_from_live_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LivePluginsApi->get_latest_from_live_plugins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**GetLatestFromLivePlugins200Response**](GetLatestFromLivePlugins200Response.md)

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

