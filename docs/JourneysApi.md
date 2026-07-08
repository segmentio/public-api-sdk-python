# segment_public_api.JourneysApi

All URIs are relative to *https://api.segmentapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_journey**](JourneysApi.md#create_journey) | **POST** /spaces/{spaceId}/journeys | Create Journey



## Operation: create_journey

> CreateJourney200Response create_journey(space_id, create_journey_alpha_input)

Create Journey

Creates a Journey in the given Engage space. Accepts an XState journey definition and creates the journey in draft state.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com. 

### Example

* Bearer Authentication (token):
```python
import time
import os
import segment_public_api
from segment_public_api.models.create_journey200_response import CreateJourney200Response
from segment_public_api.models.create_journey_alpha_input import CreateJourneyAlphaInput
from segment_public_api.rest import ApiException
from pprint import pprint



# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.JourneysApi(api_client)
    space_id = '9aQ1Lj62S4bomZKLF4DPqW' # str | 
    create_journey_alpha_input = {"name":"Checkout Abandonment SMS","description":"Sends SMS to users who abandon checkout within 3 minutes","definition":{"initial":"entry_ab1c2","states":{"entry_ab1c2":{"meta":{"type":"entry","event":{"type":"ast","options":{"AND":[{"event":"checkout_started"}]}}},"on":{"next":"split_de3f4"}},"split_de3f4":{"meta":{"type":"split","name":"Wait for checkout_completed","splitType":"event","delay":{"duration":3,"durationUnits":"minutes"}},"on":{"branch_1":"splitBranch_gh5i6","else":"splitElseBranch_jk7l8"}},"splitBranch_gh5i6":{"meta":{"type":"splitBranch","name":"Completed","condition":{"type":"ast","options":{"AND":[{"event":"checkout_completed"}]}}},"on":{"next":"exit_mn9o0"}},"splitElseBranch_jk7l8":{"meta":{"type":"splitElseBranch","name":"Abandoned"},"on":{"next":"exit_mn9o0"}},"exit_mn9o0":{"meta":{"type":"exit"}}},"entryRules":{"type":"multiple","concurrency":{"enabled":true,"propertyFilter":{"property":"checkout_id"}}}}} # CreateJourneyAlphaInput | 

    try:
        # Create Journey
        api_response = api_instance.create_journey(space_id, create_journey_alpha_input)
        print("The response of JourneysApi->create_journey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JourneysApi->create_journey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **space_id** | **str**|  | 
 **create_journey_alpha_input** | [**CreateJourneyAlphaInput**](CreateJourneyAlphaInput.md)|  | 

### Return type

[**CreateJourney200Response**](CreateJourney200Response.md)

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

