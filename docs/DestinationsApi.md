# segment_public_api.DestinationsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_destination**](DestinationsApi.md#create_destination) | **POST** /destinations | Create Destination
[**create_destination_subscription**](DestinationsApi.md#create_destination_subscription) | **POST** /destinations/{destinationId}/subscriptions | Create Destination Subscription
[**delete_destination**](DestinationsApi.md#delete_destination) | **DELETE** /destinations/{destinationId} | Delete Destination
[**get_destination**](DestinationsApi.md#get_destination) | **GET** /destinations/{destinationId} | Get Destination
[**get_subscription_from_destination**](DestinationsApi.md#get_subscription_from_destination) | **GET** /destinations/{destinationId}/subscriptions/{id} | Get Subscription from Destination
[**list_delivery_metrics_summary_from_destination**](DestinationsApi.md#list_delivery_metrics_summary_from_destination) | **GET** /destinations/{destinationId}/delivery-metrics | List Delivery Metrics Summary from Destination
[**list_destinations**](DestinationsApi.md#list_destinations) | **GET** /destinations | List Destinations
[**list_subscriptions_from_destination**](DestinationsApi.md#list_subscriptions_from_destination) | **GET** /destinations/{destinationId}/subscriptions | List Subscriptions from Destination
[**remove_subscription_from_destination**](DestinationsApi.md#remove_subscription_from_destination) | **DELETE** /destinations/{destinationId}/subscriptions/{id} | Remove Subscription from Destination
[**update_destination**](DestinationsApi.md#update_destination) | **PATCH** /destinations/{destinationId} | Update Destination
[**update_subscription_for_destination**](DestinationsApi.md#update_subscription_for_destination) | **PATCH** /destinations/{destinationId}/subscriptions/{id} | Update Subscription for Destination



## Operation: create_destination

> CreateDestination200Response create_destination(create_destination_v1_input)

Create Destination

Creates a new Destination.    • When called, this endpoint may generate the `Integration Created` event in the [audit trail](/tag/Audit-Trail).       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_destination200_response import CreateDestination200Response
from segment_public_api.models.create_destination_v1_input import CreateDestinationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    create_destination_v1_input = {"sourceId":"rh5BDZp6QDHvXFCkibm1pR","metadataId":"54521fd525e721e32a72ee91","name":"my destination v1","settings":{"apiKey":"3cb9b589437d3904f19b2b791c2cdada","retarget":true}} # CreateDestinationV1Input | 

    try:
        # Create Destination
        api_response = api_instance.create_destination(create_destination_v1_input)
        print("The response of DestinationsApi->create_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->create_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_destination_v1_input** | [**CreateDestinationV1Input**](CreateDestinationV1Input.md)|  | 

### Return type

[**CreateDestination200Response**](CreateDestination200Response.md)

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


## Operation: create_destination_subscription

> CreateDestinationSubscription200Response create_destination_subscription(destination_id, create_destination_subscription_alpha_input)

Create Destination Subscription

Creates a new Destination subscription.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Destination Subscriptions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_destination_subscription200_response import CreateDestinationSubscription200Response
from segment_public_api.models.create_destination_subscription_alpha_input import CreateDestinationSubscriptionAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    create_destination_subscription_alpha_input = {"name":"Example Subscription","actionId":"jiMz7MfHNeHmUckzRnUGkU","trigger":"type = \"track\"","enabled":false} # CreateDestinationSubscriptionAlphaInput | 

    try:
        # Create Destination Subscription
        api_response = api_instance.create_destination_subscription(destination_id, create_destination_subscription_alpha_input)
        print("The response of DestinationsApi->create_destination_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->create_destination_subscription: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **create_destination_subscription_alpha_input** | [**CreateDestinationSubscriptionAlphaInput**](CreateDestinationSubscriptionAlphaInput.md)|  | 

### Return type

[**CreateDestinationSubscription200Response**](CreateDestinationSubscription200Response.md)

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


## Operation: delete_destination

> DeleteDestination200Response delete_destination(destination_id)

Delete Destination

Deletes an existing Destination.    • When called, this endpoint may generate the `Integration Deleted` event in the [audit trail](/tag/Audit-Trail).  Config API omitted fields: - `catalogId`       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_destination200_response import DeleteDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = '65c2bdbede6f2d8297f943db' # str | 

    try:
        # Delete Destination
        api_response = api_instance.delete_destination(destination_id)
        print("The response of DestinationsApi->delete_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->delete_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 

### Return type

[**DeleteDestination200Response**](DeleteDestination200Response.md)

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


## Operation: get_destination

> GetDestination200Response get_destination(destination_id)

Get Destination

Returns a Destination by its id.        Config API omitted fields: - `catalogId` 

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_destination200_response import GetDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'qtiZHLLqqsHmpvLXNtP5du' # str | 

    try:
        # Get Destination
        api_response = api_instance.get_destination(destination_id)
        print("The response of DestinationsApi->get_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->get_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 

### Return type

[**GetDestination200Response**](GetDestination200Response.md)

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


## Operation: get_subscription_from_destination

> GetSubscriptionFromDestination200Response get_subscription_from_destination(destination_id, id)

Get Subscription from Destination

Gets a Destination subscription by id.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Destination Subscriptions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_subscription_from_destination200_response import GetSubscriptionFromDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    id = 'kyMKN6LUgMvF8dwRMEz3cX' # str | 

    try:
        # Get Subscription from Destination
        api_response = api_instance.get_subscription_from_destination(destination_id, id)
        print("The response of DestinationsApi->get_subscription_from_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->get_subscription_from_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetSubscriptionFromDestination200Response**](GetSubscriptionFromDestination200Response.md)

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


## Operation: list_delivery_metrics_summary_from_destination

> ListDeliveryMetricsSummaryFromDestination200Response list_delivery_metrics_summary_from_destination(destination_id, source_id, start_time=start_time, end_time=end_time, granularity=granularity)

List Delivery Metrics Summary from Destination

Get an event delivery metrics summary from a Destination.  Based on the granularity chosen, there are restrictions on the time range you can query:  **Minute**: - Max time range: 4 hours - Oldest possible start time: 48 hours in the past  **Hour**: - Max Time range: 7 days - Oldest possible start time: 7 days in the past  **Day**: - Max time range: 14 days - Oldest possible start time: 14 days in the past

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_delivery_metrics_summary_from_destination200_response import ListDeliveryMetricsSummaryFromDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    source_id = 'rh5BDZp6QDHvXFCkibm1pR' # str | The id of the Source linked to the Destination.  Config API note: analogous to `parent`.  This parameter exists in beta.
    start_time = '2006-01-02T15:04:05.000Z' # str | Filter events that happened after this time.  Defaults to: - 1 hour ago if granularity is `MINUTE`. - 7 days ago if granularity is `HOUR`. - 30 days ago if granularity is `DAY`.  This parameter exists in beta. (optional)
    end_time = '2006-01-02T15:04:05.000Z' # str | Filter events that happened before this time. Defaults to now if not set.  This parameter exists in beta. (optional)
    granularity = 'DAY' # str | The granularity to filter metrics to. Either `MINUTE`, `HOUR` or `DAY`.  Defaults to `MINUTE` if not set.  This parameter exists in beta. (optional)

    try:
        # List Delivery Metrics Summary from Destination
        api_response = api_instance.list_delivery_metrics_summary_from_destination(destination_id, source_id, start_time=start_time, end_time=end_time, granularity=granularity)
        print("The response of DestinationsApi->list_delivery_metrics_summary_from_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->list_delivery_metrics_summary_from_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **source_id** | **str**| The id of the Source linked to the Destination.  Config API note: analogous to &#x60;parent&#x60;.  This parameter exists in beta. | 
 **start_time** | **str**| Filter events that happened after this time.  Defaults to: - 1 hour ago if granularity is &#x60;MINUTE&#x60;. - 7 days ago if granularity is &#x60;HOUR&#x60;. - 30 days ago if granularity is &#x60;DAY&#x60;.  This parameter exists in beta. | [optional] 
 **end_time** | **str**| Filter events that happened before this time. Defaults to now if not set.  This parameter exists in beta. | [optional] 
 **granularity** | **str**| The granularity to filter metrics to. Either &#x60;MINUTE&#x60;, &#x60;HOUR&#x60; or &#x60;DAY&#x60;.  Defaults to &#x60;MINUTE&#x60; if not set.  This parameter exists in beta. | [optional] 

### Return type

[**ListDeliveryMetricsSummaryFromDestination200Response**](ListDeliveryMetricsSummaryFromDestination200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: list_destinations

> ListDestinations200Response list_destinations(pagination=pagination)

List Destinations

Returns a list of Destinations.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_destinations200_response import ListDestinations200Response
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
    api_instance = segment_public_api.DestinationsApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Required pagination params for the request.  This parameter exists in v1. (optional)

    try:
        # List Destinations
        api_response = api_instance.list_destinations(pagination=pagination)
        print("The response of DestinationsApi->list_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->list_destinations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Required pagination params for the request.  This parameter exists in v1. | [optional] 

### Return type

[**ListDestinations200Response**](ListDestinations200Response.md)

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


## Operation: list_subscriptions_from_destination

> ListSubscriptionsFromDestination200Response list_subscriptions_from_destination(destination_id, pagination=pagination)

List Subscriptions from Destination

Lists subscriptions for a Destination.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Destination Subscriptions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_subscriptions_from_destination200_response import ListSubscriptionsFromDestination200Response
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
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination options.  This parameter exists in alpha. (optional)

    try:
        # List Subscriptions from Destination
        api_response = api_instance.list_subscriptions_from_destination(destination_id, pagination=pagination)
        print("The response of DestinationsApi->list_subscriptions_from_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->list_subscriptions_from_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination options.  This parameter exists in alpha. | [optional] 

### Return type

[**ListSubscriptionsFromDestination200Response**](ListSubscriptionsFromDestination200Response.md)

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


## Operation: remove_subscription_from_destination

> RemoveSubscriptionFromDestination200Response remove_subscription_from_destination(destination_id, id)

Remove Subscription from Destination

Deletes an existing Destination subscription.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Destination Subscriptions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_subscription_from_destination200_response import RemoveSubscriptionFromDestination200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    id = 'zXCqmEMHJojkD45GcBAPt' # str | 

    try:
        # Remove Subscription from Destination
        api_response = api_instance.remove_subscription_from_destination(destination_id, id)
        print("The response of DestinationsApi->remove_subscription_from_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->remove_subscription_from_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RemoveSubscriptionFromDestination200Response**](RemoveSubscriptionFromDestination200Response.md)

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


## Operation: update_destination

> UpdateDestination200Response update_destination(destination_id, update_destination_v1_input)

Update Destination

Updates an existing Destination.  **Note**: if you attempt to update read-only settings for your destination you'll encounter the following behavior:    * If only read-only properties are being updated, the endpoint will return an HTTP 400 error.   * If there's a mix of writable and read-only properties in the payload, the request will be accepted, the writable properties will be updated and the read-only properties ignored.     • When called, this endpoint may generate the `Integration Disabled` event in the [audit trail](/tag/Audit-Trail).  Config API omitted fields: - `updateMask`          

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_destination200_response import UpdateDestination200Response
from segment_public_api.models.update_destination_v1_input import UpdateDestinationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'qtiZHLLqqsHmpvLXNtP5du' # str | 
    update_destination_v1_input = {"enabled":false} # UpdateDestinationV1Input | 

    try:
        # Update Destination
        api_response = api_instance.update_destination(destination_id, update_destination_v1_input)
        print("The response of DestinationsApi->update_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->update_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **update_destination_v1_input** | [**UpdateDestinationV1Input**](UpdateDestinationV1Input.md)|  | 

### Return type

[**UpdateDestination200Response**](UpdateDestination200Response.md)

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


## Operation: update_subscription_for_destination

> UpdateSubscriptionForDestination200Response update_subscription_for_destination(destination_id, id, update_subscription_for_destination_alpha_input)

Update Subscription for Destination

Updates an existing Destination subscription.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Destination Subscriptions feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_subscription_for_destination200_response import UpdateSubscriptionForDestination200Response
from segment_public_api.models.update_subscription_for_destination_alpha_input import UpdateSubscriptionForDestinationAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.DestinationsApi(api_client)
    destination_id = 'fP7qoQw2HTWt9WdMr718gn' # str | 
    id = '3ELMSracBm5MMikXBYfo1c' # str | 
    update_subscription_for_destination_alpha_input = {"input":{"name":"Updated name"}} # UpdateSubscriptionForDestinationAlphaInput | 

    try:
        # Update Subscription for Destination
        api_response = api_instance.update_subscription_for_destination(destination_id, id, update_subscription_for_destination_alpha_input)
        print("The response of DestinationsApi->update_subscription_for_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsApi->update_subscription_for_destination: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_id** | **str**|  | 
 **id** | **str**|  | 
 **update_subscription_for_destination_alpha_input** | [**UpdateSubscriptionForDestinationAlphaInput**](UpdateSubscriptionForDestinationAlphaInput.md)|  | 

### Return type

[**UpdateSubscriptionForDestination200Response**](UpdateSubscriptionForDestination200Response.md)

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

