# segment_public_api.CredentialsApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](CredentialsApi.md#create_credential) | **POST** /credentials | Create Credential
[**delete_credential**](CredentialsApi.md#delete_credential) | **DELETE** /credentials/{credentialId} | Delete Credential
[**get_credential**](CredentialsApi.md#get_credential) | **GET** /credentials/{credentialId} | Get Credential
[**list_credential_consumers**](CredentialsApi.md#list_credential_consumers) | **GET** /credentials/{credentialId}/consumers | List Credential Consumers
[**list_credentials**](CredentialsApi.md#list_credentials) | **GET** /credentials | List Credentials
[**update_credential**](CredentialsApi.md#update_credential) | **PATCH** /credentials/{credentialId} | Update Credential



## Operation: create_credential

> CreateCredential201Response create_credential(create_credential_v1_input)

Create Credential

Creates a new Credential.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_credential201_response import CreateCredential201Response
from segment_public_api.models.create_credential_v1_input import CreateCredentialV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CredentialsApi(api_client)
    create_credential_v1_input = {"name":"Production Snowflake","settings":{"type":"Snowflake","username":"prod_user","account":"xy12345.us-east-1","warehouse":"COMPUTE_WH","database":"ANALYTICS_DB","authentication":{"type":"keypair","privateKey":"<privateKey>","privateKeyPassphrase":"<privateKeyPassphrase>"}}} # CreateCredentialV1Input | 

    try:
        # Create Credential
        api_response = api_instance.create_credential(create_credential_v1_input)
        print("The response of CredentialsApi->create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credential_v1_input** | [**CreateCredentialV1Input**](CreateCredentialV1Input.md)|  | 

### Return type

[**CreateCredential201Response**](CreateCredential201Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json
 - **Accept**: application/vnd.segment.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: delete_credential

> DeleteCredential200Response delete_credential(credential_id)

Delete Credential

Deletes an existing Credential. Fails if the Credential is still in use by a Warehouse or Source.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.delete_credential200_response import DeleteCredential200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CredentialsApi(api_client)
    credential_id = 'cred_2JzKWb8FGhGVYZ3xVqQGc7NkYPl' # str | 

    try:
        # Delete Credential
        api_response = api_instance.delete_credential(credential_id)
        print("The response of CredentialsApi->delete_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

[**DeleteCredential200Response**](DeleteCredential200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: get_credential

> GetCredential200Response get_credential(credential_id)

Get Credential

Returns a Credential by its id.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.get_credential200_response import GetCredential200Response
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CredentialsApi(api_client)
    credential_id = 'cred_2JzKWb8FGhGVYZ3xVqQGc7NkYPl' # str | 

    try:
        # Get Credential
        api_response = api_instance.get_credential(credential_id)
        print("The response of CredentialsApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

[**GetCredential200Response**](GetCredential200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: list_credential_consumers

> ListCredentialConsumers200Response list_credential_consumers(credential_id, warehouses_pagination=warehouses_pagination, sources_pagination=sources_pagination)

List Credential Consumers

Returns the Warehouses and Sources that use a Credential.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_credential_consumers200_response import ListCredentialConsumers200Response
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
    api_instance = segment_public_api.CredentialsApi(api_client)
    credential_id = 'cred_2JzKWb8FGhGVYZ3xVqQGc7NkYPl' # str | 
    warehouses_pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters for the list of Warehouses.  This parameter exists in v1. (optional)
    sources_pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters for the list of Sources.  This parameter exists in v1. (optional)

    try:
        # List Credential Consumers
        api_response = api_instance.list_credential_consumers(credential_id, warehouses_pagination=warehouses_pagination, sources_pagination=sources_pagination)
        print("The response of CredentialsApi->list_credential_consumers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->list_credential_consumers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **warehouses_pagination** | [**PaginationInput**](.md)| Defines the pagination parameters for the list of Warehouses.  This parameter exists in v1. | [optional] 
 **sources_pagination** | [**PaginationInput**](.md)| Defines the pagination parameters for the list of Sources.  This parameter exists in v1. | [optional] 

### Return type

[**ListCredentialConsumers200Response**](ListCredentialConsumers200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: list_credentials

> ListCredentials200Response list_credentials(pagination=pagination)

List Credentials

Returns a list of Credentials.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.list_credentials200_response import ListCredentials200Response
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
    api_instance = segment_public_api.CredentialsApi(api_client)
    pagination = segment_public_api.PaginationInput(count=10) # PaginationInput | Defines the pagination parameters.  This parameter exists in v1. (optional)

    try:
        # List Credentials
        api_response = api_instance.list_credentials(pagination=pagination)
        print("The response of CredentialsApi->list_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->list_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**PaginationInput**](.md)| Defines the pagination parameters.  This parameter exists in v1. | [optional] 

### Return type

[**ListCredentials200Response**](ListCredentials200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.segment.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## Operation: update_credential

> UpdateCredential200Response update_credential(credential_id, update_credential_v1_input)

Update Credential

Updates an existing Credential. All Warehouses using this Credential are affected immediately.

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.update_credential200_response import UpdateCredential200Response
from segment_public_api.models.update_credential_v1_input import UpdateCredentialV1Input
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.CredentialsApi(api_client)
    credential_id = 'cred_2JzKWb8FGhGVYZ3xVqQGc7NkYPl' # str | 
    update_credential_v1_input = {"name":"Updated Snowflake Prod","settings":{"username":"new_prod_user","authentication":{"type":"keypair","privateKey":"<newPrivateKey>","privateKeyPassphrase":"<newPrivateKeyPassphrase>"}}} # UpdateCredentialV1Input | 

    try:
        # Update Credential
        api_response = api_instance.update_credential(credential_id, update_credential_v1_input)
        print("The response of CredentialsApi->update_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **update_credential_v1_input** | [**UpdateCredentialV1Input**](UpdateCredentialV1Input.md)|  | 

### Return type

[**UpdateCredential200Response**](UpdateCredential200Response.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.segment.v1+json
 - **Accept**: application/vnd.segment.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Resource not found |  -  |
**422** | Validation failure |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

