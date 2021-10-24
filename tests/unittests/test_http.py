from papi.errors import errors
from papi.common import common
from papi.mapper import tojsonstr
from papi.objects.Segment import Segment
from tests.unittests import base


class BaseHTTPClientTest(base.BaseTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'
        self._workspace = Segment.workspace("")

    def _patch_execute(self):
        return self.patch_call('papi.http.httpclient.HTTPClient._execute')

    def test_http_get(self):
        mock_http_execute = self._patch_execute()
        response = common.bunch(
            ok=True,
            text=tojsonstr(common.bunch(
                    data=common.bunch(
                        source=common.bunch(
                            id=self._id
                        )
                    )
                )
            )
        )
        mock_http_execute.return_value = (None, response)
        ret = self._workspace.connections.sources.get(self._id)
        http_request = mock_http_execute.call_args[0][0]
        self.assertEqual('GET', http_request.method)
        self.assertEqual(f'{self._workspace.baseurl}/sources/{self._id}', http_request.url)
        self.assertEqual(ret.id, self._id)

    def test_http_post(self):
        mock_http_execute = self._patch_execute()
        response = common.bunch(
            ok=True,
            text=tojsonstr(common.bunch(
                    data=common.bunch(
                        labels=[]
                    )
                )
            )
        )
        mock_http_execute.return_value = (None, response)
        self._workspace.admin.labels.add('key', 'value', 'description')
        http_request = mock_http_execute.call_args[0][0]
        self.assertEqual('POST', http_request.method)
        self.assertEqual(f'{self._workspace.baseurl}/labels', http_request.url)

    def test_http_delete(self):
        mock_http_execute = self._patch_execute()
        response = common.bunch(
            ok=True,
            text=tojsonstr(common.bunch(
                    data=common.bunch(
                        status='success'
                    )
                )
            )
        )
        mock_http_execute.return_value = (None, response)
        key, value = 'key', 'value'
        ret = self._workspace.admin.labels.delete(key, value)
        http_request = mock_http_execute.call_args[0][0]
        self.assertEqual('DELETE', http_request.method)
        self.assertEqual(f'{self._workspace.baseurl}/labels/{key}/{value}', http_request.url)
        self.assertEqual(ret.status, 'success')

    def test_http_patch(self):
        mock_http_execute = self._patch_execute()
        response = common.bunch(
            ok=True,
            text=tojsonstr(common.bunch(
                    data=common.bunch(
                        source=common.bunch(
                            id=self._id
                        )
                    )
                )
            )
        )
        mock_http_execute.return_value = (None, response)
        ret = self._workspace.connections.sources.update(self._id)
        http_request = mock_http_execute.call_args[0][0]
        self.assertEqual('PATCH', http_request.method)
        self.assertEqual(f'{self._workspace.baseurl}/sources/{self._id}', http_request.url)
        self.assertEqual(ret.id, self._id)

    def test_http_error(self):
        mock_http_execute = self._patch_execute()
        response = common.bunch(
            ok=False,
            status_code=404,
            text=tojsonstr(common.bunch(
                    errors=common.bunch(
                        message='Resource not found'
                    )
                )
            )
        )
        mock_http_execute.return_value = (None, response)
        with self.assertRaises(errors.ResourceNotFound) as error:
            self._workspace.connections.sources.get(self._id)
        http_request = mock_http_execute.call_args[0][0]
        self.assertEqual('GET', http_request.method)
        self.assertEqual(f'{self._workspace.baseurl}/sources/{self._id}', http_request.url)
        self.assertEqual('Resource not found', error.exception.errors.message)
