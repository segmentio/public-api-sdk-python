# segment_public_api.ReverseETLApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reverse_etl_model**](ReverseETLApi.md#create_reverse_etl_model) | **POST** /reverse-etl-models | Create Reverse Etl Model
[**delete_reverse_etl_model**](ReverseETLApi.md#delete_reverse_etl_model) | **DELETE** /reverse-etl-models/{modelId} | Delete Reverse Etl Model
[**get_reverse_etl_model**](ReverseETLApi.md#get_reverse_etl_model) | **GET** /reverse-etl-models/{modelId} | Get Reverse Etl Model
[**list_reverse_etl_models**](ReverseETLApi.md#list_reverse_etl_models) | **GET** /reverse-etl-models | List Reverse Etl Models
[**update_reverse_etl_model**](ReverseETLApi.md#update_reverse_etl_model) | **PATCH** /reverse-etl-models/{modelId} | Update Reverse Etl Model



## Operation: create_reverse_etl_model

> CreateReverseEtlModel200Response create_reverse_etl_model(create_reverse_etl_model_input)

Create Reverse Etl Model

Creates a new Reverse ETL Model.          • When called, this endpoint may generate the `Model Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_reverse_etl_model200_response import CreateReverseEtlModel200Response
from segment_public_api.models.create_reverse_etl_model_input import CreateReverseEtlModelInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ReverseETLApi(api_client)
    create_reverse_etl_model_input = {"sourceId":"qQEHquLrjRDN9j1ByrChyn","name":"Model 1","description":"This model is very useful.","enabled":true,"query":"SELECT 'user_1' AS id","queryIdentifierColumn":"id","scheduleStrategy":"MANUAL","scheduleConfig":{}} # CreateReverseEtlModelInput | 

    try:
        # Create Reverse Etl Model
        api_response = api_instance.create_reverse_etl_model(create_reverse_etl_model_input)
        print("The response of ReverseETLApi->create_reverse_etl_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->create_reverse_etl_model: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reverse_etl_model_input** | [**CreateReverseEtlModelInput**](CreateReverseEtlModelInput.md)|  | 

### Return type

[**CreateReverseEtlModel200Response**](CreateReverseEtlModel200Response.md)

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


## Operation: delete_reverse_etl_model

> DeleteReverseEtlModel200Response delete_reverse_etl_model(model_id)

Delete Reverse Etl Model

Deletes an existing Model.          • When called, this endpoint may generate the `Model Deleted` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_reverse_etl_model200_response import DeleteReverseEtlModel200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ReverseETLApi(api_client)
    model_id = 'aow61ZsjXFRsUqB5wWmZES' # str | 

    try:
        # Delete Reverse Etl Model
        api_response = api_instance.delete_reverse_etl_model(model_id)
        print("The response of ReverseETLApi->delete_reverse_etl_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->delete_reverse_etl_model: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 

### Return type

[**DeleteReverseEtlModel200Response**](DeleteReverseEtlModel200Response.md)

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


## Operation: get_reverse_etl_model

> GetReverseEtlModel200Response get_reverse_etl_model(model_id)

Get Reverse Etl Model

Returns a Reverse ETL Model by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_reverse_etl_model200_response import GetReverseEtlModel200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ReverseETLApi(api_client)
    model_id = 'MaAeg9yDd1UZTBeEYDiVw' # str | 

    try:
        # Get Reverse Etl Model
        api_response = api_instance.get_reverse_etl_model(model_id)
        print("The response of ReverseETLApi->get_reverse_etl_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->get_reverse_etl_model: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 

### Return type

[**GetReverseEtlModel200Response**](GetReverseEtlModel200Response.md)

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


## Operation: list_reverse_etl_models

> ListReverseEtlModels200Response list_reverse_etl_models(pagination)

List Reverse Etl Models

Returns a list of Reverse ETL Models.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_reverse_etl_models200_response import ListReverseEtlModels200Response
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
    api_instance = segment_public_api.ReverseETLApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in alpha.

    try:
        # List Reverse Etl Models
        api_response = api_instance.list_reverse_etl_models(pagination)
        print("The response of ReverseETLApi->list_reverse_etl_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->list_reverse_etl_models: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in alpha. | 

### Return type

[**ListReverseEtlModels200Response**](ListReverseEtlModels200Response.md)

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


## Operation: update_reverse_etl_model

> UpdateReverseEtlModel200Response update_reverse_etl_model(model_id, update_reverse_etl_model_input)

Update Reverse Etl Model

Updates an existing Reverse ETL Model.          • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Model Settings Saved * Model State Change Toggled       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_reverse_etl_model200_response import UpdateReverseEtlModel200Response
from segment_public_api.models.update_reverse_etl_model_input import UpdateReverseEtlModelInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ReverseETLApi(api_client)
    model_id = '37YCmBXayzqG4sit63P5pH' # str | 
    update_reverse_etl_model_input = {"name":"My Updated Model"} # UpdateReverseEtlModelInput | 

    try:
        # Update Reverse Etl Model
        api_response = api_instance.update_reverse_etl_model(model_id, update_reverse_etl_model_input)
        print("The response of ReverseETLApi->update_reverse_etl_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->update_reverse_etl_model: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **update_reverse_etl_model_input** | [**UpdateReverseEtlModelInput**](UpdateReverseEtlModelInput.md)|  | 

### Return type

[**UpdateReverseEtlModel200Response**](UpdateReverseEtlModel200Response.md)

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

