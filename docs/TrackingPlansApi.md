# segment_public_api.TrackingPlansApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_source_to_tracking_plan**](TrackingPlansApi.md#add_source_to_tracking_plan) | **POST** /tracking-plans/{trackingPlanId}/sources | Add Source to Tracking Plan
[**create_tracking_plan**](TrackingPlansApi.md#create_tracking_plan) | **POST** /tracking-plans | Create Tracking Plan
[**delete_tracking_plan**](TrackingPlansApi.md#delete_tracking_plan) | **DELETE** /tracking-plans/{trackingPlanId} | Delete Tracking Plan
[**get_tracking_plan**](TrackingPlansApi.md#get_tracking_plan) | **GET** /tracking-plans/{trackingPlanId} | Get Tracking Plan
[**list_rules_from_tracking_plan**](TrackingPlansApi.md#list_rules_from_tracking_plan) | **GET** /tracking-plans/{trackingPlanId}/rules | List Rules from Tracking Plan
[**list_sources_from_tracking_plan**](TrackingPlansApi.md#list_sources_from_tracking_plan) | **GET** /tracking-plans/{trackingPlanId}/sources | List Sources from Tracking Plan
[**list_tracking_plans**](TrackingPlansApi.md#list_tracking_plans) | **GET** /tracking-plans | List Tracking Plans
[**remove_rules_from_tracking_plan**](TrackingPlansApi.md#remove_rules_from_tracking_plan) | **DELETE** /tracking-plans/{trackingPlanId}/rules | Remove Rules from Tracking Plan
[**remove_source_from_tracking_plan**](TrackingPlansApi.md#remove_source_from_tracking_plan) | **DELETE** /tracking-plans/{trackingPlanId}/sources | Remove Source from Tracking Plan
[**replace_rules_in_tracking_plan**](TrackingPlansApi.md#replace_rules_in_tracking_plan) | **PUT** /tracking-plans/{trackingPlanId}/rules | Replace Rules in Tracking Plan
[**update_rules_in_tracking_plan**](TrackingPlansApi.md#update_rules_in_tracking_plan) | **PATCH** /tracking-plans/{trackingPlanId}/rules | Update Rules in Tracking Plan
[**update_tracking_plan**](TrackingPlansApi.md#update_tracking_plan) | **PATCH** /tracking-plans/{trackingPlanId} | Update Tracking Plan



## Operation: add_source_to_tracking_plan

> AddSourceToTrackingPlan200Response add_source_to_tracking_plan(tracking_plan_id, add_source_to_tracking_plan_v1_input)

Add Source to Tracking Plan

Connects a Source to a Tracking Plan.    • When called, this endpoint may generate the `Source Modified` event in the [audit trail](/tag/Audit-Trail).   • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_source_to_tracking_plan200_response import AddSourceToTrackingPlan200Response
from segment_public_api.models.add_source_to_tracking_plan_v1_input import AddSourceToTrackingPlanV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    add_source_to_tracking_plan_v1_input = {"sourceId":"qQEHquLrjRDN9j1ByrChyn"} # AddSourceToTrackingPlanV1Input | 

    try:
        # Add Source to Tracking Plan
        api_response = api_instance.add_source_to_tracking_plan(tracking_plan_id, add_source_to_tracking_plan_v1_input)
        print("The response of TrackingPlansApi->add_source_to_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->add_source_to_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **add_source_to_tracking_plan_v1_input** | [**AddSourceToTrackingPlanV1Input**](AddSourceToTrackingPlanV1Input.md)|  | 

### Return type

[**AddSourceToTrackingPlan200Response**](AddSourceToTrackingPlan200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: create_tracking_plan

> CreateTrackingPlan200Response create_tracking_plan(create_tracking_plan_v1_input)

Create Tracking Plan

Creates a Tracking Plan.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_tracking_plan200_response import CreateTrackingPlan200Response
from segment_public_api.models.create_tracking_plan_v1_input import CreateTrackingPlanV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    create_tracking_plan_v1_input = {"name":"New TP","type":"LIVE"} # CreateTrackingPlanV1Input | 

    try:
        # Create Tracking Plan
        api_response = api_instance.create_tracking_plan(create_tracking_plan_v1_input)
        print("The response of TrackingPlansApi->create_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->create_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tracking_plan_v1_input** | [**CreateTrackingPlanV1Input**](CreateTrackingPlanV1Input.md)|  | 

### Return type

[**CreateTrackingPlan200Response**](CreateTrackingPlan200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_tracking_plan

> DeleteTrackingPlan200Response delete_tracking_plan(tracking_plan_id)

Delete Tracking Plan

Deletes a Tracking Plan.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_tracking_plan200_response import DeleteTrackingPlan200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 

    try:
        # Delete Tracking Plan
        api_response = api_instance.delete_tracking_plan(tracking_plan_id)
        print("The response of TrackingPlansApi->delete_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->delete_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 

### Return type

[**DeleteTrackingPlan200Response**](DeleteTrackingPlan200Response.md)

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


## Operation: get_tracking_plan

> GetTrackingPlan200Response get_tracking_plan(tracking_plan_id)

Get Tracking Plan

Returns a Tracking Plan.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_tracking_plan200_response import GetTrackingPlan200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 

    try:
        # Get Tracking Plan
        api_response = api_instance.get_tracking_plan(tracking_plan_id)
        print("The response of TrackingPlansApi->get_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->get_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 

### Return type

[**GetTrackingPlan200Response**](GetTrackingPlan200Response.md)

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


## Operation: list_rules_from_tracking_plan

> ListRulesFromTrackingPlan200Response list_rules_from_tracking_plan(tracking_plan_id, pagination)

List Rules from Tracking Plan

Lists Tracking Plan rules.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 200 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_rules_from_tracking_plan200_response import ListRulesFromTrackingPlan200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    pagination = segment_public_api.PaginationInput() # PaginationInput | Pagination options.  This parameter exists in v1.

    try:
        # List Rules from Tracking Plan
        api_response = api_instance.list_rules_from_tracking_plan(tracking_plan_id, pagination)
        print("The response of TrackingPlansApi->list_rules_from_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->list_rules_from_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination options.  This parameter exists in v1. | 

### Return type

[**ListRulesFromTrackingPlan200Response**](ListRulesFromTrackingPlan200Response.md)

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


## Operation: list_sources_from_tracking_plan

> ListSourcesFromTrackingPlan200Response list_sources_from_tracking_plan(tracking_plan_id, pagination)

List Sources from Tracking Plan

Lists Sources connected to a Tracking Plan.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.   This endpoint requires the user to have at least the following permission(s):   * Source Read-only  * Tracking Plan Read-only

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_sources_from_tracking_plan200_response import ListSourcesFromTrackingPlan200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    pagination = segment_public_api.PaginationInput() # PaginationInput | Pagination options.  This parameter exists in v1.

    try:
        # List Sources from Tracking Plan
        api_response = api_instance.list_sources_from_tracking_plan(tracking_plan_id, pagination)
        print("The response of TrackingPlansApi->list_sources_from_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->list_sources_from_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination options.  This parameter exists in v1. | 

### Return type

[**ListSourcesFromTrackingPlan200Response**](ListSourcesFromTrackingPlan200Response.md)

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


## Operation: list_tracking_plans

> ListTrackingPlans200Response list_tracking_plans(pagination, type=type)

List Tracking Plans

Returns a list of Tracking Plans.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_tracking_plans200_response import ListTrackingPlans200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    pagination = segment_public_api.PaginationInput() # PaginationInput | Pagination options.  This parameter exists in v1.
    type = 'LIVE' # str | Requests Tracking Plans of a certain type. If omitted, lists all types.  This parameter exists in v1. (optional)

    try:
        # List Tracking Plans
        api_response = api_instance.list_tracking_plans(pagination, type=type)
        print("The response of TrackingPlansApi->list_tracking_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->list_tracking_plans: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination options.  This parameter exists in v1. | 
 **type** | **str**| Requests Tracking Plans of a certain type. If omitted, lists all types.  This parameter exists in v1. | [optional] 

### Return type

[**ListTrackingPlans200Response**](ListTrackingPlans200Response.md)

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


## Operation: remove_rules_from_tracking_plan

> RemoveRulesFromTrackingPlan200Response remove_rules_from_tracking_plan(tracking_plan_id, rules)

Remove Rules from Tracking Plan

Deletes Tracking Plan rules.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_rule_v1 import RemoveRuleV1
from segment_public_api.models.remove_rules_from_tracking_plan200_response import RemoveRulesFromTrackingPlan200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    rules = [segment_public_api.RemoveRuleV1()] # List[RemoveRuleV1] | Rules to delete.  This parameter exists in v1.

    try:
        # Remove Rules from Tracking Plan
        api_response = api_instance.remove_rules_from_tracking_plan(tracking_plan_id, rules)
        print("The response of TrackingPlansApi->remove_rules_from_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->remove_rules_from_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **rules** | [**List[RemoveRuleV1]**](RemoveRuleV1.md)| Rules to delete.  This parameter exists in v1. | 

### Return type

[**RemoveRulesFromTrackingPlan200Response**](RemoveRulesFromTrackingPlan200Response.md)

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


## Operation: remove_source_from_tracking_plan

> RemoveSourceFromTrackingPlan200Response remove_source_from_tracking_plan(tracking_plan_id, source_id)

Remove Source from Tracking Plan

Disconnects a Source from a Tracking Plan.    • When called, this endpoint may generate the `Source Modified` event in the [audit trail](/tag/Audit-Trail).   • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_source_from_tracking_plan200_response import RemoveSourceFromTrackingPlan200Response
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    source_id = 'qQEHquLrjRDN9j1ByrChyn' # str | The id of the Source associated with the Tracking Plan.  Config API note: analogous to `sourceName`.  This parameter exists in v1.

    try:
        # Remove Source from Tracking Plan
        api_response = api_instance.remove_source_from_tracking_plan(tracking_plan_id, source_id)
        print("The response of TrackingPlansApi->remove_source_from_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->remove_source_from_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **source_id** | **str**| The id of the Source associated with the Tracking Plan.  Config API note: analogous to &#x60;sourceName&#x60;.  This parameter exists in v1. | 

### Return type

[**RemoveSourceFromTrackingPlan200Response**](RemoveSourceFromTrackingPlan200Response.md)

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


## Operation: replace_rules_in_tracking_plan

> ReplaceRulesInTrackingPlan200Response replace_rules_in_tracking_plan(tracking_plan_id, replace_rules_in_tracking_plan_v1_input)

Replace Rules in Tracking Plan

Replaces Tracking Plan rules.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_rules_in_tracking_plan200_response import ReplaceRulesInTrackingPlan200Response
from segment_public_api.models.replace_rules_in_tracking_plan_v1_input import ReplaceRulesInTrackingPlanV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    replace_rules_in_tracking_plan_v1_input = {"rules":[{"key":"New Replaced Rule","type":"TRACK","version":1,"jsonSchema":{}}]} # ReplaceRulesInTrackingPlanV1Input | 

    try:
        # Replace Rules in Tracking Plan
        api_response = api_instance.replace_rules_in_tracking_plan(tracking_plan_id, replace_rules_in_tracking_plan_v1_input)
        print("The response of TrackingPlansApi->replace_rules_in_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->replace_rules_in_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **replace_rules_in_tracking_plan_v1_input** | [**ReplaceRulesInTrackingPlanV1Input**](ReplaceRulesInTrackingPlanV1Input.md)|  | 

### Return type

[**ReplaceRulesInTrackingPlan200Response**](ReplaceRulesInTrackingPlan200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_rules_in_tracking_plan

> UpdateRulesInTrackingPlan200Response update_rules_in_tracking_plan(tracking_plan_id, update_rules_in_tracking_plan_v1_input)

Update Rules in Tracking Plan

Updates Tracking Plan rules.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_rules_in_tracking_plan200_response import UpdateRulesInTrackingPlan200Response
from segment_public_api.models.update_rules_in_tracking_plan_v1_input import UpdateRulesInTrackingPlanV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    update_rules_in_tracking_plan_v1_input = {"rules":[{"key":"New Rule","type":"TRACK","version":1,"jsonSchema":{}}]} # UpdateRulesInTrackingPlanV1Input | 

    try:
        # Update Rules in Tracking Plan
        api_response = api_instance.update_rules_in_tracking_plan(tracking_plan_id, update_rules_in_tracking_plan_v1_input)
        print("The response of TrackingPlansApi->update_rules_in_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->update_rules_in_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **update_rules_in_tracking_plan_v1_input** | [**UpdateRulesInTrackingPlanV1Input**](UpdateRulesInTrackingPlanV1Input.md)|  | 

### Return type

[**UpdateRulesInTrackingPlan200Response**](UpdateRulesInTrackingPlan200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_tracking_plan

> UpdateTrackingPlan200Response update_tracking_plan(tracking_plan_id, update_tracking_plan_v1_input)

Update Tracking Plan

Updates a Tracking Plan.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.  Config API omitted fields: - `updateMask`       

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_tracking_plan200_response import UpdateTrackingPlan200Response
from segment_public_api.models.update_tracking_plan_v1_input import UpdateTrackingPlanV1Input
from segment_public_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.segmentapis.com
# See configuration.py for a list of all supported configuration parameters.
configuration = segment_public_api.Configuration(
    host = "https://api.segmentapis.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TrackingPlansApi(api_client)
    tracking_plan_id = 'tp_sprout_rVGCC6WdrNxjCf6JpCHP' # str | 
    update_tracking_plan_v1_input = {"name":"Updated TP"} # UpdateTrackingPlanV1Input | 

    try:
        # Update Tracking Plan
        api_response = api_instance.update_tracking_plan(tracking_plan_id, update_tracking_plan_v1_input)
        print("The response of TrackingPlansApi->update_tracking_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingPlansApi->update_tracking_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_plan_id** | **str**|  | 
 **update_tracking_plan_v1_input** | [**UpdateTrackingPlanV1Input**](UpdateTrackingPlanV1Input.md)|  | 

### Return type

[**UpdateTrackingPlan200Response**](UpdateTrackingPlan200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

