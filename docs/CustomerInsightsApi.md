# segment_public_api.CustomerInsightsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_download**](CustomerInsightsApi.md#create_download) | **POST** /customer-insights/download | Create Download



## Operation: create_download

> CreateDownload200Response create_download(create_download_alpha_input)

Create Download

Create Customer Insights Presigned URLs   The rate limit for this endpoint is 1 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_download200_response import CreateDownload200Response
from segment_public_api.models.create_download_alpha_input import CreateDownloadAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CustomerInsightsApi(api_client)
    create_download_alpha_input = {"collectionId":"2wmpXTGB69A8BwGJ4hD5XvQ03aD","workspaceId":"9y433Y71snvrWKfchyBbu9","startTime":"2006-01-02T15:04:05.000Z"} # CreateDownloadAlphaInput | 

    try:
        # Create Download
        api_response = api_instance.create_download(create_download_alpha_input)
        print("The response of CustomerInsightsApi->create_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerInsightsApi->create_download: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_download_alpha_input** | [**CreateDownloadAlphaInput**](CreateDownloadAlphaInput.md)|  | 

### Return type

[**CreateDownload200Response**](CreateDownload200Response.md)

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

