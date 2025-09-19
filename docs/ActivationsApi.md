# segment_public_api.ActivationsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_activation_to_audience**](ActivationsApi.md#add_activation_to_audience) | **POST** /spaces/{spaceId}/audiences/{audienceId}/destination-connections/{connectionId}/activations | Add Activation to Audience
[**add_destination_to_audience**](ActivationsApi.md#add_destination_to_audience) | **POST** /spaces/{spaceId}/audiences/{audienceId}/destination-connections | Add Destination to Audience
[**get_activation_from_audience**](ActivationsApi.md#get_activation_from_audience) | **GET** /spaces/{spaceId}/audiences/{audienceId}/activations/{id} | Get Activation from Audience
[**list_activations_from_audience**](ActivationsApi.md#list_activations_from_audience) | **GET** /spaces/{spaceId}/audiences/{audienceId}/activations | List Activations from Audience
[**list_destinations_from_audience**](ActivationsApi.md#list_destinations_from_audience) | **GET** /spaces/{spaceId}/audiences/{audienceId}/destination-connections | List Destinations from Audience
[**remove_activation_from_audience**](ActivationsApi.md#remove_activation_from_audience) | **DELETE** /spaces/{spaceId}/audiences/{audienceId}/activations/{id} | Remove Activation from Audience
[**update_activation_for_audience**](ActivationsApi.md#update_activation_for_audience) | **PATCH** /spaces/{spaceId}/audiences/{audienceId}/activations/{id} | Update Activation for Audience



## Operation: add_activation_to_audience

> AddActivationToAudience200Response add_activation_to_audience(space_id, audience_id, connection_id, add_activation_to_audience_alpha_input)

Add Activation to Audience

Creates Activation.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Activation Created` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_activation_to_audience200_response import AddActivationToAudience200Response
from segment_public_api.models.add_activation_to_audience_alpha_input import AddActivationToAudienceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    connection_id = 'ii_123456789' # str | 
    add_activation_to_audience_alpha_input = {"activationType":"Audience Entered","activationName":"Test Activation","enabled":true,"performResync":true,"personalization":{"profile":{"properties":["mountain_bikers_2023","game_boy_color_owners"],"mapping":{"mountain_bikers_2023":"bikers_segment","game_boy_color_owners":"retro_gamers"}},"entities":[{"properties":["ID","LAST_ACTIVITY_TIME","BALANCE"],"relationshipSlug":"owned-accounts-copy"}]},"destinationMapping":{"actionId":"action_123","settings":{"webhookUrl":"https://example.com/webhook","method":"POST"}}} # AddActivationToAudienceAlphaInput | 

    try:
        # Add Activation to Audience
        api_response = api_instance.add_activation_to_audience(space_id, audience_id, connection_id, add_activation_to_audience_alpha_input)
        print("The response of ActivationsApi->add_activation_to_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->add_activation_to_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **connection_id** | **str**|  | 
 **add_activation_to_audience_alpha_input** | [**AddActivationToAudienceAlphaInput**](AddActivationToAudienceAlphaInput.md)|  | 

### Return type

[**AddActivationToAudience200Response**](AddActivationToAudience200Response.md)

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


## Operation: add_destination_to_audience

> AddDestinationToAudience200Response add_destination_to_audience(space_id, audience_id, add_destination_to_audience_alpha_input)

Add Destination to Audience

Adds a Destination to an Audience.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Destination Added into Audience` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_destination_to_audience200_response import AddDestinationToAudience200Response
from segment_public_api.models.add_destination_to_audience_alpha_input import AddDestinationToAudienceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    add_destination_to_audience_alpha_input = {"destination":{"id":"684758860892086596310ac","type":"destination"}} # AddDestinationToAudienceAlphaInput | 

    try:
        # Add Destination to Audience
        api_response = api_instance.add_destination_to_audience(space_id, audience_id, add_destination_to_audience_alpha_input)
        print("The response of ActivationsApi->add_destination_to_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->add_destination_to_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **add_destination_to_audience_alpha_input** | [**AddDestinationToAudienceAlphaInput**](AddDestinationToAudienceAlphaInput.md)|  | 

### Return type

[**AddDestinationToAudience200Response**](AddDestinationToAudience200Response.md)

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


## Operation: get_activation_from_audience

> GetActivationFromAudience200Response get_activation_from_audience(space_id, audience_id, id)

Get Activation from Audience

Gets a single Activation by id.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_activation_from_audience200_response import GetActivationFromAudience200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    id = 'act_987654321' # str | 

    try:
        # Get Activation from Audience
        api_response = api_instance.get_activation_from_audience(space_id, audience_id, id)
        print("The response of ActivationsApi->get_activation_from_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->get_activation_from_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**GetActivationFromAudience200Response**](GetActivationFromAudience200Response.md)

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


## Operation: list_activations_from_audience

> ListActivationsFromAudience200Response list_activations_from_audience(space_id, audience_id, pagination=pagination)

List Activations from Audience

Lists all Activations.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_activations_from_audience200_response import ListActivationsFromAudience200Response
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
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Optional pagination.  This parameter exists in alpha. (optional)

    try:
        # List Activations from Audience
        api_response = api_instance.list_activations_from_audience(space_id, audience_id, pagination=pagination)
        print("The response of ActivationsApi->list_activations_from_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->list_activations_from_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Optional pagination.  This parameter exists in alpha. | [optional] 

### Return type

[**ListActivationsFromAudience200Response**](ListActivationsFromAudience200Response.md)

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


## Operation: list_destinations_from_audience

> ListDestinationsFromAudience200Response list_destinations_from_audience(space_id, audience_id, pagination=pagination)

List Destinations from Audience

Lists all Destinations from an Audience.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Audience feature enabled. Please reach out to your customer success manager for more information.  • When called, this endpoint may generate the `Destinations Listed from Audience` event in the [audit trail](/tag/Audit-Trail).   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_destinations_from_audience200_response import ListDestinationsFromAudience200Response
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
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Optional pagination.  This parameter exists in alpha. (optional)

    try:
        # List Destinations from Audience
        api_response = api_instance.list_destinations_from_audience(space_id, audience_id, pagination=pagination)
        print("The response of ActivationsApi->list_destinations_from_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->list_destinations_from_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Optional pagination.  This parameter exists in alpha. | [optional] 

### Return type

[**ListDestinationsFromAudience200Response**](ListDestinationsFromAudience200Response.md)

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


## Operation: remove_activation_from_audience

> RemoveActivationFromAudience200Response remove_activation_from_audience(space_id, audience_id, id)

Remove Activation from Audience

Deletes an Activation.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_activation_from_audience200_response import RemoveActivationFromAudience200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    id = 'act_987654321' # str | 

    try:
        # Remove Activation from Audience
        api_response = api_instance.remove_activation_from_audience(space_id, audience_id, id)
        print("The response of ActivationsApi->remove_activation_from_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->remove_activation_from_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RemoveActivationFromAudience200Response**](RemoveActivationFromAudience200Response.md)

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


## Operation: update_activation_for_audience

> UpdateActivationForAudience200Response update_activation_for_audience(space_id, audience_id, id, update_activation_for_audience_alpha_input)

Update Activation for Audience

Updates an Activation.   The rate limit for this endpoint is 50 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_activation_for_audience200_response import UpdateActivationForAudience200Response
from segment_public_api.models.update_activation_for_audience_alpha_input import UpdateActivationForAudienceAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.ActivationsApi(api_client)
    space_id = 'spa_9aQ1Lj62S4bomZKLF4DPqW' # str | 
    audience_id = 'aud_0ujsszwN8NRY24YaXiTIE2VWDTS' # str | 
    id = 'act_987654321' # str | 
    update_activation_for_audience_alpha_input = {"activationName":"Updated Test Activation","enabled":false,"performResync":false,"personalization":{"profile":{"properties":["updated_mountain_bikers_2023","updated_game_boy_color_owners"],"mapping":{"updated_mountain_bikers_2023":"updated_bikers","updated_game_boy_color_owners":"updated_gamers"}},"entities":[{"properties":["ID","UPDATED_BALANCE"],"relationshipSlug":"owned-accounts-updated"}]},"destinationMapping":{"actionId":"action_456","settings":{"webhookUrl":"https://example.com/updated-webhook","method":"PUT"}}} # UpdateActivationForAudienceAlphaInput | 

    try:
        # Update Activation for Audience
        api_response = api_instance.update_activation_for_audience(space_id, audience_id, id, update_activation_for_audience_alpha_input)
        print("The response of ActivationsApi->update_activation_for_audience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivationsApi->update_activation_for_audience: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **audience_id** | **str**|  | 
 **id** | **str**|  | 
 **update_activation_for_audience_alpha_input** | [**UpdateActivationForAudienceAlphaInput**](UpdateActivationForAudienceAlphaInput.md)|  | 

### Return type

[**UpdateActivationForAudience200Response**](UpdateActivationForAudience200Response.md)

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

