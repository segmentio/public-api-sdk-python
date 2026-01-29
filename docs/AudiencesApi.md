# segment_public_api.AudiencesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_audience_schedule_to_audience**](AudiencesApi.md#add_audience_schedule_to_audience) | **POST** /spaces/{spaceId}/audiences/{id}/schedules | Add Audience Schedule to Audience
[**create_audience**](AudiencesApi.md#create_audience) | **POST** /spaces/{spaceId}/audiences | Create Audience
[**create_audience_preview**](AudiencesApi.md#create_audience_preview) | **POST** /spaces/{spaceId}/audiences/previews | Create Audience Preview
[**force_execute_audience_run**](AudiencesApi.md#force_execute_audience_run) | **POST** /spaces/{spaceId}/audiences/{audienceId}/runs | Force Execute Audience Run
[**get_audience**](AudiencesApi.md#get_audience) | **GET** /spaces/{spaceId}/audiences/{id} | Get Audience
[**get_audience_preview**](AudiencesApi.md#get_audience_preview) | **GET** /spaces/{spaceId}/audiences/previews/{id} | Get Audience Preview
[**get_audience_schedule_from_space_and_audience**](AudiencesApi.md#get_audience_schedule_from_space_and_audience) | **GET** /spaces/{spaceId}/audiences/{id}/schedules/{scheduleId} | Get Audience Schedule from Space And Audience
[**list_audience_consumers_from_space_and_audience**](AudiencesApi.md#list_audience_consumers_from_space_and_audience) | **GET** /spaces/{spaceId}/audiences/{id}/audience-references | List Audience Consumers from Space And Audience
[**list_audience_schedules_from_space_and_audience**](AudiencesApi.md#list_audience_schedules_from_space_and_audience) | **GET** /spaces/{spaceId}/audiences/{id}/schedules | List Audience Schedules from Space And Audience
[**list_audiences**](AudiencesApi.md#list_audiences) | **GET** /spaces/{spaceId}/audiences | List Audiences
[**remove_audience_from_space**](AudiencesApi.md#remove_audience_from_space) | **DELETE** /spaces/{spaceId}/audiences/{id} | Remove Audience from Space
[**remove_audience_schedule_from_audience**](AudiencesApi.md#remove_audience_schedule_from_audience) | **DELETE** /spaces/{spaceId}/audiences/{id}/schedules/{scheduleId} | Remove Audience Schedule from Audience
[**update_audience_for_space**](AudiencesApi.md#update_audience_for_space) | **PATCH** /spaces/{spaceId}/audiences/{id} | Update Audience for Space
[**update_audience_schedule_for_audience**](AudiencesApi.md#update_audience_schedule_for_audience) | **PATCH** /spaces/{spaceId}/audiences/{id}/schedules/{scheduleId} | Update Audience Schedule for Audience



## Operation: add_audience_schedule_to_audience

> AddAudienceScheduleToAudience200Response add_audience_schedule_to_audience(space_id, id, add_audience_schedule_to_audience_alpha_input)

Add Audience Schedule to Audience

The ability to configure the run schedule for an Audience is limited to Linked Audiences (audienceType = LINKED).  Note that if a Linked Audience remains disabled for 90 days Segment will delete the associated schedule and a new schedule will need to be created.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_audience_schedule_to_audience200_response import AddAudienceScheduleToAudience200Response
from segment_public_api.models.add_audience_schedule_to_audience_alpha_input import AddAudienceScheduleToAudienceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    add_audience_schedule_to_audience_alpha_input = {"strategy":"SPECIFIC_DAYS","config":{"days":[1,3,5],"hours":[9,17],"timezone":"America/New_York"}} # AddAudienceScheduleToAudienceAlphaInput | 

    try:
        # Add Audience Schedule to Audience
        api_response = api_instance.add_audience_schedule_to_audience(space_id, id, add_audience_schedule_to_audience_alpha_input)
        print("The response of AudiencesApi->add_audience_schedule_to_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->add_audience_schedule_to_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **add_audience_schedule_to_audience_alpha_input** | [**AddAudienceScheduleToAudienceAlphaInput**](AddAudienceScheduleToAudienceAlphaInput.md)|  | 

### Return type

[**AddAudienceScheduleToAudience200Response**](AddAudienceScheduleToAudience200Response.md)

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


## Operation: create_audience

> CreateAudience200Response create_audience(space_id, create_audience_input)

Create Audience

Creates Audience.  • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Created` event in the [audit trail](/tag/Audit-Trail).  Note: The definition for an Audience created using the API is not editable through the Segment App.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_audience200_response import CreateAudience200Response
from segment_public_api.models.create_audience_input import CreateAudienceInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    create_audience_input = {"name":"Profiles Audience V1","description":"Test profiles audience v1 example","enabled":true,"audienceType":"USERS","definition":{"query":"event('Purchased').count() >= 1"},"options":{"includeHistoricalData":true}} # CreateAudienceInput | 

    try:
        # Create Audience
        api_response = api_instance.create_audience(space_id, create_audience_input)
        print("The response of AudiencesApi->create_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->create_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_audience_input** | [**CreateAudienceInput**](CreateAudienceInput.md)|  | 

### Return type

[**CreateAudience200Response**](CreateAudience200Response.md)

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


## Operation: create_audience_preview

> CreateAudiencePreview200Response create_audience_preview(space_id, create_audience_preview_beta_input)

Create Audience Preview

Previews Audience.  • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Preview Created` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 5 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information. This endpoint also has a rate limit of 700 requests per month per spaceId, which is lower than the default due to access pattern restrictions.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_audience_preview200_response import CreateAudiencePreview200Response
from segment_public_api.models.create_audience_preview_beta_input import CreateAudiencePreviewBetaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    create_audience_preview_beta_input = {"definition":{"query":"entity('owned-accounts').count() >= 1","targetEntity":"owned-accounts"},"audienceType":"LINKED","options":{"filterByExternalIds":["android.idfa","anonymous_id","email","ios.idfa","user_id"]}} # CreateAudiencePreviewBetaInput | 

    try:
        # Create Audience Preview
        api_response = api_instance.create_audience_preview(space_id, create_audience_preview_beta_input)
        print("The response of AudiencesApi->create_audience_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->create_audience_preview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_audience_preview_beta_input** | [**CreateAudiencePreviewBetaInput**](CreateAudiencePreviewBetaInput.md)|  | 

### Return type

[**CreateAudiencePreview200Response**](CreateAudiencePreview200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: force_execute_audience_run

> ForceExecuteAudienceRun200Response force_execute_audience_run(space_id, audience_id)

Force Execute Audience Run

The ability to force execute a run for an Audience is limited to Linked Audiences (audienceType = `LINKED`).  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Run Forced` event in the [audit trail](/tag/Audit-Trail).

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.force_execute_audience_run200_response import ForceExecuteAudienceRun200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 

    try:
        # Force Execute Audience Run
        api_response = api_instance.force_execute_audience_run(space_id, audience_id)
        print("The response of AudiencesApi->force_execute_audience_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->force_execute_audience_run: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 

### Return type

[**ForceExecuteAudienceRun200Response**](ForceExecuteAudienceRun200Response.md)

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


## Operation: get_audience

> GetAudience200Response get_audience(space_id, id, include=include)

Get Audience

Returns the Audience by id and spaceId. Supports including audience schedules using `?include=schedules`.  • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 100 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_audience200_response import GetAudience200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    include = 'include_example' # str | Additional resource to include, support schedules only.  This parameter exists in alpha. (optional)

    try:
        # Get Audience
        api_response = api_instance.get_audience(space_id, id, include=include)
        print("The response of AudiencesApi->get_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **include** | **str**| Additional resource to include, support schedules only.  This parameter exists in alpha. | [optional] 

### Return type

[**GetAudience200Response**](GetAudience200Response.md)

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


## Operation: get_audience_preview

> GetAudiencePreview200Response get_audience_preview(space_id, id)

Get Audience Preview

Reads the results of an audience preview.  • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 300 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_audience_preview200_response import GetAudiencePreview200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = '31XR7mRsdw3vz3ZqvRa1623re0q-compute_preview_execution-9aQ1Lj62S4bomZKLF4DPqW-compute_preview_execution' # str | 

    try:
        # Get Audience Preview
        api_response = api_instance.get_audience_preview(space_id, id)
        print("The response of AudiencesApi->get_audience_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audience_preview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetAudiencePreview200Response**](GetAudiencePreview200Response.md)

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


## Operation: get_audience_schedule_from_space_and_audience

> GetAudienceScheduleFromSpaceAndAudience200Response get_audience_schedule_from_space_and_audience(space_id, id, schedule_id)

Get Audience Schedule from Space And Audience

Returns the schedule for the given audience and scheduleId.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_audience_schedule_from_space_and_audience200_response import GetAudienceScheduleFromSpaceAndAudience200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    schedule_id = 'sch_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 

    try:
        # Get Audience Schedule from Space And Audience
        api_response = api_instance.get_audience_schedule_from_space_and_audience(space_id, id, schedule_id)
        print("The response of AudiencesApi->get_audience_schedule_from_space_and_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->get_audience_schedule_from_space_and_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **schedule_id** | **str**|  | 

### Return type

[**GetAudienceScheduleFromSpaceAndAudience200Response**](GetAudienceScheduleFromSpaceAndAudience200Response.md)

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


## Operation: list_audience_consumers_from_space_and_audience

> ListAudienceConsumersFromSpaceAndAudience200Response list_audience_consumers_from_space_and_audience(space_id, id, pagination=pagination, search=search, sort=sort)

List Audience Consumers from Space And Audience

Returns the list of consumers for the given audience.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_audience_consumers_from_space_and_audience200_response import ListAudienceConsumersFromSpaceAndAudience200Response
from segment_public_api.models.list_audience_consumers_sort_input import ListAudienceConsumersSortInput
from segment_public_api.models.list_audience_search_input import ListAudienceSearchInput
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
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsswThIGTUYm2K8FjOOfXtY1K' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Information about the pagination of this response.  [See pagination](https://docs.segmentapis.com/tag/Pagination/#section/Pagination-parameters) for more info.  This parameter exists in alpha. (optional)
    search = segment_public_api.ListAudienceSearchInput() # ListAudienceSearchInput | Optional search criteria  This parameter exists in alpha. (optional)
    sort = segment_public_api.ListAudienceConsumersSortInput() # ListAudienceConsumersSortInput | Optional sort criteria  This parameter exists in alpha. (optional)

    try:
        # List Audience Consumers from Space And Audience
        api_response = api_instance.list_audience_consumers_from_space_and_audience(space_id, id, pagination=pagination, search=search, sort=sort)
        print("The response of AudiencesApi->list_audience_consumers_from_space_and_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_audience_consumers_from_space_and_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Information about the pagination of this response.  [See pagination](https://docs.segmentapis.com/tag/Pagination/#section/Pagination-parameters) for more info.  This parameter exists in alpha. | [optional] 
 **search** | [**ListAudienceSearchInput**](.md)| Optional search criteria  This parameter exists in alpha. | [optional] 
 **sort** | [**ListAudienceConsumersSortInput**](.md)| Optional sort criteria  This parameter exists in alpha. | [optional] 

### Return type

[**ListAudienceConsumersFromSpaceAndAudience200Response**](ListAudienceConsumersFromSpaceAndAudience200Response.md)

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


## Operation: list_audience_schedules_from_space_and_audience

> ListAudienceSchedulesFromSpaceAndAudience200Response list_audience_schedules_from_space_and_audience(space_id, id)

List Audience Schedules from Space And Audience

Returns the list of schedules for the given audience.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_audience_schedules_from_space_and_audience200_response import ListAudienceSchedulesFromSpaceAndAudience200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 

    try:
        # List Audience Schedules from Space And Audience
        api_response = api_instance.list_audience_schedules_from_space_and_audience(space_id, id)
        print("The response of AudiencesApi->list_audience_schedules_from_space_and_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_audience_schedules_from_space_and_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**ListAudienceSchedulesFromSpaceAndAudience200Response**](ListAudienceSchedulesFromSpaceAndAudience200Response.md)

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


## Operation: list_audiences

> ListAudiences200Response list_audiences(space_id, search=search, pagination=pagination, include=include)

List Audiences

Returns Audiences by spaceId. Supports including audience schedules using `?include=schedules`.  • This endpoint is in **Beta** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_audience_search_input import ListAudienceSearchInput
from segment_public_api.models.list_audiences200_response import ListAudiences200Response
from segment_public_api.models.list_audiences_pagination_input import ListAudiencesPaginationInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    search = segment_public_api.ListAudienceSearchInput() # ListAudienceSearchInput | Optional search criteria  This parameter exists in alpha. (optional)
    pagination = segment_public_api.ListAudiencesPaginationInput() # ListAudiencesPaginationInput | Information about the pagination of this response.  [See pagination](https://docs.segmentapis.com/tag/Pagination/#section/Pagination-parameters) for more info.  This parameter exists in alpha. (optional)
    include = 'include_example' # str | Additional resource to include, support schedules only.  This parameter exists in alpha. (optional)

    try:
        # List Audiences
        api_response = api_instance.list_audiences(space_id, search=search, pagination=pagination, include=include)
        print("The response of AudiencesApi->list_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_audiences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **search** | [**ListAudienceSearchInput**](.md)| Optional search criteria  This parameter exists in alpha. | [optional] 
 **pagination** | [**ListAudiencesPaginationInput**](.md)| Information about the pagination of this response.  [See pagination](https://docs.segmentapis.com/tag/Pagination/#section/Pagination-parameters) for more info.  This parameter exists in alpha. | [optional] 
 **include** | **str**| Additional resource to include, support schedules only.  This parameter exists in alpha. | [optional] 

### Return type

[**ListAudiences200Response**](ListAudiences200Response.md)

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


## Operation: remove_audience_from_space

> RemoveAudienceFromSpace200Response remove_audience_from_space(space_id, id)

Remove Audience from Space

Deletes an Audience by id and spaceId.  • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Deleted` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_audience_from_space200_response import RemoveAudienceFromSpace200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 

    try:
        # Remove Audience from Space
        api_response = api_instance.remove_audience_from_space(space_id, id)
        print("The response of AudiencesApi->remove_audience_from_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->remove_audience_from_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RemoveAudienceFromSpace200Response**](RemoveAudienceFromSpace200Response.md)

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


## Operation: remove_audience_schedule_from_audience

> RemoveAudienceScheduleFromAudience200Response remove_audience_schedule_from_audience(space_id, id, schedule_id)

Remove Audience Schedule from Audience

Deletes an audience schedule for a Linked Audience (audienceType = LINKED).  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_audience_schedule_from_audience200_response import RemoveAudienceScheduleFromAudience200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    schedule_id = 'sch_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 

    try:
        # Remove Audience Schedule from Audience
        api_response = api_instance.remove_audience_schedule_from_audience(space_id, id, schedule_id)
        print("The response of AudiencesApi->remove_audience_schedule_from_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->remove_audience_schedule_from_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **schedule_id** | **str**|  | 

### Return type

[**RemoveAudienceScheduleFromAudience200Response**](RemoveAudienceScheduleFromAudience200Response.md)

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


## Operation: update_audience_for_space

> UpdateAudienceForSpace200Response update_audience_for_space(space_id, id, update_audience_for_space_input)

Update Audience for Space

Updates the Audience.  • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Modified` event in the [audit trail](/tag/Audit-Trail).  • Note that when an Audience is updated, the Audience will be locked from future edits until the changes have been incorporated. You can find more information [in the Segment docs](https://segment-docs.netlify.app/docs/engage/audiences/#editing-realtime-audiences-and-traits).  Note: The definition for an Audience updated using the API is not editable through the Segment App.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_audience_for_space200_response import UpdateAudienceForSpace200Response
from segment_public_api.models.update_audience_for_space_input import UpdateAudienceForSpaceInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    update_audience_for_space_input = {"name":"Profiles Audience V1 Updated","description":"Updated V1 description","enabled":true,"definition":{"query":"event('Purchased').count() >= 3"},"options":{"includeHistoricalData":false,"filterByExternalIds":["user_id","email"]}} # UpdateAudienceForSpaceInput | 

    try:
        # Update Audience for Space
        api_response = api_instance.update_audience_for_space(space_id, id, update_audience_for_space_input)
        print("The response of AudiencesApi->update_audience_for_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->update_audience_for_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **update_audience_for_space_input** | [**UpdateAudienceForSpaceInput**](UpdateAudienceForSpaceInput.md)|  | 

### Return type

[**UpdateAudienceForSpace200Response**](UpdateAudienceForSpace200Response.md)

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


## Operation: update_audience_schedule_for_audience

> UpdateAudienceScheduleForAudience200Response update_audience_schedule_for_audience(space_id, id, schedule_id, update_audience_schedule_for_audience_alpha_input)

Update Audience Schedule for Audience

Updates an audience schedule for a Linked Audience (audienceType = LINKED).  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_audience_schedule_for_audience200_response import UpdateAudienceScheduleForAudience200Response
from segment_public_api.models.update_audience_schedule_for_audience_alpha_input import UpdateAudienceScheduleForAudienceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.AudiencesApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    schedule_id = 'sch_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    update_audience_schedule_for_audience_alpha_input = {"strategy":"SPECIFIC_DAYS","config":{"days":[1,3,4],"hours":[9,16],"timezone":"America/New_York"}} # UpdateAudienceScheduleForAudienceAlphaInput | 

    try:
        # Update Audience Schedule for Audience
        api_response = api_instance.update_audience_schedule_for_audience(space_id, id, schedule_id, update_audience_schedule_for_audience_alpha_input)
        print("The response of AudiencesApi->update_audience_schedule_for_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->update_audience_schedule_for_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **schedule_id** | **str**|  | 
 **update_audience_schedule_for_audience_alpha_input** | [**UpdateAudienceScheduleForAudienceAlphaInput**](UpdateAudienceScheduleForAudienceAlphaInput.md)|  | 

### Return type

[**UpdateAudienceScheduleForAudience200Response**](UpdateAudienceScheduleForAudience200Response.md)

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

