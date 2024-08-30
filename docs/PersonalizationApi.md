# segment_public_api.PersonalizationApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_personalization_data**](PersonalizationApi.md#get_personalization_data) | **GET** /personalization/v1/spaces/{spaceId}/{entityType}/{entityIdentifier} | Get Personalization Data



## Operation: get_personalization_data

> GetPersonalizationData200Response get_personalization_data(space_id, entity_type, entity_identifier, children_entity_type=children_entity_type)

Get Personalization Data

Get Personalization Data.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Entities feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_personalization_data200_response import GetPersonalizationData200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.PersonalizationApi(api_client)
    space_id = 'spaceId' # str | 
    entity_type = 'profile' # str | 
    entity_identifier = 'identifier' # str | 
    children_entity_type = 'children_entity_type_example' # str | Child entity type.  This parameter exists in alpha. (optional)

    try:
        # Get Personalization Data
        api_response = api_instance.get_personalization_data(space_id, entity_type, entity_identifier, children_entity_type=children_entity_type)
        print("The response of PersonalizationApi->get_personalization_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalizationApi->get_personalization_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **entity_type** | **str**|  | 
 **entity_identifier** | **str**|  | 
 **children_entity_type** | **str**| Child entity type.  This parameter exists in alpha. | [optional] 

### Return type

[**GetPersonalizationData200Response**](GetPersonalizationData200Response.md)

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

