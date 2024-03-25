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



## Operation: get_egress_failed_metrics_from_delivery_overview

> GetEgressFailedMetricsFromDeliveryOverview200Response get_egress_failed_metrics_from_delivery_overview(metrics)

Get Egress Failed Metrics from Delivery Overview

Get events that failed to be delivered to Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_delivery_overview_dest_metrics_beta_input import GetDeliveryOverviewDestMetricsBetaInput
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    metrics = segment_public_api.GetDeliveryOverviewDestMetricsBetaInput() # GetDeliveryOverviewDestMetricsBetaInput | Metrics for this Destination pipeline step.  This parameter exists in beta.

    try:
        # Get Egress Failed Metrics from Delivery Overview
        api_response = api_instance.get_egress_failed_metrics_from_delivery_overview(metrics)
        print("The response of DeliveryOverviewApi->get_egress_failed_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_egress_failed_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**GetDeliveryOverviewDestMetricsBetaInput**](.md)| Metrics for this Destination pipeline step.  This parameter exists in beta. | 

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

> GetEgressFailedMetricsFromDeliveryOverview200Response get_egress_success_metrics_from_delivery_overview(metrics)

Get Egress Success Metrics from Delivery Overview

Get events successfully delivered to Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_delivery_overview_dest_metrics_beta_input import GetDeliveryOverviewDestMetricsBetaInput
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    metrics = segment_public_api.GetDeliveryOverviewDestMetricsBetaInput() # GetDeliveryOverviewDestMetricsBetaInput | Metrics for this Destination pipeline step.  This parameter exists in beta.

    try:
        # Get Egress Success Metrics from Delivery Overview
        api_response = api_instance.get_egress_success_metrics_from_delivery_overview(metrics)
        print("The response of DeliveryOverviewApi->get_egress_success_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_egress_success_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**GetDeliveryOverviewDestMetricsBetaInput**](.md)| Metrics for this Destination pipeline step.  This parameter exists in beta. | 

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

> GetEgressFailedMetricsFromDeliveryOverview200Response get_filtered_at_destination_metrics_from_delivery_overview(metrics)

Get Filtered At Destination Metrics from Delivery Overview

Get events that were filtered at Destination.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_delivery_overview_dest_metrics_beta_input import GetDeliveryOverviewDestMetricsBetaInput
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    metrics = segment_public_api.GetDeliveryOverviewDestMetricsBetaInput() # GetDeliveryOverviewDestMetricsBetaInput | Metrics for this Destination pipeline step.  This parameter exists in beta.

    try:
        # Get Filtered At Destination Metrics from Delivery Overview
        api_response = api_instance.get_filtered_at_destination_metrics_from_delivery_overview(metrics)
        print("The response of DeliveryOverviewApi->get_filtered_at_destination_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_filtered_at_destination_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**GetDeliveryOverviewDestMetricsBetaInput**](.md)| Metrics for this Destination pipeline step.  This parameter exists in beta. | 

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

> GetEgressFailedMetricsFromDeliveryOverview200Response get_filtered_at_source_metrics_from_delivery_overview(metrics)

Get Filtered At Source Metrics from Delivery Overview

Get events that were filtered at Source.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_delivery_overview_source_metrics_beta_input import GetDeliveryOverviewSourceMetricsBetaInput
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    metrics = segment_public_api.GetDeliveryOverviewSourceMetricsBetaInput() # GetDeliveryOverviewSourceMetricsBetaInput | Metrics for this Source pipeline step.  This parameter exists in beta.

    try:
        # Get Filtered At Source Metrics from Delivery Overview
        api_response = api_instance.get_filtered_at_source_metrics_from_delivery_overview(metrics)
        print("The response of DeliveryOverviewApi->get_filtered_at_source_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_filtered_at_source_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**GetDeliveryOverviewSourceMetricsBetaInput**](.md)| Metrics for this Source pipeline step.  This parameter exists in beta. | 

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

> GetEgressFailedMetricsFromDeliveryOverview200Response get_ingress_failed_metrics_from_delivery_overview(metrics)

Get Ingress Failed Metrics from Delivery Overview

Get events that failed on ingest.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_delivery_overview_source_metrics_beta_input import GetDeliveryOverviewSourceMetricsBetaInput
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    metrics = segment_public_api.GetDeliveryOverviewSourceMetricsBetaInput() # GetDeliveryOverviewSourceMetricsBetaInput | Metrics for this Source pipeline step.  This parameter exists in beta.

    try:
        # Get Ingress Failed Metrics from Delivery Overview
        api_response = api_instance.get_ingress_failed_metrics_from_delivery_overview(metrics)
        print("The response of DeliveryOverviewApi->get_ingress_failed_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_ingress_failed_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**GetDeliveryOverviewSourceMetricsBetaInput**](.md)| Metrics for this Source pipeline step.  This parameter exists in beta. | 

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

> GetEgressFailedMetricsFromDeliveryOverview200Response get_ingress_success_metrics_from_delivery_overview(metrics)

Get Ingress Success Metrics from Delivery Overview

Get events that were successfully received by Segment.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_delivery_overview_source_metrics_beta_input import GetDeliveryOverviewSourceMetricsBetaInput
from segment_public_api.models.get_egress_failed_metrics_from_delivery_overview200_response import GetEgressFailedMetricsFromDeliveryOverview200Response
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
    metrics = segment_public_api.GetDeliveryOverviewSourceMetricsBetaInput() # GetDeliveryOverviewSourceMetricsBetaInput | Metrics for this Source pipeline step.  This parameter exists in beta.

    try:
        # Get Ingress Success Metrics from Delivery Overview
        api_response = api_instance.get_ingress_success_metrics_from_delivery_overview(metrics)
        print("The response of DeliveryOverviewApi->get_ingress_success_metrics_from_delivery_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryOverviewApi->get_ingress_success_metrics_from_delivery_overview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | [**GetDeliveryOverviewSourceMetricsBetaInput**](.md)| Metrics for this Source pipeline step.  This parameter exists in beta. | 

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

