# segment_public_api.IAMUsersApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permissions_to_user**](IAMUsersApi.md#add_permissions_to_user) | **POST** /users/{userId}/permissions | Add Permissions to User
[**create_invites**](IAMUsersApi.md#create_invites) | **POST** /invites | Create Invites
[**delete_invites**](IAMUsersApi.md#delete_invites) | **DELETE** /invites | Delete Invites
[**delete_users**](IAMUsersApi.md#delete_users) | **DELETE** /users | Delete Users
[**get_user**](IAMUsersApi.md#get_user) | **GET** /users/{userId} | Get User
[**list_invites**](IAMUsersApi.md#list_invites) | **GET** /invites | List Invites
[**list_user_groups_from_user**](IAMUsersApi.md#list_user_groups_from_user) | **GET** /users/{userId}/groups | List User Groups from User
[**list_users**](IAMUsersApi.md#list_users) | **GET** /users | List Users
[**replace_permissions_for_user**](IAMUsersApi.md#replace_permissions_for_user) | **PUT** /users/{userId}/permissions | Replace Permissions for User



## Operation: add_permissions_to_user

> AddPermissionsToUser200Response add_permissions_to_user(user_id, add_permissions_to_user_v1_input)

Add Permissions to User

Adds a list of access permissions to a user.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Policy Created * User Policy Updated          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_permissions_to_user200_response import AddPermissionsToUser200Response
from segment_public_api.models.add_permissions_to_user_v1_input import AddPermissionsToUserV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMUsersApi(api_client)
    user_id = 'sgJDWk3K21k6LE3tLU9nRK' # str | 
    add_permissions_to_user_v1_input = {"permissions":[{"roleId":"1WDUuRLxv84rrfCNUwvkrRtkxnS","resources":[{"id":"9aQ1Lj62S4bomZKLF4DPqW","type":"WORKSPACE"}]}]} # AddPermissionsToUserV1Input | 

    try:
        # Add Permissions to User
        api_response = api_instance.add_permissions_to_user(user_id, add_permissions_to_user_v1_input)
        print("The response of IAMUsersApi->add_permissions_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->add_permissions_to_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **add_permissions_to_user_v1_input** | [**AddPermissionsToUserV1Input**](AddPermissionsToUserV1Input.md)|  | 

### Return type

[**AddPermissionsToUser200Response**](AddPermissionsToUser200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: create_invites

> CreateInvites200Response create_invites(create_invites_v1_input)

Create Invites

Invites a list of users to join a Workspace.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Non-Segment User Invited to Workspace * Policy Created * New Segment User Invited to Workspace  Config API omitted fields: - `parent`          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_invites200_response import CreateInvites200Response
from segment_public_api.models.create_invites_v1_input import CreateInvitesV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMUsersApi(api_client)
    create_invites_v1_input = {"invites":[{"email":"foo@example.com","permissions":[{"roleId":"1WDUuRLxv84rrfCNUwvkrRtkxnS","resources":[{"id":"9aQ1Lj62S4bomZKLF4DPqW","type":"WORKSPACE"}]}]}]} # CreateInvitesV1Input | 

    try:
        # Create Invites
        api_response = api_instance.create_invites(create_invites_v1_input)
        print("The response of IAMUsersApi->create_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->create_invites: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invites_v1_input** | [**CreateInvitesV1Input**](CreateInvitesV1Input.md)|  | 

### Return type

[**CreateInvites200Response**](CreateInvites200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_invites

> DeleteInvites200Response delete_invites(emails)

Delete Invites

Removes a list of invitations to join a Workspace.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Invite Deleted * Group Memberships Deleted          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_invites200_response import DeleteInvites200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMUsersApi(api_client)
    emails = ['[\"foo@example.com\"]'] # List[str] | The list of emails to delete invites for.  This parameter exists in v1.

    try:
        # Delete Invites
        api_response = api_instance.delete_invites(emails)
        print("The response of IAMUsersApi->delete_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->delete_invites: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emails** | [**List[str]**](str.md)| The list of emails to delete invites for.  This parameter exists in v1. | 

### Return type

[**DeleteInvites200Response**](DeleteInvites200Response.md)

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


## Operation: delete_users

> DeleteUsers200Response delete_users(user_ids)

Delete Users

Removes one or multiple users.    • When called, this endpoint may generate the `Group Memberships Deleted` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_users200_response import DeleteUsers200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMUsersApi(api_client)
    user_ids = ['[\"dLPzv57d5nRGz8U5iegLKp\"]'] # List[str] | The ids of the users to remove.  This parameter exists in v1.

    try:
        # Delete Users
        api_response = api_instance.delete_users(user_ids)
        print("The response of IAMUsersApi->delete_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->delete_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ids** | [**List[str]**](str.md)| The ids of the users to remove.  This parameter exists in v1. | 

### Return type

[**DeleteUsers200Response**](DeleteUsers200Response.md)

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


## Operation: get_user

> GetUser200Response get_user(user_id)

Get User

Returns a user given their id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_user200_response import GetUser200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMUsersApi(api_client)
    user_id = 'sgJDWk3K21k6LE3tLU9nRK' # str | 

    try:
        # Get User
        api_response = api_instance.get_user(user_id)
        print("The response of IAMUsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**GetUser200Response**](GetUser200Response.md)

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


## Operation: list_invites

> ListInvites200Response list_invites(pagination)

List Invites

Returns a list of invitations to join a Workspace.  Config API omitted fields: - `parent` 

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_invites200_response import ListInvites200Response
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
    api_instance = segment_public_api.IAMUsersApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1.

    try:
        # List Invites
        api_response = api_instance.list_invites(pagination)
        print("The response of IAMUsersApi->list_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->list_invites: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | 

### Return type

[**ListInvites200Response**](ListInvites200Response.md)

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


## Operation: list_user_groups_from_user

> ListUserGroupsFromUser200Response list_user_groups_from_user(user_id, pagination)

List User Groups from User

Returns all groups a user belongs to.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_user_groups_from_user200_response import ListUserGroupsFromUser200Response
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
    api_instance = segment_public_api.IAMUsersApi(api_client)
    user_id = 'sgJDWk3K21k6LE3tLU9nRK' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination for groups.  This parameter exists in v1.

    try:
        # List User Groups from User
        api_response = api_instance.list_user_groups_from_user(user_id, pagination)
        print("The response of IAMUsersApi->list_user_groups_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->list_user_groups_from_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination for groups.  This parameter exists in v1. | 

### Return type

[**ListUserGroupsFromUser200Response**](ListUserGroupsFromUser200Response.md)

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


## Operation: list_users

> ListUsers200Response list_users(pagination)

List Users

Returns a list of users with access to the Workspace.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_users200_response import ListUsers200Response
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
    api_instance = segment_public_api.IAMUsersApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination for users.  This parameter exists in v1.

    try:
        # List Users
        api_response = api_instance.list_users(pagination)
        print("The response of IAMUsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->list_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination for users.  This parameter exists in v1. | 

### Return type

[**ListUsers200Response**](ListUsers200Response.md)

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


## Operation: replace_permissions_for_user

> ReplacePermissionsForUser200Response replace_permissions_for_user(user_id, replace_permissions_for_user_v1_input)

Replace Permissions for User

Updates the list of access permissions for a user.    • When called, this endpoint may generate the `Policy Deleted` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_permissions_for_user200_response import ReplacePermissionsForUser200Response
from segment_public_api.models.replace_permissions_for_user_v1_input import ReplacePermissionsForUserV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMUsersApi(api_client)
    user_id = 'sgJDWk3K21k6LE3tLU9nRK' # str | 
    replace_permissions_for_user_v1_input = {"permissions":[{"roleId":"1WDUuRLxv84rrfCNUwvkrRtkxnS","resources":[{"id":"9aQ1Lj62S4bomZKLF4DPqW","type":"WORKSPACE"}]}]} # ReplacePermissionsForUserV1Input | 

    try:
        # Replace Permissions for User
        api_response = api_instance.replace_permissions_for_user(user_id, replace_permissions_for_user_v1_input)
        print("The response of IAMUsersApi->replace_permissions_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMUsersApi->replace_permissions_for_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **replace_permissions_for_user_v1_input** | [**ReplacePermissionsForUserV1Input**](ReplacePermissionsForUserV1Input.md)|  | 

### Return type

[**ReplacePermissionsForUser200Response**](ReplacePermissionsForUser200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json
 - **Accept**: application/vnd.segment.v1+json, application/json, application/vnd.segment.v1beta+json, application/vnd.segment.v1alpha+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

