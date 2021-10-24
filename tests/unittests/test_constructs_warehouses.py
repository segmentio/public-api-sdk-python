from unittest import mock

from papi.constructs import warehouses
from papi.common import common
from tests.unittests import base_constructs


class TestWarehouses(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'
        self._array = ['1', '2', '3']
        self._source_id = 'JVNa19ama'

    def test_all(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = warehouses.Warehouses(self._workspace).all()
            mock_iterator.assert_called_once_with('/warehouses', 'warehouses')
            self.assertEqual(ret, self._array)

    def test_get(self):
        get_response = common.bunch(warehouse=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = warehouses.Warehouses(self._workspace).get(self._id)
        self._workspace.get.assert_called_once_with(f'/warehouses/{self._id}')
        self.assertEqual(ret, self._id)

    def test_delete(self):
        delete_response = 'Success'
        self._initialize_workspace(delete_response=delete_response)
        ret = warehouses.Warehouses(self._workspace).delete(self._id)
        self._workspace.delete.assert_called_once_with(f'/warehouses/{self._id}', {'warehouseId': self._id})
        self.assertEqual(ret, delete_response)

    def test_connection_state(self):
        get_response = 'Connected'
        self._initialize_workspace(get_response=get_response)
        ret = warehouses.Warehouses(self._workspace).get_connection_state(self._id)
        self._workspace.get.assert_called_once_with(f'/warehouses/{self._id}/connection-state')
        self.assertEqual(ret, get_response)

    def test_get_warehouse_sources(self):
        get_response = common.bunch(sources=self._array)
        self._initialize_workspace(get_response=get_response)
        ret = warehouses.Warehouses(self._workspace).sources.all(self._id)
        self._workspace.get.assert_called_once_with(f'/warehouses/{self._id}/connected-sources')
        self.assertEqual(ret, get_response.sources)

    def test_connect_source_to_warehouse(self):
        post_response = 'Success'
        self._initialize_workspace(post_response=post_response)
        ret = warehouses.Warehouses(self._workspace).sources.add(self._id, self._source_id)
        self._workspace.post.assert_called_once_with(f'/warehouses/{self._id}/connected-sources/{self._source_id}')
        self.assertEqual(ret, post_response)

    def test_disconnect_source_to_warehouse(self):
        delete_response = 'Success'
        self._initialize_workspace(delete_response=delete_response)
        ret = warehouses.Warehouses(self._workspace).sources.remove(self._id, self._source_id)
        self._workspace.delete.assert_called_once_with(f'/warehouses/{self._id}/connected-sources/{self._source_id}')
        self.assertEqual(ret, delete_response)
