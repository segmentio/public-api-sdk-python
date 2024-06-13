# segment_public_api.DeliveryOverviewApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_egress_failed_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_egress_failed_metrics_from_delivery_overview) | **GET** /delivery-overview/failed-delivery | Get Egress Failed Metrics from Delivery Overview
[**get_egress_success_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_egress_success_metrics_from_delivery_overview) | **GET** /delivery-overview/successful-delivery | Get Egress Success Metrics from Delivery Overview
[**get_filtered_at_destination_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_filtered_at_destination_metrics_from_delivery_overview) | **GET** /delivery-overview/filtered-at-destination | Get Filtered At Destination Metrics from Delivery Overview
[**get_filtered_at_source_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_filtered_at_source_metrics_from_delivery_overview) | **GET** /delivery-overview/filtered-at-source | Get Filtered At Source Metrics from Delivery Overview
[**get_ingress_failed_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_ingress_failed_metrics_from_delivery_overview) | **GET** /delivery-overview/failed-on-ingest | Get Ingress Failed Metrics from Delivery Overview
[**get_ingress_success_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_ingress_success_metrics_from_delivery_overview) | **GET** /delivery-overview/successfully-received | Get Ingress Success Metrics from Delivery Overview
[**get_linked_audience_success_metrics_from_delivery_overview**](DeliveryOverviewApi.md#get_linked_audience_success_metrics_from_delivery_overview) | **GET** /delivery-overview/audience/success | Get Linked Audience Success Metrics from Delivery Overview



## Operation: get_egress_failed_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_egress_failed_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Egress Failed Metrics from Delivery Overview

Get events that failed to be delivered to Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_destination_filter_by import DeliveryOverviewDestinationFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    destination_config_id = 'fP7qoQw2HTWt9WdMr718gn' # str | The id tied to a Workspace Destination.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=eventName'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, `discardReason`, `appVersion`, `subscriptionId`, `activationId`, `audienceId`, or `spaceId`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewDestinationFilterBy() # DeliveryOverviewDestinationFilterBy | An optional filter for `eventName`, `eventType`, `discardReason`, `appVersion`, `subscriptionId`, `activationId`, `audienceId`, and/or `spaceId` that can be applied in addition to a `groupBy`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Egress Failed Metrics from Delivery Overview
        api_response = api_instance.get_egress_failed_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_egress_failed_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_egress_failed_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **destination_config_id** | **str**| The id tied to a Workspace Destination.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, &#x60;appVersion&#x60;, &#x60;subscriptionId&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, or &#x60;spaceId&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewDestinationFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, &#x60;appVersion&#x60;, &#x60;subscriptionId&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, and/or &#x60;spaceId&#x60; that can be applied in addition to a &#x60;groupBy&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_egress_success_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_egress_success_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Egress Success Metrics from Delivery Overview

Get events successfully delivered to Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_destination_filter_by import DeliveryOverviewDestinationFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    destination_config_id = 'fP7qoQw2HTWt9WdMr718gn' # str | The id tied to a Workspace Destination.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=eventName'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, `discardReason`, `appVersion`, `subscriptionId`, `activationId`, `audienceId`, and `spaceId`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewDestinationFilterBy() # DeliveryOverviewDestinationFilterBy | An optional filter for `eventName`, `eventType`, `discardReason`, `appVersion`, `subscriptionId`, `activationId`, `audienceId`, and/or `spaceId` that can be applied in addition to a `groupBy`. If you would like to view retry attempts for a successful delivery, you can filter `discardReason` from `successes.attempt.1` through `successes.attempt.10`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Egress Success Metrics from Delivery Overview
        api_response = api_instance.get_egress_success_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_egress_success_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_egress_success_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **destination_config_id** | **str**| The id tied to a Workspace Destination.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, &#x60;appVersion&#x60;, &#x60;subscriptionId&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, and &#x60;spaceId&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewDestinationFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, &#x60;appVersion&#x60;, &#x60;subscriptionId&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, and/or &#x60;spaceId&#x60; that can be applied in addition to a &#x60;groupBy&#x60;. If you would like to view retry attempts for a successful delivery, you can filter &#x60;discardReason&#x60; from &#x60;successes.attempt.1&#x60; through &#x60;successes.attempt.10&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_filtered_at_destination_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_filtered_at_destination_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Filtered At Destination Metrics from Delivery Overview

Get events that were filtered at Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_destination_filter_by import DeliveryOverviewDestinationFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    destination_config_id = 'fP7qoQw2HTWt9WdMr718gn' # str | The id tied to a Workspace Destination.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=eventName'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, `discardReason`, `appVersion`, `subscriptionId`, `activationId`, `audienceId`, or `spaceId`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewDestinationFilterBy() # DeliveryOverviewDestinationFilterBy | An optional filter for `eventName`, `eventType`, `discardReason`, `appVersion`, `subscriptionId`, `activationId`, `audienceId`, and/or `spaceId` that can be applied in addition to a `groupBy`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Filtered At Destination Metrics from Delivery Overview
        api_response = api_instance.get_filtered_at_destination_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_filtered_at_destination_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_filtered_at_destination_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **destination_config_id** | **str**| The id tied to a Workspace Destination.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, &#x60;appVersion&#x60;, &#x60;subscriptionId&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, or &#x60;spaceId&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewDestinationFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, &#x60;appVersion&#x60;, &#x60;subscriptionId&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, and/or &#x60;spaceId&#x60; that can be applied in addition to a &#x60;groupBy&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_filtered_at_source_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_filtered_at_source_metrics_from_delivery_overview(source_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Filtered At Source Metrics from Delivery Overview

Get events that were filtered at Source.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_source_filter_by import DeliveryOverviewSourceFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=eventName'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, `discardReason`, and `appVersion`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewSourceFilterBy() # DeliveryOverviewSourceFilterBy | An optional filter for `eventName`, `eventType`, `discardReason`, and/or `appVersion` that can be applied in addition to a `groupBy`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Optional params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Filtered At Source Metrics from Delivery Overview
        api_response = api_instance.get_filtered_at_source_metrics_from_delivery_overview(source_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_filtered_at_source_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_filtered_at_source_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, and &#x60;appVersion&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewSourceFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, and/or &#x60;appVersion&#x60; that can be applied in addition to a &#x60;groupBy&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Optional params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_ingress_failed_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_ingress_failed_metrics_from_delivery_overview(source_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Ingress Failed Metrics from Delivery Overview

Get events that failed on ingest.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_source_filter_by import DeliveryOverviewSourceFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=eventName'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, `discardReason`, and `appVersion`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewSourceFilterBy() # DeliveryOverviewSourceFilterBy | An optional filter for `eventName`, `eventType`, `discardReason`, and/or `appVersion` that can be applied in addition to a `groupBy`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Optional params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Ingress Failed Metrics from Delivery Overview
        api_response = api_instance.get_ingress_failed_metrics_from_delivery_overview(source_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_ingress_failed_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_ingress_failed_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, and &#x60;appVersion&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewSourceFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;discardReason&#x60;, and/or &#x60;appVersion&#x60; that can be applied in addition to a &#x60;groupBy&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Optional params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_ingress_success_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_ingress_success_metrics_from_delivery_overview(source_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Ingress Success Metrics from Delivery Overview

Get events that were successfully received by Segment.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_successfully_received_filter_by import DeliveryOverviewSuccessfullyReceivedFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=eventName'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, and `appVersion`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewSuccessfullyReceivedFilterBy() # DeliveryOverviewSuccessfullyReceivedFilterBy | An optional filter for `eventName`, `eventType`, and/or `appVersion` that can be applied in addition to a `groupBy`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Optional params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Ingress Success Metrics from Delivery Overview
        api_response = api_instance.get_ingress_success_metrics_from_delivery_overview(source_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_ingress_success_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_ingress_success_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, and &#x60;appVersion&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewSuccessfullyReceivedFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, and/or &#x60;appVersion&#x60; that can be applied in addition to a &#x60;groupBy&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Optional params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_linked_audience_success_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_linked_audience_success_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)

Get Linked Audience Success Metrics from Delivery Overview

Get events successfully delivered for Linked Audiences.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delivery_overview_audience_filter_by import DeliveryOverviewAudienceFilterBy
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    api_instance = segment_public_api.DeliveryOverviewApi(api_client)
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The sourceId for the Workspace.  This parameter exists in beta.
    destination_config_id = 'fP7qoQw2HTWt9WdMr718gn' # str | The id tied to a Workspace Destination.  This parameter exists in beta.
    start_time = '2024-01-01T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta.
    end_time = '2024-01-03T00:00:00Z' # str | The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta.
    granularity = 'DAY' # str | The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta.
    group_by = ['groupBy.0=spaceId'] # List[str] | A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: `eventName`, `eventType`, `activationId`, `audienceId`, and `spaceId`.  This parameter exists in beta. (optional)
    filter = segment_public_api.DeliveryOverviewAudienceFilterBy() # DeliveryOverviewAudienceFilterBy | An optional filter for `eventName`, `eventType`, `activationId`, `audienceId`, and/or `spaceId` that can be applied in addition to a `groupBy`.  This parameter exists in beta. (optional)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Params to specify the page cursor and count.  This parameter exists in beta. (optional)

    try:
        # Get Linked Audience Success Metrics from Delivery Overview
        api_response = api_instance.get_linked_audience_success_metrics_from_delivery_overview(source_id, destination_config_id, start_time, end_time, granularity, group_by=group_by, filter=filter, pagination=pagination)
        print("The response of DeliveryOverviewApi->get_linked_audience_success_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_linked_audience_success_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The sourceId for the Workspace.  This parameter exists in beta. | 
 **destination_config_id** | **str**| The id tied to a Workspace Destination.  This parameter exists in beta. | 
 **start_time** | **str**| The ISO8601 formatted timestamp corresponding to the beginning of the requested timeframe, inclusive.  This parameter exists in beta. | 
 **end_time** | **str**| The ISO8601 formatted timestamp corresponding to the end of the requested timeframe, noninclusive.  This parameter exists in beta. | 
 **granularity** | **str**| The size of each bucket in the requested window.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 14 days - Oldest possible start time: 30 days in the past  **Day**: - Max time range: 30 days - Oldest possible start time: 30 days in the past  This parameter exists in beta. | 
 **group_by** | [**List[str]**](str.md)| A comma-delimited list of strings representing one or more dimensions to group the result by.  Valid options are: &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, and &#x60;spaceId&#x60;.  This parameter exists in beta. | [optional] 
 **filter** | [**DeliveryOverviewAudienceFilterBy**](.md)| An optional filter for &#x60;eventName&#x60;, &#x60;eventType&#x60;, &#x60;activationId&#x60;, &#x60;audienceId&#x60;, and/or &#x60;spaceId&#x60; that can be applied in addition to a &#x60;groupBy&#x60;.  This parameter exists in beta. | [optional] 
 **pagination** | [**PaginationInput**](.md)| Params to specify the page cursor and count.  This parameter exists in beta. | [optional] 

### Return type

[**GetEgressFailedMetricsFromDeliveryOverview200Response**](GetEgressFailedMetricsFromDeliveryOverview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

