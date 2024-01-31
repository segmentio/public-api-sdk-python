# segment_public_api.LabelsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label**](LabelsApi.md#create_label) | **POST** /labels | Create Label
[**delete_label**](LabelsApi.md#delete_label) | **DELETE** /labels/{key}/{value} | Delete Label
[**list_labels**](LabelsApi.md#list_labels) | **GET** /labels | List Labels



## Operation: create_label

> CreateLabel200Response create_label(create_label_v1_input)

Create Label

Creates a new label.    • When called, this endpoint may generate the `Label Created` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_label200_response import CreateLabel200Response
from segment_public_api.models.create_label_v1_input import CreateLabelV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.LabelsApi(api_client)
    create_label_v1_input = {"label":{"key":"environment","value":"yolo","description":"an environment for courageous devs"}} # CreateLabelV1Input | 

    try:
        # Create Label
        api_response = api_instance.create_label(create_label_v1_input)
        print("The response of LabelsApi->create_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->create_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_label_v1_input** | [**CreateLabelV1Input**](CreateLabelV1Input.md)|  | 

### Return type

[**CreateLabel200Response**](CreateLabel200Response.md)

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


## Operation: delete_label

> DeleteLabel200Response delete_label(key, value)

Delete Label

Deletes a label.    • When called, this endpoint may generate the `Label Deleted` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_label200_response import DeleteLabel200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.LabelsApi(api_client)
    key = 'environment' # str | 
    value = 'yolo' # str | 

    try:
        # Delete Label
        api_response = api_instance.delete_label(key, value)
        print("The response of LabelsApi->delete_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->delete_label: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **value** | **str**|  | 

### Return type

[**DeleteLabel200Response**](DeleteLabel200Response.md)

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


## Operation: list_labels

> ListLabels200Response list_labels()

List Labels

Returns a list of all available labels.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_labels200_response import ListLabels200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.LabelsApi(api_client)

    try:
        # List Labels
        api_response = api_instance.list_labels()
        print("The response of LabelsApi->list_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->list_labels: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListLabels200Response**](ListLabels200Response.md)

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

