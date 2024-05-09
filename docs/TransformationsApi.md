# segment_public_api.TransformationsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transformation**](TransformationsApi.md#create_transformation) | **POST** /transformations | Create Transformation
[**delete_transformation**](TransformationsApi.md#delete_transformation) | **DELETE** /transformations/{transformationId} | Delete Transformation
[**get_transformation**](TransformationsApi.md#get_transformation) | **GET** /transformations/{transformationId} | Get Transformation
[**list_transformations**](TransformationsApi.md#list_transformations) | **GET** /transformations | List Transformations
[**update_transformation**](TransformationsApi.md#update_transformation) | **PATCH** /transformations/{transformationId} | Update Transformation



## Operation: create_transformation

> CreateTransformation200Response create_transformation(create_transformation_v1_input)

Create Transformation

Creates a new Transformation.    • When called, this endpoint may generate the `Transformation Created` event in the [audit trail](/tag/Audit-Trail).   • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_transformation200_response import CreateTransformation200Response
from segment_public_api.models.create_transformation_v1_input import CreateTransformationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TransformationsApi(api_client)
    create_transformation_v1_input = {"name":"Name of the new transformation","sourceId":"qQEHquLrjRDN9j1ByrChyn","enabled":true,"newEventName":"new-event-name","propertyRenames":[{"oldName":"old-name","newName":"new-name"},{"oldName":"another-name-old","newName":"another-name-new"}],"propertyValueTransformations":[{"propertyPaths":["properties.some-property","context.some-property"],"propertyValue":"some property value"}],"if":"event = 'Example Event V1'"} # CreateTransformationV1Input | 

    try:
        # Create Transformation
        api_response = api_instance.create_transformation(create_transformation_v1_input)
        print("The response of TransformationsApi->create_transformation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformationsApi->create_transformation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transformation_v1_input** | [**CreateTransformationV1Input**](CreateTransformationV1Input.md)|  | 

### Return type

[**CreateTransformation200Response**](CreateTransformation200Response.md)

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


## Operation: delete_transformation

> DeleteTransformation200Response delete_transformation(transformation_id)

Delete Transformation

Deletes a Transformation.    • When called, this endpoint may generate the `Transformation Deleted` event in the [audit trail](/tag/Audit-Trail).   • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_transformation200_response import DeleteTransformation200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TransformationsApi(api_client)
    transformation_id = '2c0vVuRdDmJ3UQkVjd5WxaA3dar' # str | 

    try:
        # Delete Transformation
        api_response = api_instance.delete_transformation(transformation_id)
        print("The response of TransformationsApi->delete_transformation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformationsApi->delete_transformation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transformation_id** | **str**|  | 

### Return type

[**DeleteTransformation200Response**](DeleteTransformation200Response.md)

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


## Operation: get_transformation

> GetTransformation200Response get_transformation(transformation_id)

Get Transformation

Gets a Transformation.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_transformation200_response import GetTransformation200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TransformationsApi(api_client)
    transformation_id = 'pHrD51Ds35Zjfka84yXQE6' # str | 

    try:
        # Get Transformation
        api_response = api_instance.get_transformation(transformation_id)
        print("The response of TransformationsApi->get_transformation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformationsApi->get_transformation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transformation_id** | **str**|  | 

### Return type

[**GetTransformation200Response**](GetTransformation200Response.md)

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


## Operation: list_transformations

> ListTransformations200Response list_transformations(pagination=pagination)

List Transformations

Lists all Transformations in the Workspace.    • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_transformations200_response import ListTransformations200Response
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
    api_instance = segment_public_api.TransformationsApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination options.  This parameter exists in v1. (optional)

    try:
        # List Transformations
        api_response = api_instance.list_transformations(pagination=pagination)
        print("The response of TransformationsApi->list_transformations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformationsApi->list_transformations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination options.  This parameter exists in v1. | [optional] 

### Return type

[**ListTransformations200Response**](ListTransformations200Response.md)

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


## Operation: update_transformation

> UpdateTransformation200Response update_transformation(transformation_id, update_transformation_v1_input)

Update Transformation

Updates an existing Transformation.    • When called, this endpoint may generate the `Transformation Updated` event in the [audit trail](/tag/Audit-Trail).   • In order to successfully call this endpoint, the specified Workspace needs to have the Protocols feature enabled. Please reach out to your customer success manager for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_transformation200_response import UpdateTransformation200Response
from segment_public_api.models.update_transformation_v1_input import UpdateTransformationV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.TransformationsApi(api_client)
    transformation_id = 'pHrD51Ds35Zjfka84yXQE6' # str | 
    update_transformation_v1_input = {"name":"updated-name","sourceId":"rh5BDZp6QDHvXFCkibm1pR","enabled":true,"destinationMetadataId":"547610a5db31d978f14a5c4e","if":"event=\"my-event\"","newEventName":"my-updated-event","propertyRenames":[{"newName":"new-property","oldName":"old-property"}],"propertyValueTransformations":[{"propertyPaths":["properties.another-property"],"propertyValue":"another property value"}]} # UpdateTransformationV1Input | 

    try:
        # Update Transformation
        api_response = api_instance.update_transformation(transformation_id, update_transformation_v1_input)
        print("The response of TransformationsApi->update_transformation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransformationsApi->update_transformation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transformation_id** | **str**|  | 
 **update_transformation_v1_input** | [**UpdateTransformationV1Input**](UpdateTransformationV1Input.md)|  | 

### Return type

[**UpdateTransformation200Response**](UpdateTransformation200Response.md)

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

