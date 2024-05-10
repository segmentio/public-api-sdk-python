# segment_public_api.IAMRolesApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_roles**](IAMRolesApi.md#list_roles) | **GET** /roles | List Roles



## Operation: list_roles

> ListRoles200Response list_roles(pagination=pagination)

List Roles

Returns a list of Roles available to apply to permissions for users and/or groups.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_roles200_response import ListRoles200Response
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
    api_instance = segment_public_api.IAMRolesApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination for roles.  This parameter exists in v1. (optional)

    try:
        # List Roles
        api_response = api_instance.list_roles(pagination=pagination)
        print("The response of IAMRolesApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMRolesApi->list_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination for roles.  This parameter exists in v1. | [optional] 

### Return type

[**ListRoles200Response**](ListRoles200Response.md)

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

