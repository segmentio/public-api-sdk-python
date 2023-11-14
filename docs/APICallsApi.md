# segment_public_api.APICallsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_per_source_api_calls_usage**](APICallsApi.md#get_daily_per_source_api_calls_usage) | **GET** /usage/api-calls/sources/daily | Get Daily Per Source API Calls Usage
[**get_daily_workspace_api_calls_usage**](APICallsApi.md#get_daily_workspace_api_calls_usage) | **GET** /usage/api-calls/daily | Get Daily Workspace API Calls Usage



## Operation: get_daily_per_source_api_calls_usage

> GetDailyPerSourceAPICallsUsage200Response get_daily_per_source_api_calls_usage(period, pagination)

Get Daily Per Source API Calls Usage

Provides daily cumulative per-source API call counts for a usage period.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_daily_per_source_api_calls_usage200_response import GetDailyPerSourceAPICallsUsage200Response
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
    api_instance = segment_public_api.APICallsApi(api_client)
    period = '2021-02-01' # str | The start of the usage month in the ISO-8601 format.  This parameter exists in v1.
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination input for per Source API calls counts.  This parameter exists in v1.

    try:
        # Get Daily Per Source API Calls Usage
        api_response = api_instance.get_daily_per_source_api_calls_usage(period, pagination)
        print("The response of APICallsApi->get_daily_per_source_api_calls_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICallsApi->get_daily_per_source_api_calls_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| The start of the usage month in the ISO-8601 format.  This parameter exists in v1. | 
 **pagination** | [**PaginationInput**](.md)| Pagination input for per Source API calls counts.  This parameter exists in v1. | 

### Return type

[**GetDailyPerSourceAPICallsUsage200Response**](GetDailyPerSourceAPICallsUsage200Response.md)

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


## Operation: get_daily_workspace_api_calls_usage

> GetDailyWorkspaceAPICallsUsage200Response get_daily_workspace_api_calls_usage(period, pagination)

Get Daily Workspace API Calls Usage

Provides daily cumulative API call counts for a usage period.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_daily_workspace_api_calls_usage200_response import GetDailyWorkspaceAPICallsUsage200Response
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
    api_instance = segment_public_api.APICallsApi(api_client)
    period = '2021-02-01' # str | The start of the usage month in the ISO-8601 format.  This parameter exists in v1.
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination input for Workspace API call counts.  This parameter exists in v1.

    try:
        # Get Daily Workspace API Calls Usage
        api_response = api_instance.get_daily_workspace_api_calls_usage(period, pagination)
        print("The response of APICallsApi->get_daily_workspace_api_calls_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APICallsApi->get_daily_workspace_api_calls_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| The start of the usage month in the ISO-8601 format.  This parameter exists in v1. | 
 **pagination** | [**PaginationInput**](.md)| Pagination input for Workspace API call counts.  This parameter exists in v1. | 

### Return type

[**GetDailyWorkspaceAPICallsUsage200Response**](GetDailyWorkspaceAPICallsUsage200Response.md)

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

