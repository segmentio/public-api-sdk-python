# segment_public_api.ComputedTraitsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_computed_trait**](ComputedTraitsApi.md#create_computed_trait) | **POST** /spaces/{spaceId}/computed-traits | Create Computed Trait
[**get_computed_trait**](ComputedTraitsApi.md#get_computed_trait) | **GET** /spaces/{spaceId}/computed-traits/{id} | Get Computed Trait
[**list_computed_traits**](ComputedTraitsApi.md#list_computed_traits) | **GET** /spaces/{spaceId}/computed-traits | List Computed Traits
[**remove_computed_trait_from_space**](ComputedTraitsApi.md#remove_computed_trait_from_space) | **DELETE** /spaces/{spaceId}/computed-traits/{id} | Remove Computed Trait from Space
[**update_computed_trait_for_space**](ComputedTraitsApi.md#update_computed_trait_for_space) | **PATCH** /spaces/{spaceId}/computed-traits/{id} | Update Computed Trait for Space



## Operation: create_computed_trait

> CreateComputedTrait200Response create_computed_trait(space_id, create_trait_alpha_input)

Create Computed Trait

Creates a Computed Trait  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Computed Trait feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_computed_trait200_response import CreateComputedTrait200Response
from segment_public_api.models.create_trait_alpha_input import CreateTraitAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ComputedTraitsApi(api_client)
    space_id = 'spaceId' # str | 
    create_trait_alpha_input = {"name":"name","description":"description","definition":{"query":"event('Shoes Bought').count() >= 1","type":"users"}} # CreateTraitAlphaInput | 

    try:
        # Create Computed Trait
        api_response = api_instance.create_computed_trait(space_id, create_trait_alpha_input)
        print("The response of ComputedTraitsApi->create_computed_trait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputedTraitsApi->create_computed_trait: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_trait_alpha_input** | [**CreateTraitAlphaInput**](CreateTraitAlphaInput.md)|  | 

### Return type

[**CreateComputedTrait200Response**](CreateComputedTrait200Response.md)

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


## Operation: get_computed_trait

> CreateComputedTrait200Response get_computed_trait(space_id, id)

Get Computed Trait

Returns the Computed Trait by id and spaceId  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Computed Trait feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 100 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_computed_trait200_response import CreateComputedTrait200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ComputedTraitsApi(api_client)
    space_id = 'spaceId' # str | 
    id = 'id' # str | 

    try:
        # Get Computed Trait
        api_response = api_instance.get_computed_trait(space_id, id)
        print("The response of ComputedTraitsApi->get_computed_trait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputedTraitsApi->get_computed_trait: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**CreateComputedTrait200Response**](CreateComputedTrait200Response.md)

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


## Operation: list_computed_traits

> ListComputedTraits200Response list_computed_traits(space_id, pagination)

List Computed Traits

Returns Computed Traits by spaceId.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Computed Trait feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_computed_traits200_response import ListComputedTraits200Response
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
    api_instance = segment_public_api.ComputedTraitsApi(api_client)
    space_id = 'spaceId' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Information about the pagination of this response.  This parameter exists in alpha.

    try:
        # List Computed Traits
        api_response = api_instance.list_computed_traits(space_id, pagination)
        print("The response of ComputedTraitsApi->list_computed_traits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputedTraitsApi->list_computed_traits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Information about the pagination of this response.  This parameter exists in alpha. | 

### Return type

[**ListComputedTraits200Response**](ListComputedTraits200Response.md)

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


## Operation: remove_computed_trait_from_space

> RemoveComputedTraitFromSpace200Response remove_computed_trait_from_space(space_id, id)

Remove Computed Trait from Space

Deletes a Computed Trait by id and spaceId.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Computed Trait feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Computed Trait Deleted` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 20 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_computed_trait_from_space200_response import RemoveComputedTraitFromSpace200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ComputedTraitsApi(api_client)
    space_id = 'spaceId' # str | 
    id = 'id' # str | 

    try:
        # Remove Computed Trait from Space
        api_response = api_instance.remove_computed_trait_from_space(space_id, id)
        print("The response of ComputedTraitsApi->remove_computed_trait_from_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputedTraitsApi->remove_computed_trait_from_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RemoveComputedTraitFromSpace200Response**](RemoveComputedTraitFromSpace200Response.md)

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


## Operation: update_computed_trait_for_space

> UpdateComputedTraitForSpace200Response update_computed_trait_for_space(space_id, id, update_computed_trait_for_space_alpha_input)

Update Computed Trait for Space

Updates the enabled status for a computed trait.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Computed Trait feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Computed Trait Modified` event in the [audit trail](/tag/Audit-Trail).  • Note that when a Computed Trait is updated, the Computed Trait will be locked from future edits until the changes have been incorporated. You can find more information [in the Segment docs](https://segment-docs.netlify.app/docs/unify/traits/computed-traits/#editing-realtime-traits).   The rate limit for this endpoint is 10 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_computed_trait_for_space200_response import UpdateComputedTraitForSpace200Response
from segment_public_api.models.update_computed_trait_for_space_alpha_input import UpdateComputedTraitForSpaceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ComputedTraitsApi(api_client)
    space_id = 'spaceId' # str | 
    id = 'id' # str | 
    update_computed_trait_for_space_alpha_input = {"enabled":false} # UpdateComputedTraitForSpaceAlphaInput | 

    try:
        # Update Computed Trait for Space
        api_response = api_instance.update_computed_trait_for_space(space_id, id, update_computed_trait_for_space_alpha_input)
        print("The response of ComputedTraitsApi->update_computed_trait_for_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputedTraitsApi->update_computed_trait_for_space: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **id** | **str**|  | 
 **update_computed_trait_for_space_alpha_input** | [**UpdateComputedTraitForSpaceAlphaInput**](UpdateComputedTraitForSpaceAlphaInput.md)|  | 

### Return type

[**UpdateComputedTraitForSpace200Response**](UpdateComputedTraitForSpace200Response.md)

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

