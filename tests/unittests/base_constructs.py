from unittest import mock

from papi.objects.Segment import Segment
from tests.unittests import base


class BaseConstructTest(base.BaseTest):

    def setUp(self):
        super().setUp()
        self._workspace = Segment.workspace("")

    def _initialize_workspace(self, get_response=None, put_response=None, post_response=None, delete_response=None, patch_response=None):
        self._workspace.get = mock.MagicMock(return_value=get_response)
        self._workspace.put = mock.MagicMock(return_value=put_response)
        self._workspace.post = mock.MagicMock(return_value=post_response)
        self._workspace.delete = mock.MagicMock(return_value=delete_response)
        self._workspace.patch = mock.MagicMock(return_value=patch_response)
