# segment_public_api.MonthlyTrackedUsersApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_daily_per_source_mtu_usage**](MonthlyTrackedUsersApi.md#get_daily_per_source_mtu_usage) | **GET** /usage/mtu/sources/daily | Get Daily Per Source MTU Usage
[**get_daily_workspace_mtu_usage**](MonthlyTrackedUsersApi.md#get_daily_workspace_mtu_usage) | **GET** /usage/mtu/daily | Get Daily Workspace MTU Usage



## Operation: get_daily_per_source_mtu_usage

> GetDailyPerSourceMTUUsage200Response get_daily_per_source_mtu_usage(period, pagination=pagination)

Get Daily Per Source MTU Usage

Provides daily cumulative per-source MTU counts for a usage period.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_daily_per_source_mtu_usage200_response import GetDailyPerSourceMTUUsage200Response
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
    api_instance = segment_public_api.MonthlyTrackedUsersApi(api_client)
    period = '2021-02-01' # str | The start of the usage month, in the ISO-8601 format.  This parameter exists in v1.
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination input for per Source MTU counts.  This parameter exists in v1. (optional)

    try:
        # Get Daily Per Source MTU Usage
        api_response = api_instance.get_daily_per_source_mtu_usage(period, pagination=pagination)
        print("The response of MonthlyTrackedUsersApi->get_daily_per_source_mtu_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonthlyTrackedUsersApi->get_daily_per_source_mtu_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| The start of the usage month, in the ISO-8601 format.  This parameter exists in v1. | 
 **pagination** | [**PaginationInput**](.md)| Pagination input for per Source MTU counts.  This parameter exists in v1. | [optional] 

### Return type

[**GetDailyPerSourceMTUUsage200Response**](GetDailyPerSourceMTUUsage200Response.md)

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


## Operation: get_daily_workspace_mtu_usage

> GetDailyWorkspaceMTUUsage200Response get_daily_workspace_mtu_usage(period, pagination=pagination)

Get Daily Workspace MTU Usage

Provides daily cumulative MTU counts for a usage period.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_daily_workspace_mtu_usage200_response import GetDailyWorkspaceMTUUsage200Response
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
    api_instance = segment_public_api.MonthlyTrackedUsersApi(api_client)
    period = '2021-02-01' # str | The start of the usage month, in the ISO-8601 format.  This parameter exists in v1.
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination input for Workspace MTU counts.  This parameter exists in v1. (optional)

    try:
        # Get Daily Workspace MTU Usage
        api_response = api_instance.get_daily_workspace_mtu_usage(period, pagination=pagination)
        print("The response of MonthlyTrackedUsersApi->get_daily_workspace_mtu_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonthlyTrackedUsersApi->get_daily_workspace_mtu_usage: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period** | **str**| The start of the usage month, in the ISO-8601 format.  This parameter exists in v1. | 
 **pagination** | [**PaginationInput**](.md)| Pagination input for Workspace MTU counts.  This parameter exists in v1. | [optional] 

### Return type

[**GetDailyWorkspaceMTUUsage200Response**](GetDailyWorkspaceMTUUsage200Response.md)

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

