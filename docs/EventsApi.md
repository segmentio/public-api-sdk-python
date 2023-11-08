# segment_public_api.EventsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events_volume_from_workspace**](EventsApi.md#get_events_volume_from_workspace) | **GET** /events/volume | Get Events Volume from Workspace



## Operation: get_events_volume_from_workspace

> GetEventsVolumeFromWorkspace200Response get_events_volume_from_workspace(granularity, start_time, end_time, group_by=group_by, source_id=source_id, event_name=event_name, event_type=event_type, app_version=app_version, pagination=pagination)

Get Events Volume from Workspace

Enumerates the Workspace event volumes over time in minute increments.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_events_volume_from_workspace200_response import GetEventsVolumeFromWorkspace200Response
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
    api_instance = segment_public_api.EventsApi(api_client)
    granularity = 'DAY' # str | The size of each bucket in the requested window.  This parameter exists in v1.
    start_time = '2021-10-28T00:00:00Z' # str | The ISO8601 formatted timestamp that corresponds to the beginning of the requested time frame, inclusive.  This parameter exists in v1.
    end_time = '2021-10-29T16:40:00Z' # str | The ISO8601 formatted timestamp that corresponds to the end of the requested time frame, noninclusive. Segment recommends that you lag queries 1 minute behind clock time to reduce the risk for latency to impact the counts.  This parameter exists in v1.
    group_by = ['[\"eventType\"]'] # List[str] | A comma-delimited list of strings that represents the dimensions to group the result by. The options are: `eventName`, `eventType` and `source`.  This parameter exists in v1. (optional)
    source_id = ['source_id_example'] # List[str] | A list of strings which filters the results to the given SourceIds.  This parameter exists in v1. (optional)
    event_name = ['event_name_example'] # List[str] | A list of strings which filters the results to the given EventNames.  This parameter exists in v1. (optional)
    event_type = ['event_type_example'] # List[str] | A list of strings which filters the results to the given EventTypes.  This parameter exists in v1. (optional)
    app_version = ['app_version_example'] # List[str] | A list of strings which filters the results to the given AppVersions.  This parameter exists in v1. (optional)
    pagination = segment_public_api.PaginationInput() # PaginationInput | Pagination input for event volume by Workspace.  This parameter exists in v1. (optional)

    try:
        # Get Events Volume from Workspace
        api_response = api_instance.get_events_volume_from_workspace(granularity, start_time, end_time, group_by=group_by, source_id=source_id, event_name=event_name, event_type=event_type, app_version=app_version, pagination=pagination)
        print("The response of EventsApi->get_events_volume_from_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events_volume_from_workspace: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granularity** | **str**| The size of each bucket in the requested window.  This parameter exists in v1. | 
 **start_time** | **str**| The ISO8601 formatted timestamp that corresponds to the beginning of the requested time frame, inclusive.  This parameter exists in v1. | 
 **end_time** | **str**| The ISO8601 formatted timestamp that corresponds to the end of the requested time frame, noninclusive. Segment recommends that you lag queries 1 minute behind clock time to reduce the risk for latency to impact the counts.  This parameter exists in v1. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings that represents the dimensions to group the result by. The options are: &#x60;eventName&#x60;, &#x60;eventType&#x60; and &#x60;source&#x60;.  This parameter exists in v1. | [optional] 
 **source_id** | [**List[str]**](str.md)| A list of strings which filters the results to the given SourceIds.  This parameter exists in v1. | [optional] 
 **event_name** | [**List[str]**](str.md)| A list of strings which filters the results to the given EventNames.  This parameter exists in v1. | [optional] 
 **event_type** | [**List[str]**](str.md)| A list of strings which filters the results to the given EventTypes.  This parameter exists in v1. | [optional] 
 **app_version** | [**List[str]**](str.md)| A list of strings which filters the results to the given AppVersions.  This parameter exists in v1. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Pagination input for event volume by Workspace.  This parameter exists in v1. | [optional] 

### Return type

[**GetEventsVolumeFromWorkspace200Response**](GetEventsVolumeFromWorkspace200Response.md)

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

