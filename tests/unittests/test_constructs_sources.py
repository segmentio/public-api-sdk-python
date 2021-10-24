from unittest import mock

from papi.constructs import sources
from papi.common import common, settings
from tests.unittests import base_constructs


class TestSources(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'
        self._array = ['1', '2', '3']
        self._source = common.bunch(
            id=self._id,
            catalog_slug='javascript',
            slug='ajs',
            enabled=True,
            name='website',
            options={
                'api-key': '54521fdc25e721e32a72ef02'
            }
        )

    def test_add_from_source_without_override(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = [common.bunch(
                id=self._id,
                slug=self._source.catalog_slug,
                options=[]
            )]
            self._initialize_workspace(post_response=common.bunch(source=self._id))
            ret = sources.Sources(self._workspace).add_from_source(
                common.bunch(
                    metadata=common.bunch(slug=self._source.catalog_slug),
                    slug=self._source.slug,
                    enabled=self._source.enabled,
                    name=self._source.name,
                    settings={}
                )
            )
            mock_iterator.assert_called_once_with('/catalog/sources', 'sourcesCatalog')
            self._workspace.post.assert_called_once_with('/sources', mock.ANY)
            expected_param = TestSources._create_add_parameter(self._source.slug, self._source.enabled, self._source.name,
                                                               self._id)
            actual_param = self._workspace.post.call_args[0][1]
            self.assert_equal_objects(actual_param, expected_param)
            self.assertEqual(ret, self._id)

    def test_add_with_options(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = [common.bunch(
                id=self._id,
                slug=self._source.catalog_slug,
                options=[
                    common.bunch(
                        name='api-key',
                        required=True
                    )
                ])
            ]
            self._initialize_workspace(post_response=common.bunch(source=self._id))
            ret = sources.Sources(self._workspace).add(
                self._source.catalog_slug,
                self._source.slug,
                self._source.enabled,
                self._source.name,
                self._source.options
            )
            mock_iterator.assert_called_once_with('/catalog/sources', 'sourcesCatalog')
            self._workspace.post.assert_called_once_with('/sources', mock.ANY)
            expected_param = TestSources._create_add_parameter(self._source.slug, self._source.enabled, self._source.name,
                                                               self._id, self._source.options)
            actual_param = self._workspace.post.call_args[0][1]
            self.assert_equal_objects(actual_param, expected_param)
            self.assertEqual(ret, self._id)

    @staticmethod
    def _create_add_parameter(slug, enabled, name, metadata_id, options=None):
        param = common.bunch(
            slug=slug,
            enabled=enabled,
            name=name,
            metadataId=metadata_id,
        )
        if options:
            param.settings = settings.create_settings(options)
        return param

    def test_find(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = [common.bunch(
                id=self._source.id,
                slug=self._source.slug
            )]
            ret = sources.Sources(self._workspace).find(self._source.slug)
            self.assertEqual(ret.slug, self._source.slug)

    def test_all(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = sources.Sources(self._workspace).all()
            mock_iterator.assert_called_once_with('/sources', 'sources')
            self.assertEqual(ret, self._array)

    def test_get(self):
        get_response = common.bunch(source=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = sources.Sources(self._workspace).get(self._id)
        self._workspace.get.assert_called_once_with(f'/sources/{self._id}')
        self.assertEqual(ret, self._id)

    def test_show(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = [self._source]
            self._initialize_workspace()
            sources.Sources(self._workspace).show()
            mock_iterator.assert_called_once_with('/sources', 'sources')

    def test_delete(self):
        delete_response = 'Success'
        self._initialize_workspace(delete_response=delete_response)
        ret = sources.Sources(self._workspace).delete(self._id)
        self._workspace.delete.assert_called_once_with(f'/sources/{self._id}', {'sourceId': self._id})
        self.assertEqual(ret, delete_response)

    def test_destinations(self):
        get_response = common.bunch(destinations=self._array)
        self._initialize_workspace(get_response=get_response)
        ret = sources.Sources(self._workspace).destinations(self._id)
        self._workspace.get.assert_called_once_with(f'/sources/{self._id}/connected-destinations')
        self.assertEqual(ret, self._array)

    def test_warehouses(self):
        get_response = common.bunch(warehouses=self._array)
        self._initialize_workspace(get_response=get_response)
        ret = sources.Sources(self._workspace).warehouses(self._id)
        self._workspace.get.assert_called_once_with(f'/sources/{self._id}/connected-warehouses')
        self.assertEqual(ret, self._array)

    def test_update(self):
        patch_response = common.bunch(source=self._id)
        self._initialize_workspace(patch_response=patch_response)
        ret = sources.Sources(self._workspace).update(
            self._id,
            self._source.name,
            self._source.enabled,
            self._source.slug,
            self._source.options
        )
        self._workspace.patch.assert_called_once_with(f'/sources/{self._id}', mock.ANY)
        expected_param = common.bunch(
            sourceId=self._id,
            name=self._source.name,
            enabled=self._source.enabled,
            slug=self._source.slug,
            settings=settings.create_settings(self._source.options)
        )
        actual_param = self._workspace.patch.call_args[0][1]
        self.assert_equal_objects(actual_param, expected_param)
        self.assertEqual(ret, self._id)
