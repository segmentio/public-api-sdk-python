# segment_public_api.AudiencesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audience**](AudiencesApi.md#create_audience) | **POST** /spaces/{spaceId}/audiences | Create Audience
[**get_audience**](AudiencesApi.md#get_audience) | **GET** /spaces/{spaceId}/audiences/{id} | Get Audience
[**list_audiences**](AudiencesApi.md#list_audiences) | **GET** /spaces/{spaceId}/audiences | List Audiences
[**remove_audience_from_space**](AudiencesApi.md#remove_audience_from_space) | **DELETE** /spaces/{spaceId}/audiences/{id} | Remove Audience from Space
[**update_audience_for_space**](AudiencesApi.md#update_audience_for_space) | **PATCH** /spaces/{spaceId}/audiences/{id} | Update Audience for Space



## Operation: create_audience

> CreateAudience200Response create_audience(space_id, create_audience_alpha_input)

Create Audience

Creates Audience.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Created` event in the [audit trail](/tag/Audit-Trail).  Note: The definition for an Audience created via the API is not editable via the Segment App.   The rate limit for this endpoint is 10 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_audience200_response import CreateAudience200Response
from segment_public_api.models.create_audience_alpha_input import CreateAudienceAlphaInput
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
    space_id = 'spaceId' # str | 
    create_audience_alpha_input = {"name":"name","description":"description","definition":{"query":"event('Shoes Bought').count() >= 1","type":"users"}} # CreateAudienceAlphaInput | 

    try:
        # Create Audience
        api_response = api_instance.create_audience(space_id, create_audience_alpha_input)
        print("The response of AudiencesApi->create_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->create_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_audience_alpha_input** | [**CreateAudienceAlphaInput**](CreateAudienceAlphaInput.md)|  | 

### Return type

[**CreateAudience200Response**](CreateAudience200Response.md)

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


## Operation: get_audience

> GetAudience200Response get_audience(space_id, id)

Get Audience

Returns the Audience by id and spaceId.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 100 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

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
    space_id = 'spaceId' # str | 
    id = 'id' # str | 

    try:
        # Get Audience
        api_response = api_instance.get_audience(space_id, id)
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

### Return type

[**GetAudience200Response**](GetAudience200Response.md)

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

> ListAudiences200Response list_audiences(space_id, pagination)

List Audiences

Returns Audiences by spaceId.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_audiences200_response import ListAudiences200Response
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
    space_id = 'spaceId' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Information about the pagination of this response.  [See pagination](https://docs.segmentapis.com/tag/Pagination/#section/Pagination-parameters) for more info.  This parameter exists in alpha.

    try:
        # List Audiences
        api_response = api_instance.list_audiences(space_id, pagination)
        print("The response of AudiencesApi->list_audiences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AudiencesApi->list_audiences: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Information about the pagination of this response.  [See pagination](https://docs.segmentapis.com/tag/Pagination/#section/Pagination-parameters) for more info.  This parameter exists in alpha. | 

### Return type

[**ListAudiences200Response**](ListAudiences200Response.md)

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


## Operation: remove_audience_from_space

> RemoveAudienceFromSpace200Response remove_audience_from_space(space_id, id)

Remove Audience from Space

Deletes an Audience by id and spaceId.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Deleted` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 20 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

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
    space_id = 'spaceId' # str | 
    id = 'id' # str | 

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

Updates the enabled status for an audience  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Audience Modified` event in the [audit trail](/tag/Audit-Trail).  • Note that when an Audience is updated, the Audience will be locked from future edits until the changes have been incorporated. You can find more information [in the Segment docs](https://segment-docs.netlify.app/docs/engage/audiences/#editing-realtime-audiences-and-traits).  Note: The definition for an Audience updated via the API is not editable via the Segment App.   The rate limit for this endpoint is 10 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

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
    space_id = 'spaceId' # str | 
    id = 'id' # str | 
    update_audience_for_space_input = {"enabled":false} # UpdateAudienceForSpaceInput | 

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

