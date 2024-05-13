# segment_public_api.IAMGroupsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permissions_to_user_group**](IAMGroupsApi.md#add_permissions_to_user_group) | **POST** /groups/{userGroupId}/permissions | Add Permissions to User Group
[**add_users_to_user_group**](IAMGroupsApi.md#add_users_to_user_group) | **POST** /groups/{userGroupId}/users | Add Users to User Group
[**create_user_group**](IAMGroupsApi.md#create_user_group) | **POST** /groups | Create User Group
[**delete_user_group**](IAMGroupsApi.md#delete_user_group) | **DELETE** /groups/{userGroupId} | Delete User Group
[**get_user_group**](IAMGroupsApi.md#get_user_group) | **GET** /groups/{userGroupId} | Get User Group
[**list_invites_from_user_group**](IAMGroupsApi.md#list_invites_from_user_group) | **GET** /groups/{userGroupId}/invites | List Invites from User Group
[**list_user_groups**](IAMGroupsApi.md#list_user_groups) | **GET** /groups | List User Groups
[**list_users_from_user_group**](IAMGroupsApi.md#list_users_from_user_group) | **GET** /groups/{userGroupId}/users | List Users from User Group
[**remove_users_from_user_group**](IAMGroupsApi.md#remove_users_from_user_group) | **DELETE** /group/{userGroupId}/users | Remove Users from User Group
[**replace_permissions_for_user_group**](IAMGroupsApi.md#replace_permissions_for_user_group) | **PUT** /groups/{userGroupId}/permissions | Replace Permissions for User Group
[**replace_users_in_user_group**](IAMGroupsApi.md#replace_users_in_user_group) | **PUT** /group/{userGroupId}/users | Replace Users in User Group
[**update_user_group**](IAMGroupsApi.md#update_user_group) | **PATCH** /groups/{userGroupId} | Update User Group



## Operation: add_permissions_to_user_group

> AddPermissionsToUserGroup200Response add_permissions_to_user_group(user_group_id, add_permissions_to_user_group_v1_input)

Add Permissions to User Group

Adds a list of access permissions to a user group.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Policy Created * User Group Policy Updated          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_permissions_to_user_group200_response import AddPermissionsToUserGroup200Response
from segment_public_api.models.add_permissions_to_user_group_v1_input import AddPermissionsToUserGroupV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    add_permissions_to_user_group_v1_input = {"permissions":[{"roleId":"1WDUuRLxv84rrfCNUwvkrRtkxnS","resources":[{"id":"9aQ1Lj62S4bomZKLF4DPqW","type":"WORKSPACE"}]}]} # AddPermissionsToUserGroupV1Input | 

    try:
        # Add Permissions to User Group
        api_response = api_instance.add_permissions_to_user_group(user_group_id, add_permissions_to_user_group_v1_input)
        print("The response of IAMGroupsApi->add_permissions_to_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->add_permissions_to_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **add_permissions_to_user_group_v1_input** | [**AddPermissionsToUserGroupV1Input**](AddPermissionsToUserGroupV1Input.md)|  | 

### Return type

[**AddPermissionsToUserGroup200Response**](AddPermissionsToUserGroup200Response.md)

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


## Operation: add_users_to_user_group

> AddUsersToUserGroup200Response add_users_to_user_group(user_group_id, add_users_to_user_group_v1_input)

Add Users to User Group

Adds a list of users or invites to a user group.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Subjects Added to Group * User Added To User Group          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.add_users_to_user_group200_response import AddUsersToUserGroup200Response
from segment_public_api.models.add_users_to_user_group_v1_input import AddUsersToUserGroupV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    add_users_to_user_group_v1_input = {"emails":["foo@example.com"]} # AddUsersToUserGroupV1Input | 

    try:
        # Add Users to User Group
        api_response = api_instance.add_users_to_user_group(user_group_id, add_users_to_user_group_v1_input)
        print("The response of IAMGroupsApi->add_users_to_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->add_users_to_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **add_users_to_user_group_v1_input** | [**AddUsersToUserGroupV1Input**](AddUsersToUserGroupV1Input.md)|  | 

### Return type

[**AddUsersToUserGroup200Response**](AddUsersToUserGroup200Response.md)

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


## Operation: create_user_group

> CreateUserGroup200Response create_user_group(create_user_group_v1_input)

Create User Group

Creates a user group.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* User Group Created * Policy Created          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_user_group200_response import CreateUserGroup200Response
from segment_public_api.models.create_user_group_v1_input import CreateUserGroupV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    create_user_group_v1_input = {"name":"New User Group Nbr5tuI40h"} # CreateUserGroupV1Input | 

    try:
        # Create User Group
        api_response = api_instance.create_user_group(create_user_group_v1_input)
        print("The response of IAMGroupsApi->create_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->create_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_group_v1_input** | [**CreateUserGroupV1Input**](CreateUserGroupV1Input.md)|  | 

### Return type

[**CreateUserGroup200Response**](CreateUserGroup200Response.md)

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


## Operation: delete_user_group

> DeleteUserGroup200Response delete_user_group(user_group_id)

Delete User Group

Removes a user group from a Workspace.    • When called, this endpoint may generate the `User Group Deleted` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_user_group200_response import DeleteUserGroup200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = '2c0vZc1kXJ9Nf9wIJ1Gb7JzORGf' # str | 

    try:
        # Delete User Group
        api_response = api_instance.delete_user_group(user_group_id)
        print("The response of IAMGroupsApi->delete_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->delete_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 

### Return type

[**DeleteUserGroup200Response**](DeleteUserGroup200Response.md)

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


## Operation: get_user_group

> GetUserGroup200Response get_user_group(user_group_id)

Get User Group

Returns a user group.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_user_group200_response import GetUserGroup200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 

    try:
        # Get User Group
        api_response = api_instance.get_user_group(user_group_id)
        print("The response of IAMGroupsApi->get_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->get_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 

### Return type

[**GetUserGroup200Response**](GetUserGroup200Response.md)

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


## Operation: list_invites_from_user_group

> ListInvitesFromUserGroup200Response list_invites_from_user_group(user_group_id, pagination=pagination)

List Invites from User Group

Returns the emails of invitees to a user group.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_invites_from_user_group200_response import ListInvitesFromUserGroup200Response
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
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination for invites to the group.  This parameter exists in v1. (optional)

    try:
        # List Invites from User Group
        api_response = api_instance.list_invites_from_user_group(user_group_id, pagination=pagination)
        print("The response of IAMGroupsApi->list_invites_from_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->list_invites_from_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination for invites to the group.  This parameter exists in v1. | [optional] 

### Return type

[**ListInvitesFromUserGroup200Response**](ListInvitesFromUserGroup200Response.md)

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


## Operation: list_user_groups

> ListUserGroups200Response list_user_groups(pagination=pagination)

List User Groups

Returns all user groups.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_user_groups200_response import ListUserGroups200Response
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
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination for user groups.  This parameter exists in v1. (optional)

    try:
        # List User Groups
        api_response = api_instance.list_user_groups(pagination=pagination)
        print("The response of IAMGroupsApi->list_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->list_user_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Pagination for user groups.  This parameter exists in v1. | [optional] 

### Return type

[**ListUserGroups200Response**](ListUserGroups200Response.md)

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


## Operation: list_users_from_user_group

> ListUsersFromUserGroup200Response list_users_from_user_group(user_group_id, pagination=pagination)

List Users from User Group

Returns users belonging to a user group.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_users_from_user_group200_response import ListUsersFromUserGroup200Response
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
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Pagination for members of a group.  This parameter exists in v1. (optional)

    try:
        # List Users from User Group
        api_response = api_instance.list_users_from_user_group(user_group_id, pagination=pagination)
        print("The response of IAMGroupsApi->list_users_from_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->list_users_from_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **pagination** | [**PaginationInput**](.md)| Pagination for members of a group.  This parameter exists in v1. | [optional] 

### Return type

[**ListUsersFromUserGroup200Response**](ListUsersFromUserGroup200Response.md)

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


## Operation: remove_users_from_user_group

> RemoveUsersFromUserGroup200Response remove_users_from_user_group(user_group_id, emails)

Remove Users from User Group

Removes one or multiple users or invites from a user group by email.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Group Memberships Deleted * User Removed From User Group          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.remove_users_from_user_group200_response import RemoveUsersFromUserGroup200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    emails = ['emails.0=foo%40example.com'] # List[str] | The list of emails to remove from the user group.  This parameter exists in v1.

    try:
        # Remove Users from User Group
        api_response = api_instance.remove_users_from_user_group(user_group_id, emails)
        print("The response of IAMGroupsApi->remove_users_from_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->remove_users_from_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **emails** | [**List[str]**](str.md)| The list of emails to remove from the user group.  This parameter exists in v1. | 

### Return type

[**RemoveUsersFromUserGroup200Response**](RemoveUsersFromUserGroup200Response.md)

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


## Operation: replace_permissions_for_user_group

> ReplacePermissionsForUserGroup200Response replace_permissions_for_user_group(user_group_id, replace_permissions_for_user_group_v1_input)

Replace Permissions for User Group

Updates the list of access permissions for a user group.    • When called, this endpoint may generate the `Policy Deleted` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_permissions_for_user_group200_response import ReplacePermissionsForUserGroup200Response
from segment_public_api.models.replace_permissions_for_user_group_v1_input import ReplacePermissionsForUserGroupV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    replace_permissions_for_user_group_v1_input = {"permissions":[{"roleId":"1WDUuRLxv84rrfCNUwvkrRtkxnS","resources":[{"id":"9aQ1Lj62S4bomZKLF4DPqW","type":"WORKSPACE"}]}]} # ReplacePermissionsForUserGroupV1Input | 

    try:
        # Replace Permissions for User Group
        api_response = api_instance.replace_permissions_for_user_group(user_group_id, replace_permissions_for_user_group_v1_input)
        print("The response of IAMGroupsApi->replace_permissions_for_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->replace_permissions_for_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **replace_permissions_for_user_group_v1_input** | [**ReplacePermissionsForUserGroupV1Input**](ReplacePermissionsForUserGroupV1Input.md)|  | 

### Return type

[**ReplacePermissionsForUserGroup200Response**](ReplacePermissionsForUserGroup200Response.md)

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


## Operation: replace_users_in_user_group

> ReplaceUsersInUserGroup200Response replace_users_in_user_group(user_group_id, replace_users_in_user_group_v1_input)

Replace Users in User Group

Replaces the members of a user group by email.    • When called, this endpoint may generate one or more of the following [audit trail](/tag/Audit-Trail) events:* Subjects Added to Group * User Added To User Group * Group Memberships Deleted          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.replace_users_in_user_group200_response import ReplaceUsersInUserGroup200Response
from segment_public_api.models.replace_users_in_user_group_v1_input import ReplaceUsersInUserGroupV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    replace_users_in_user_group_v1_input = {"emails":["foo@example.com"]} # ReplaceUsersInUserGroupV1Input | 

    try:
        # Replace Users in User Group
        api_response = api_instance.replace_users_in_user_group(user_group_id, replace_users_in_user_group_v1_input)
        print("The response of IAMGroupsApi->replace_users_in_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->replace_users_in_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **replace_users_in_user_group_v1_input** | [**ReplaceUsersInUserGroupV1Input**](ReplaceUsersInUserGroupV1Input.md)|  | 

### Return type

[**ReplaceUsersInUserGroup200Response**](ReplaceUsersInUserGroup200Response.md)

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


## Operation: update_user_group

> UpdateUserGroup200Response update_user_group(user_group_id, update_user_group_v1_input)

Update User Group

Updates a user group for a Workspace.    • When called, this endpoint may generate the `User Group Updated` event in the [audit trail](/tag/Audit-Trail).          The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_user_group200_response import UpdateUserGroup200Response
from segment_public_api.models.update_user_group_v1_input import UpdateUserGroupV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.IAMGroupsApi(api_client)
    user_group_id = 'bBABwqbaDf2QdwTbW8bNEm' # str | 
    update_user_group_v1_input = {"name":"PAPI Example Group"} # UpdateUserGroupV1Input | 

    try:
        # Update User Group
        api_response = api_instance.update_user_group(user_group_id, update_user_group_v1_input)
        print("The response of IAMGroupsApi->update_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IAMGroupsApi->update_user_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **update_user_group_v1_input** | [**UpdateUserGroupV1Input**](UpdateUserGroupV1Input.md)|  | 

### Return type

[**UpdateUserGroup200Response**](UpdateUserGroup200Response.md)

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

