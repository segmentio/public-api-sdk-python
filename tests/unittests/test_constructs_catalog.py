from unittest import mock

from papi.constructs import catalog
from papi.common import common
from papi.errors import errors
from tests.unittests import base_constructs


class TestCatalog(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'
        self._slug = 'javascript'

    def test_show_sources(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = TestCatalog._create_iterator_response()
            catalog.Catalog(self._workspace).show_sources()
            mock_iterator.assert_called_once_with('/catalog/sources', 'sourcesCatalog')

    def test_show_destinations(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = TestCatalog._create_iterator_response()
            catalog.Catalog(self._workspace).show_destinations()
            mock_iterator.assert_called_once_with('/catalog/destinations', 'destinationsCatalog')

    def test_show_warehouses(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = TestCatalog._create_iterator_response()
            catalog.Catalog(self._workspace).show_warehouses()
            mock_iterator.assert_called_once_with('/catalog/warehouses', 'warehousesCatalog')

    @staticmethod
    def _create_iterator_response():
        return [common.bunch(id=id, slug=slug, name=name, options=options) for id, slug, name, options in [
            ('a87shd1ka', 'javascript', 'Javascript', [common.bunch(name='api-key', required=True, type='string')]),
            ('kajnsd19a', 'kotlin', 'Kotlin', [common.bunch(name='account_id', required=False, type='int')]),
            ('lk1on2e41', 'zendesk', 'Zendesk', [common.bunch(name='buckets', required=True, type='array')])
        ]]

    def test_show_source_options(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = TestCatalog._create_iterator_response()
            catalog.Catalog(self._workspace).show_source_options('javascript')
            mock_iterator.assert_called_once_with('/catalog/sources', 'sourcesCatalog')

    def test_show_destination_options(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = TestCatalog._create_iterator_response()
            catalog.Catalog(self._workspace).show_destination_options('kotlin')
            mock_iterator.assert_called_once_with('/catalog/destinations', 'destinationsCatalog')

    def test_show_warehouse_options(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = TestCatalog._create_iterator_response()
            catalog.Catalog(self._workspace).show_warehouse_options('zendesk')
            mock_iterator.assert_called_once_with('/catalog/warehouses', 'warehousesCatalog')

    def test_get_source_not_found(self):
        mock_iterator = self.patch_call("papi.objects.Segment.Workspace.iterator")
        mock_iterator.return_value = []
        with self.assertRaises(errors.ResourceNotFound) as error:
            catalog.Catalog(self._workspace).get_source('javascript')
        mock_iterator.assert_called_once_with('/catalog/sources', 'sourcesCatalog')
        self.assertEqual('Resource not found', error.exception.message)

    def test_get_destination_not_found(self):
        mock_iterator = self.patch_call("papi.objects.Segment.Workspace.iterator")
        mock_iterator.return_value = []
        with self.assertRaises(errors.ResourceNotFound) as error:
            catalog.Catalog(self._workspace).get_destination('aws-s3')
        mock_iterator.assert_called_once_with('/catalog/destinations', 'destinationsCatalog')
        self.assertEqual('Resource not found', error.exception.message)

    def test_get_warehouse_not_found(self):
        mock_iterator = self.patch_call("papi.objects.Segment.Workspace.iterator")
        mock_iterator.return_value = []
        with self.assertRaises(errors.ResourceNotFound) as error:
            catalog.Catalog(self._workspace).get_warehouse('redshift')
        mock_iterator.assert_called_once_with('/catalog/warehouses', 'warehousesCatalog')
        self.assertEqual('Resource not found', error.exception.message)

    def test_get_source_metadata(self):
        get_response = common.bunch(sourceMetadata=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = catalog.Catalog(self._workspace).get_source_metadata(self._id)
        self._workspace.get.assert_called_once_with(f'/catalog/sources/{self._id}')
        self.assertEqual(ret, self._id)

    def test_get_destination_metadata(self):
        get_response = common.bunch(destinationMetadata=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = catalog.Catalog(self._workspace).get_destination_metadata(self._id)
        self._workspace.get.assert_called_once_with(f'/catalog/destinations/{self._id}')
        self.assertEqual(ret, self._id)

    def test_get_warehouse_metadata(self):
        get_response = common.bunch(warehouseMetadata=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = catalog.Catalog(self._workspace).get_warehouse_metadata(self._id)
        self._workspace.get.assert_called_once_with(f'/catalog/warehouses/{self._id}')
        self.assertEqual(ret, self._id)
