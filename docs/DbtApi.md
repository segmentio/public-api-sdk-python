# segment_public_api.DbtApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dbt_model_sync_trigger**](DbtApi.md#create_dbt_model_sync_trigger) | **POST** /dbt-model-syncs/trigger | Create Dbt Model Sync Trigger



## Operation: create_dbt_model_sync_trigger

> CreateDbtModelSyncTrigger200Response create_dbt_model_sync_trigger(create_dbt_model_sync_trigger_input)

Create Dbt Model Sync Trigger

Creates a trigger for a new dbt model sync for a Source.   The rate limit for this endpoint is 10 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_dbt_model_sync_trigger200_response import CreateDbtModelSyncTrigger200Response
from segment_public_api.models.create_dbt_model_sync_trigger_input import CreateDbtModelSyncTriggerInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DbtApi(api_client)
    create_dbt_model_sync_trigger_input = {"sourceId":"source-id"} # CreateDbtModelSyncTriggerInput | 

    try:
        # Create Dbt Model Sync Trigger
        api_response = api_instance.create_dbt_model_sync_trigger(create_dbt_model_sync_trigger_input)
        print("The response of DbtApi->create_dbt_model_sync_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DbtApi->create_dbt_model_sync_trigger: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dbt_model_sync_trigger_input** | [**CreateDbtModelSyncTriggerInput**](CreateDbtModelSyncTriggerInput.md)|  | 

### Return type

[**CreateDbtModelSyncTrigger200Response**](CreateDbtModelSyncTrigger200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1beta+json
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

