# segment_public_api.AuditTrailApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_audit_events**](AuditTrailApi.md#list_audit_events) | **GET** /audit-events | List Audit Events



## Operation: list_audit_events

> ListAuditEvents200Response list_audit_events(pagination, start_time=start_time, end_time=end_time, resource_id=resource_id, resource_type=resource_type)

List Audit Events

Returns a list of Audit Trail events.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_audit_events200_response import ListAuditEvents200Response
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
    api_instance = segment_public_api.AuditTrailApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1.
    start_time = 'start_time_example' # str | Filter response to events that happened after this time.  This parameter exists in v1. (optional)
    end_time = 'end_time_example' # str | Filter response to events that happened before this time. Defaults to the current time, or the end time from the pagination cursor.  This parameter exists in v1. (optional)
    resource_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | Filter response to events that affect a specific resource, for example, a single Source.  This parameter exists in v1. (optional)
    resource_type = 'resource_type_example' # str | Filter response to events that affect a specific type, for example, Sources, Warehouses, and Tracking Plans.  This parameter exists in v1. (optional)

    try:
        # List Audit Events
        api_response = api_instance.list_audit_events(pagination, start_time=start_time, end_time=end_time, resource_id=resource_id, resource_type=resource_type)
        print("The response of AuditTrailApi->list_audit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailApi->list_audit_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | 
 **start_time** | **str**| Filter response to events that happened after this time.  This parameter exists in v1. | [optional] 
 **end_time** | **str**| Filter response to events that happened before this time. Defaults to the current time, or the end time from the pagination cursor.  This parameter exists in v1. | [optional] 
 **resource_id** | **str**| Filter response to events that affect a specific resource, for example, a single Source.  This parameter exists in v1. | [optional] 
 **resource_type** | **str**| Filter response to events that affect a specific type, for example, Sources, Warehouses, and Tracking Plans.  This parameter exists in v1. | [optional] 

### Return type

[**ListAuditEvents200Response**](ListAuditEvents200Response.md)

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

