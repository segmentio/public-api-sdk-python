from unittest import mock

from papi.constructs import usage
from tests.unittests import base_constructs


class TestUsage(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._period = '2021-11-01'
        self._array = [1, 2, 3]

    def test_source_daily_api_call_count(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = usage.Usage(self._workspace).sources.api.daily(self._period)
            mock_iterator.assert_called_once_with('/usage/api-calls/sources/daily', 'dailyPerSourceAPICallsUsage', {'period': self._period})
        self.assertEqual(ret, self._array)

    def test_source_daily_mtu_count(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = usage.Usage(self._workspace).sources.mtu.daily(self._period)
            mock_iterator.assert_called_once_with('/usage/mtu/sources/daily', 'dailyPerSourceMTUUsage', {'period': self._period})
        self.assertEqual(ret, self._array)

    def test_workspace_daily_api_call_count(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = usage.Usage(self._workspace).workspace.api.daily(self._period)
            mock_iterator.assert_called_once_with('/usage/api-calls/daily', 'dailyWorkspaceAPICallsUsage', {'period': self._period})
        self.assertEqual(ret, self._array)

    def test_workspace_daily_mtu_count(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = usage.Usage(self._workspace).workspace.mtu.daily(self._period)
            mock_iterator.assert_called_once_with('/usage/mtu/daily', 'dailyWorkspaceMTUUsage', {'period': self._period})
        self.assertEqual(ret, self._array)
