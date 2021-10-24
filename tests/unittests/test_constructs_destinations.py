from unittest import mock

from papi.constructs import destinations
from papi.common import common, settings
from tests.unittests import base_constructs


class TestDestinations(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'
        self._array = ['1', '2', '3']
        self._destination = common.bunch(
            id=self._id,
            enabled=True,
            catalog_slug='aws-s3',
            name='AWS S3',
            options={
                'awsRegion': 'us-west-2',
                'bucket': 'test-bucket'
            }
        )

    def test_all(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = destinations.Destinations(self._workspace).all()
            mock_iterator.assert_called_once_with('/destinations', 'destinations')
            self.assertEqual(ret, self._array)

    def test_get(self):
        get_response = common.bunch(destination=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = destinations.Destinations(self._workspace).get(self._id)
        self._workspace.get.assert_called_once_with(f'/destinations/{self._id}')
        self.assertEqual(ret, self._id)

    def test_delete(self):
        delete_response = 'Success'
        self._initialize_workspace(delete_response=delete_response)
        ret = destinations.Destinations(self._workspace).delete(self._id)
        self._workspace.delete.assert_called_once_with(f'/destinations/{self._id}', {'destinationId': self._id})
        self.assertEqual(ret, delete_response)

    def test_update(self):
        patch_response = common.bunch(destination=self._id)
        self._initialize_workspace(patch_response=patch_response)
        ret = destinations.Destinations(self._workspace).update(
            self._id,
            self._destination.name,
            self._destination.enabled,
            self._destination.options
        )
        self._workspace.patch.assert_called_once_with(f'/destinations/{self._id}', mock.ANY)
        expected_param = common.bunch(
            destinationId=self._id,
            name=self._destination.name,
            enabled=self._destination.enabled,
            settings=settings.create_settings(self._destination.options)
        )
        actual_param = self._workspace.patch.call_args[0][1]
        self.assert_equal_objects(actual_param, expected_param)
        self.assertEqual(ret, self._id)
