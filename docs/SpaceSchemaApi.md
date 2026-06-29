# segment_public_api.SpaceSchemaApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_entity_paths**](SpaceSchemaApi.md#list_entity_paths) | **GET** /spaces/{spaceId}/entity-paths | List Entity Paths
[**list_events**](SpaceSchemaApi.md#list_events) | **GET** /spaces/{spaceId}/events | List Events
[**list_properties_from_entity**](SpaceSchemaApi.md#list_properties_from_entity) | **GET** /spaces/{spaceId}/entities/{entitySlug}/properties | List Properties from Entity
[**list_properties_from_event**](SpaceSchemaApi.md#list_properties_from_event) | **GET** /spaces/{spaceId}/events/{eventName}/properties | List Properties from Event
[**list_sample_values_from_entity_property**](SpaceSchemaApi.md#list_sample_values_from_entity_property) | **GET** /spaces/{spaceId}/entities/{entitySlug}/properties/{propertyName}/sample-values | List Sample Values from Entity Property
[**list_sample_values_from_event_property**](SpaceSchemaApi.md#list_sample_values_from_event_property) | **GET** /spaces/{spaceId}/events/{eventName}/properties/{propertyName}/sample-values | List Sample Values from Event Property
[**list_sample_values_from_trait**](SpaceSchemaApi.md#list_sample_values_from_trait) | **GET** /spaces/{spaceId}/traits/{traitKey}/sample-values | List Sample Values from Trait
[**list_traits**](SpaceSchemaApi.md#list_traits) | **GET** /spaces/{spaceId}/traits | List Traits



## Operation: list_entity_paths

> ListEntityPaths200Response list_entity_paths(space_id, pagination=pagination, search=search)

List Entity Paths

Returns a list of Entity Paths for a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_entity_paths200_response import ListEntityPaths200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    search = 'search_example' # str | Filter paths by entity name or path name.  This parameter exists in alpha. (optional)

    try:
        # List Entity Paths
        api_response = api_instance.list_entity_paths(space_id, pagination=pagination, search=search)
        print("The response of SpaceSchemaApi->list_entity_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_entity_paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **search** | **str**| Filter paths by entity name or path name.  This parameter exists in alpha. | [optional] 

### Return type

[**ListEntityPaths200Response**](ListEntityPaths200Response.md)

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


## Operation: list_events

> ListEvents200Response list_events(space_id, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search)

List Events

Returns a list of Events for a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_events200_response import ListEvents200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    sort_by = 'lastSeenAt' # str | Field to sort by. Defaults to 'lastSeenAt'.  This parameter exists in alpha. (optional)
    sort_dir = 'desc' # str | Sort direction. Defaults to 'desc'.  This parameter exists in alpha. (optional)
    search = 'search_example' # str | Filter events by name substring.  This parameter exists in alpha. (optional)

    try:
        # List Events
        api_response = api_instance.list_events(space_id, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search)
        print("The response of SpaceSchemaApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **sort_by** | **str**| Field to sort by. Defaults to &#39;lastSeenAt&#39;.  This parameter exists in alpha. | [optional] 
 **sort_dir** | **str**| Sort direction. Defaults to &#39;desc&#39;.  This parameter exists in alpha. | [optional] 
 **search** | **str**| Filter events by name substring.  This parameter exists in alpha. | [optional] 

### Return type

[**ListEvents200Response**](ListEvents200Response.md)

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


## Operation: list_properties_from_entity

> ListPropertiesFromEntity200Response list_properties_from_entity(space_id, entity_slug, pagination=pagination, include_sample_values=include_sample_values, samples_count=samples_count)

List Properties from Entity

Returns a list of Properties for an Entity in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.  <div style=\"background-color: #e8f4fd; border: 1px solid #90caf9; border-radius: 6px; padding: 16px; margin: 16px 0; color: #0d47a1; line-height: 1.5;\">   <ul style=\"margin: 0; padding-left: 20px; font-size: 13px;\">     <li style=\"margin-bottom: 6px;\"><strong>Forward-only pagination</strong>: this endpoint does not support backward traversal. The <code>pagination.previous</code> field is always absent; use <code>pagination.next</code> to advance through pages.</li>   </ul> </div>    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_properties_from_entity200_response import ListPropertiesFromEntity200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    entity_slug = 'my-entity' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    include_sample_values = True # bool | When true, include sample values for each property. Defaults to false.  This parameter exists in alpha. (optional)
    samples_count = 3.4 # float | Max number of sample values to return per property. Defaults to 20, min 1, max 100.  This parameter exists in alpha. (optional)

    try:
        # List Properties from Entity
        api_response = api_instance.list_properties_from_entity(space_id, entity_slug, pagination=pagination, include_sample_values=include_sample_values, samples_count=samples_count)
        print("The response of SpaceSchemaApi->list_properties_from_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_properties_from_entity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **entity_slug** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **include_sample_values** | **bool**| When true, include sample values for each property. Defaults to false.  This parameter exists in alpha. | [optional] 
 **samples_count** | **float**| Max number of sample values to return per property. Defaults to 20, min 1, max 100.  This parameter exists in alpha. | [optional] 

### Return type

[**ListPropertiesFromEntity200Response**](ListPropertiesFromEntity200Response.md)

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


## Operation: list_properties_from_event

> ListPropertiesFromEvent200Response list_properties_from_event(space_id, event_name, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search, include_sample_values=include_sample_values, samples_count=samples_count)

List Properties from Event

Returns a list of Properties for an Event in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_properties_from_event200_response import ListPropertiesFromEvent200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    event_name = 'Order Completed' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    sort_by = 'name' # str | Field to sort by. Defaults to 'lastSeenAt'.  This parameter exists in alpha. (optional)
    sort_dir = 'asc' # str | Sort direction. Defaults to 'desc'.  This parameter exists in alpha. (optional)
    search = 'search_example' # str | Filter properties by name substring.  This parameter exists in alpha. (optional)
    include_sample_values = True # bool | When true, include sample values for each property. Defaults to false.  This parameter exists in alpha. (optional)
    samples_count = 3.4 # float | Max number of sample values to return per property. Defaults to 20, min 1, max 100.  This parameter exists in alpha. (optional)

    try:
        # List Properties from Event
        api_response = api_instance.list_properties_from_event(space_id, event_name, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search, include_sample_values=include_sample_values, samples_count=samples_count)
        print("The response of SpaceSchemaApi->list_properties_from_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_properties_from_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **event_name** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **sort_by** | **str**| Field to sort by. Defaults to &#39;lastSeenAt&#39;.  This parameter exists in alpha. | [optional] 
 **sort_dir** | **str**| Sort direction. Defaults to &#39;desc&#39;.  This parameter exists in alpha. | [optional] 
 **search** | **str**| Filter properties by name substring.  This parameter exists in alpha. | [optional] 
 **include_sample_values** | **bool**| When true, include sample values for each property. Defaults to false.  This parameter exists in alpha. | [optional] 
 **samples_count** | **float**| Max number of sample values to return per property. Defaults to 20, min 1, max 100.  This parameter exists in alpha. | [optional] 

### Return type

[**ListPropertiesFromEvent200Response**](ListPropertiesFromEvent200Response.md)

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


## Operation: list_sample_values_from_entity_property

> ListSampleValuesFromEntityProperty200Response list_sample_values_from_entity_property(space_id, entity_slug, property_name)

List Sample Values from Entity Property

Returns sample values for an Entity Property in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_sample_values_from_entity_property200_response import ListSampleValuesFromEntityProperty200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    entity_slug = 'my-entity' # str | 
    property_name = 'email' # str | 

    try:
        # List Sample Values from Entity Property
        api_response = api_instance.list_sample_values_from_entity_property(space_id, entity_slug, property_name)
        print("The response of SpaceSchemaApi->list_sample_values_from_entity_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_sample_values_from_entity_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **entity_slug** | **str**|  | 
 **property_name** | **str**|  | 

### Return type

[**ListSampleValuesFromEntityProperty200Response**](ListSampleValuesFromEntityProperty200Response.md)

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


## Operation: list_sample_values_from_event_property

> ListSampleValuesFromEventProperty200Response list_sample_values_from_event_property(space_id, event_name, property_name, property_type)

List Sample Values from Event Property

Returns sample values for an Event Property in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.event_property_type import EventPropertyType
from segment_public_api.models.list_sample_values_from_event_property200_response import ListSampleValuesFromEventProperty200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    event_name = 'Order Completed' # str | 
    property_name = 'revenue' # str | 
    property_type = segment_public_api.EventPropertyType() # EventPropertyType | The property type.  This parameter exists in alpha.

    try:
        # List Sample Values from Event Property
        api_response = api_instance.list_sample_values_from_event_property(space_id, event_name, property_name, property_type)
        print("The response of SpaceSchemaApi->list_sample_values_from_event_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_sample_values_from_event_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **event_name** | **str**|  | 
 **property_name** | **str**|  | 
 **property_type** | [**EventPropertyType**](.md)| The property type.  This parameter exists in alpha. | 

### Return type

[**ListSampleValuesFromEventProperty200Response**](ListSampleValuesFromEventProperty200Response.md)

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


## Operation: list_sample_values_from_trait

> ListSampleValuesFromTrait200Response list_sample_values_from_trait(space_id, trait_key, collection=collection)

List Sample Values from Trait

Returns sample values for a Trait in a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_sample_values_from_trait200_response import ListSampleValuesFromTrait200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    trait_key = 'email' # str | 
    collection = 'collection_example' # str | Collection to get trait values for. Defaults to 'users'.  This parameter exists in alpha. (optional)

    try:
        # List Sample Values from Trait
        api_response = api_instance.list_sample_values_from_trait(space_id, trait_key, collection=collection)
        print("The response of SpaceSchemaApi->list_sample_values_from_trait:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_sample_values_from_trait: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **trait_key** | **str**|  | 
 **collection** | **str**| Collection to get trait values for. Defaults to &#39;users&#39;.  This parameter exists in alpha. | [optional] 

### Return type

[**ListSampleValuesFromTrait200Response**](ListSampleValuesFromTrait200Response.md)

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


## Operation: list_traits

> ListTraits200Response list_traits(space_id, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search, collection=collection, include_sample_values=include_sample_values, samples_count=samples_count)

List Traits

Returns a list of Traits for a Space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.  <div style=\"background-color: #e8f4fd; border: 1px solid #90caf9; border-radius: 6px; padding: 16px; margin: 16px 0; color: #0d47a1; line-height: 1.5;\">   <ul style=\"margin: 0; padding-left: 20px; font-size: 13px;\">     <li style=\"margin-bottom: 6px;\"><strong>Forward-only pagination</strong>: this endpoint does not support backward traversal. The <code>pagination.previous</code> field is always absent; use <code>pagination.next</code> to advance through pages.</li>     <li style=\"margin-bottom: 6px;\"><strong>Deduplication guarantee</strong>: when sorting by <code>lastSeenAt</code>, results are fully deduplicated for Spaces with up to 2,500 traits. For Spaces with more than 2,500 traits, duplicate trait entries may appear across pages due to an internal pagination tradeoff. Sorting by <code>trait</code> is not affected.</li>   </ul> </div>    The rate limit for this endpoint is 25 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_traits200_response import ListTraits200Response
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
    api_instance = segment_public_api.SpaceSchemaApi(api_client)
    space_id = 'spaceId' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination params. Defaults to count 200.  This parameter exists in alpha. (optional)
    sort_by = 'trait' # str | Field to sort by. Defaults to 'trait'.  This parameter exists in alpha. (optional)
    sort_dir = 'asc' # str | Sort direction. Defaults to 'asc'.  This parameter exists in alpha. (optional)
    search = 'search_example' # str | Filter traits by key substring.  This parameter exists in alpha. (optional)
    collection = 'collection_example' # str | Collection to list traits for. Defaults to 'users'.  This parameter exists in alpha. (optional)
    include_sample_values = True # bool | When true, include sample values for each trait. Defaults to false.  This parameter exists in alpha. (optional)
    samples_count = 3.4 # float | Max number of sample values to return per trait. Defaults to 20, min 1, max 100.  This parameter exists in alpha. (optional)

    try:
        # List Traits
        api_response = api_instance.list_traits(space_id, pagination=pagination, sort_by=sort_by, sort_dir=sort_dir, search=search, collection=collection, include_sample_values=include_sample_values, samples_count=samples_count)
        print("The response of SpaceSchemaApi->list_traits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpaceSchemaApi->list_traits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination params. Defaults to count 200.  This parameter exists in alpha. | [optional] 
 **sort_by** | **str**| Field to sort by. Defaults to &#39;trait&#39;.  This parameter exists in alpha. | [optional] 
 **sort_dir** | **str**| Sort direction. Defaults to &#39;asc&#39;.  This parameter exists in alpha. | [optional] 
 **search** | **str**| Filter traits by key substring.  This parameter exists in alpha. | [optional] 
 **collection** | **str**| Collection to list traits for. Defaults to &#39;users&#39;.  This parameter exists in alpha. | [optional] 
 **include_sample_values** | **bool**| When true, include sample values for each trait. Defaults to false.  This parameter exists in alpha. | [optional] 
 **samples_count** | **float**| Max number of sample values to return per trait. Defaults to 20, min 1, max 100.  This parameter exists in alpha. | [optional] 

### Return type

[**ListTraits200Response**](ListTraits200Response.md)

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

