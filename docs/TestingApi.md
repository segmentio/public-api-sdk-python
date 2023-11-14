# segment_public_api.TestingApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo**](TestingApi.md#echo) | **GET** /echo | Echo



## Operation: echo

> Echo200Response echo(message, delay=delay, trigger_error=trigger_error, trigger_multiple_errors=trigger_multiple_errors, trigger_unexpected_error=trigger_unexpected_error, status_code=status_code)

Echo

Public Echo endpoint.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.echo200_response import Echo200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TestingApi(api_client)
    message = 'Hello, World!' # str | Sets the response `message` field. The response contains this field's entry.  This parameter exists in alpha.
    delay = 3.4 # float | The desired response delay, in milliseconds.  This parameter exists in alpha. (optional)
    trigger_error = True # bool | If `true`, returns an HTTP `4xx` error that contains the string in `message`.  This parameter exists in alpha. (optional)
    trigger_multiple_errors = True # bool | If `true`, returns an HTTP `4xx` error that contains the value of the `message` field in the error message array.  This has no effect if the request sets `triggerError`.  This parameter exists in alpha. (optional)
    trigger_unexpected_error = True # bool | If `true`, triggers a `500` error.  This has no effect if the request sets either `triggerError` or `triggerMultipleErrors`.  This parameter exists in alpha. (optional)
    status_code = 3.4 # float | Sets the HTTP status code to return.  This parameter exists in alpha. (optional)

    try:
        # Echo
        api_response = api_instance.echo(message, delay=delay, trigger_error=trigger_error, trigger_multiple_errors=trigger_multiple_errors, trigger_unexpected_error=trigger_unexpected_error, status_code=status_code)
        print("The response of TestingApi->echo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestingApi->echo: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| Sets the response &#x60;message&#x60; field. The response contains this field&#39;s entry.  This parameter exists in alpha. | 
 **delay** | **float**| The desired response delay, in milliseconds.  This parameter exists in alpha. | [optional] 
 **trigger_error** | **bool**| If &#x60;true&#x60;, returns an HTTP &#x60;4xx&#x60; error that contains the string in &#x60;message&#x60;.  This parameter exists in alpha. | [optional] 
 **trigger_multiple_errors** | **bool**| If &#x60;true&#x60;, returns an HTTP &#x60;4xx&#x60; error that contains the value of the &#x60;message&#x60; field in the error message array.  This has no effect if the request sets &#x60;triggerError&#x60;.  This parameter exists in alpha. | [optional] 
 **trigger_unexpected_error** | **bool**| If &#x60;true&#x60;, triggers a &#x60;500&#x60; error.  This has no effect if the request sets either &#x60;triggerError&#x60; or &#x60;triggerMultipleErrors&#x60;.  This parameter exists in alpha. | [optional] 
 **status_code** | **float**| Sets the HTTP status code to return.  This parameter exists in alpha. | [optional] 

### Return type

[**Echo200Response**](Echo200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

