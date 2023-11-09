# Segment Public API Python SDK

:warning: This SDK is currently released as [Public Beta](https://segment.com/legal/first-access-beta-preview/). Its use in critical systems is discouraged, but [feedback is welcome](#contributing).

The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.

All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.

See the next sections for more information on how to use the Segment Public API.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 38.0.0
- Package version: 38.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://docs.segmentapis.com](https://docs.segmentapis.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/segmentio/public-api-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/segmentio/public-api-sdk-python.git`)

Then import the package:
```python
import segment_public_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import segment_public_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import segment_public_api
from segment_public_api.rest import ApiException
from pprint import pprint

# Configure Bearer authorization: token
configuration = segment_public_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with segment_public_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = segment_public_api.WorkspacesApi(api_client)
    
    try:
        # Get Workspace
        api_response = api_instance.get_workspace()
        print("The response of WorkspacesApi->get_workspace:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)

    source_api_instance = segment_public_api.SourcesApi(api_client)
    cursor = None
    while True:
        try:
            # Get Sources
            pagination = segment_public_api.PaginationInput(count=50, cursor= cursor)
            api_response = source_api_instance.list_sources(pagination)
            print("The response of SourcesApi->list_sources:\n")
            pprint(api_response)
            cursor = api_response.data.pagination.next
            if api_response.data.pagination.next is None:
                break
        except ApiException as e:
            print("Exception when calling SourcesApi->list_sources: %s\n" % e)
```

## Contributing

The contents of this repository are automatically generated, so we can't take contributions from external developers. If you have any issues with this SDK, please raise an issue or reach out to friends@segment.com instead of opening a pull request. Pull requests will not be reviewed.
