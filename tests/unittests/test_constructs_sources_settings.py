from papi.constructs import sources
from papi.common import common
from tests.unittests import base_constructs


class TestSourcesSettings(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'

    def test_get(self):
        get_response = common.bunch(settings='settings')
        self._initialize_workspace(get_response=get_response)
        ret = sources.Sources(self._workspace).settings.get(self._id)
        self._workspace.get.assert_called_once_with(f'/sources/{self._id}/settings')
        self.assertEqual(ret, 'settings')
