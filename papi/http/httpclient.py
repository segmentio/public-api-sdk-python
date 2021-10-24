import requests
from ..lib import Command
from ..mapper import fromjsonstr, tojsonstr
from ..errors import errors


class HTTPClientRequest():
    def __init__(self, method, url, **kwargs):
        self.method = method
        self.url = url
        self.kwargs = kwargs


class HTTPClientRequestGET(HTTPClientRequest):
    def __init__(self, url, params=None, headers=None, stream=None):
        super().__init__('GET', url, params=params, headers=headers, stream=stream)


class HTTPClientRequestPUT(HTTPClientRequest):
    def __init__(self, url, headers=None, data=None):
        super().__init__('PUT', url, headers=headers, data=data)


class HTTPClientRequestPOST(HTTPClientRequest):
    def __init__(self, url, headers=None, data=None):
        super().__init__('POST', url, headers=headers, data=data)


class HTTPClientRequestDELETE(HTTPClientRequest):
    def __init__(self, url, headers=None, data=None):
        super().__init__('DELETE', url, headers=headers, data=data)


class HTTPClientRequestPATCH(HTTPClientRequest):
    def __init__(self, url, headers=None, data=None):
        super().__init__('PATCH', url, headers=headers, data=data)


class HTTPClient:

    def __init__(self):
        self._session = requests.Session()

    def get(self, url, params=None, headers=None):
        return self._execute(HTTPClientRequestGET(url, params=params, headers=headers))

    def put(self, url, headers=None, data=None):
        return self._execute(HTTPClientRequestPUT(url, headers=headers, data=data))

    def post(self, url, headers=None, data=None):
        return self._execute(HTTPClientRequestPOST(url, headers=headers, data=data))

    def delete(self, url, headers=None, data=None):
        return self._execute(HTTPClientRequestDELETE(url, headers=headers, data=data))

    def patch(self, url, headers=None, data=None):
        return self._execute(HTTPClientRequestPATCH(url, headers=headers, data=data))

    def set_headers(self, headers):
        """
        Set headers that will be included in every http request.

        :param dict headers: the headers, represented as a key-value strings in a dict
        """
        self._session.headers.update(headers)

    def _execute(self, request):
        response = self._session.request(request.method, request.url, **request.kwargs)
        return (request, response)


class SegmentClient:

    def __init__(self, token):
        self._httpclient = HTTPClient()
        self._httpclient.set_headers({'Authorization': f'Bearer {token}'})

    def get(self, baseurl, path, params=None):
        function = Command(HTTPClient.get, self._httpclient, compute_uri(baseurl, path), params if params else {})
        return SegmentClient._execute(function)

    def put(self, baseurl, path, data):
        function = Command(HTTPClient.put, self._httpclient, compute_uri(baseurl, path), {'Content-Type': 'application/json'}, tojsonstr(data))
        return SegmentClient._execute(function)

    def post(self, baseurl, path, data):
        function = Command(HTTPClient.post, self._httpclient, compute_uri(baseurl, path), {'Content-Type': 'application/json'}, tojsonstr(data))
        return SegmentClient._execute(function)

    def delete(self, baseurl, path, data):
        function = Command(HTTPClient.delete, self._httpclient, compute_uri(baseurl, path), {'Content-Type': 'application/json'}, tojsonstr(data))
        return SegmentClient._execute(function)

    def patch(self, baseurl, path, data):
        function = Command(HTTPClient.patch, self._httpclient, compute_uri(baseurl, path), {'Content-Type': 'application/json'}, tojsonstr(data))
        return SegmentClient._execute(function)

    @staticmethod
    def _execute(function):
        request, response = function()  # pylint: disable=unused-variable
        body = fromjsonstr(response.text)
        if response.ok:
            return body.data
        raise errors.ErrorFactory.create(response.status_code, errors=body.errors)


def compute_uri(baseurl, path):
    return baseurl + (path[1:] if baseurl[-1] == path[0] == '/' else path)
