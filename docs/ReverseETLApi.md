# segment_public_api.ReverseETLApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_reverse_etl_sync_for_model**](ReverseETLApi.md#cancel_reverse_etl_sync_for_model) | **POST** /reverse-etl-models/{modelId}/syncs/{syncId}/cancel | Cancel Reverse ETL Sync for Model
[**create_reverse_etl_manual_sync**](ReverseETLApi.md#create_reverse_etl_manual_sync) | **POST** /reverse-etl-syncs | Create Reverse ETL Manual Sync
[**create_reverse_etl_model**](ReverseETLApi.md#create_reverse_etl_model) | **POST** /reverse-etl-models | Create Reverse Etl Model
[**delete_reverse_etl_model**](ReverseETLApi.md#delete_reverse_etl_model) | **DELETE** /reverse-etl-models/{modelId} | Delete Reverse Etl Model
[**get_reverse_etl_model**](ReverseETLApi.md#get_reverse_etl_model) | **GET** /reverse-etl-models/{modelId} | Get Reverse Etl Model
[**get_reverse_etl_sync_status**](ReverseETLApi.md#get_reverse_etl_sync_status) | **GET** /reverse-etl-models/{modelId}/syncs/{syncId} | Get Reverse ETL Sync Status
[**list_reverse_etl_models**](ReverseETLApi.md#list_reverse_etl_models) | **GET** /reverse-etl-models | List Reverse Etl Models
[**list_reverse_etl_sync_statuses_from_model_and_subscription_id**](ReverseETLApi.md#list_reverse_etl_sync_statuses_from_model_and_subscription_id) | **GET** /reverse-etl-models/{modelId}/subscriptionId/{subscriptionId}/syncs | List Reverse ETL Sync Statuses from Model And Subscription Id
[**update_reverse_etl_model**](ReverseETLApi.md#update_reverse_etl_model) | **PATCH** /reverse-etl-models/{modelId} | Update Reverse Etl Model



## Operation: cancel_reverse_etl_sync_for_model

> CancelReverseETLSyncForModel200Response cancel_reverse_etl_sync_for_model(model_id, sync_id, cancel_reverse_etl_sync_for_model_input)

Cancel Reverse ETL Sync for Model

Cancels a sync for a Reverse ETL Connection. It might take a few seconds to completely cancel the sync.   Will return an error if the sync is already completed or cancelled.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.cancel_reverse_etl_sync_for_model200_response import CancelReverseETLSyncForModel200Response
from segment_public_api.models.cancel_reverse_etl_sync_for_model_input import CancelReverseETLSyncForModelInput
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
    model_id = 'modelId' # str | 
    sync_id = '1' # str | 
    cancel_reverse_etl_sync_for_model_input = {"reasonForCanceling":0} # CancelReverseETLSyncForModelInput | 

    try:
        # Cancel Reverse ETL Sync for Model
        api_response = api_instance.cancel_reverse_etl_sync_for_model(model_id, sync_id, cancel_reverse_etl_sync_for_model_input)
        print("The response of ReverseETLApi->cancel_reverse_etl_sync_for_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->cancel_reverse_etl_sync_for_model: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **sync_id** | **str**|  | 
 **cancel_reverse_etl_sync_for_model_input** | [**CancelReverseETLSyncForModelInput**](CancelReverseETLSyncForModelInput.md)|  | 

### Return type

[**CancelReverseETLSyncForModel200Response**](CancelReverseETLSyncForModel200Response.md)

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


## Operation: create_reverse_etl_manual_sync

> CreateReverseETLManualSync200Response create_reverse_etl_manual_sync(create_reverse_etl_manual_sync_input)

Create Reverse ETL Manual Sync

Triggers a manual sync for a Reverse ETL Connection.   In the request body, the `subscription id` is the id that follows after `/mappings/` portion in the URL of the sync.   For example, the `subscription id` would be `2` for this sync: https://app.Segment.com/example-workspace/reverse-etl/destinations/example-destination/sources/example-source/instances/1/mappings/2/source-id/3/model-id/4/sync-details   The rate limit for this endpoint is 20 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_reverse_etl_manual_sync200_response import CreateReverseETLManualSync200Response
from segment_public_api.models.create_reverse_etl_manual_sync_input import CreateReverseETLManualSyncInput
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
    create_reverse_etl_manual_sync_input = {"sourceId":"sourceId","modelId":"modelId","subscriptionId":"subscriptionId"} # CreateReverseETLManualSyncInput | 

    try:
        # Create Reverse ETL Manual Sync
        api_response = api_instance.create_reverse_etl_manual_sync(create_reverse_etl_manual_sync_input)
        print("The response of ReverseETLApi->create_reverse_etl_manual_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->create_reverse_etl_manual_sync: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reverse_etl_manual_sync_input** | [**CreateReverseETLManualSyncInput**](CreateReverseETLManualSyncInput.md)|  | 

### Return type

[**CreateReverseETLManualSync200Response**](CreateReverseETLManualSync200Response.md)

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


## Operation: create_reverse_etl_model

> CreateReverseEtlModel201Response create_reverse_etl_model(create_reverse_etl_model_input)

Create Reverse Etl Model

Creates a new Reverse ETL Model.          • When called, this endpoint may generate the `Model Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_reverse_etl_model201_response import CreateReverseEtlModel201Response
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
    create_reverse_etl_model_input = {"sourceId":"qQEHquLrjRDN9j1ByrChyn","name":"Model 1","description":"This model is very useful.","enabled":true,"query":"SELECT 'user_1' AS id","queryIdentifierColumn":"id"} # CreateReverseEtlModelInput | 

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

[**CreateReverseEtlModel201Response**](CreateReverseEtlModel201Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
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
    model_id = 'fxXMc5bLdKnDfEgBpDbV11' # str | 

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
    model_id = 'jSAVzDH3z89geNDZwoNY9V' # str | 

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


## Operation: get_reverse_etl_sync_status

> GetReverseETLSyncStatus200Response get_reverse_etl_sync_status(model_id, sync_id)

Get Reverse ETL Sync Status

Get the sync status for a Reverse ETL sync.  The sync status includes all detailed information about the sync - sync status, duration, details about the extract and load phase if applicable, etc.   The rate limit for this endpoint is 250 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_reverse_etl_sync_status200_response import GetReverseETLSyncStatus200Response
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
    model_id = 'modelId' # str | 
    sync_id = 'syncId' # str | 

    try:
        # Get Reverse ETL Sync Status
        api_response = api_instance.get_reverse_etl_sync_status(model_id, sync_id)
        print("The response of ReverseETLApi->get_reverse_etl_sync_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->get_reverse_etl_sync_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **sync_id** | **str**|  | 

### Return type

[**GetReverseETLSyncStatus200Response**](GetReverseETLSyncStatus200Response.md)

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

> ListReverseEtlModels200Response list_reverse_etl_models(pagination=pagination)

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
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in alpha. (optional)

    try:
        # List Reverse Etl Models
        api_response = api_instance.list_reverse_etl_models(pagination=pagination)
        print("The response of ReverseETLApi->list_reverse_etl_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->list_reverse_etl_models: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in alpha. | [optional] 

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


## Operation: list_reverse_etl_sync_statuses_from_model_and_subscription_id

> ListReverseETLSyncStatusesFromModelAndSubscriptionId200Response list_reverse_etl_sync_statuses_from_model_and_subscription_id(model_id, subscription_id, count=count, cursor=cursor)

List Reverse ETL Sync Statuses from Model And Subscription Id

Get the sync statuses for a Reverse ETL mapping subscription.  The sync status includes all detailed information about the sync - sync status, duration, details about the extract and load phase if applicable, etc.  The default page count is 10, and then the next page can be fetched by passing the `cursor` query parameter.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_reverse_etl_sync_statuses_from_model_and_subscription_id200_response import ListReverseETLSyncStatusesFromModelAndSubscriptionId200Response
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
    model_id = 'modelId' # str | 
    subscription_id = 'subscriptionId' # str | 
    count = 3.4 # float | The number of items to retrieve in a page, between 1 and 100. Default is 10  This parameter exists in alpha. (optional)
    cursor = 'cursor_example' # str | The page to request. Acceptable values to use are from the `current`, `next`, and `previous` keys.  This parameter exists in alpha. (optional)

    try:
        # List Reverse ETL Sync Statuses from Model And Subscription Id
        api_response = api_instance.list_reverse_etl_sync_statuses_from_model_and_subscription_id(model_id, subscription_id, count=count, cursor=cursor)
        print("The response of ReverseETLApi->list_reverse_etl_sync_statuses_from_model_and_subscription_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseETLApi->list_reverse_etl_sync_statuses_from_model_and_subscription_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  | 
 **subscription_id** | **str**|  | 
 **count** | **float**| The number of items to retrieve in a page, between 1 and 100. Default is 10  This parameter exists in alpha. | [optional] 
 **cursor** | **str**| The page to request. Acceptable values to use are from the &#x60;current&#x60;, &#x60;next&#x60;, and &#x60;previous&#x60; keys.  This parameter exists in alpha. | [optional] 

### Return type

[**ListReverseETLSyncStatusesFromModelAndSubscriptionId200Response**](ListReverseETLSyncStatusesFromModelAndSubscriptionId200Response.md)

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
    model_id = '6BthE21tPsXyA2cK3QPQFQ' # str | 
    update_reverse_etl_model_input = {"name":"My Updated Model","query":"SELECT 'user_2' AS id"} # UpdateReverseEtlModelInput | 

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

