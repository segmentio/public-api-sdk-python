from papi.common import common
from tests.unittests import base_constructs


class TestWorkspace(base_constructs.BaseConstructTest):

    def test_domain(self):
        self.assertEqual(self._workspace.domain, 'api.segmentapis.com')

    def test_info(self):
        get_response = common.bunch(
            workspace=common.bunch(
                id='id',
                slug='slug',
                name='name'
            )
        )
        self._initialize_workspace(get_response=get_response)
        ret = self._workspace.info
        self.assert_equal_objects(ret, get_response.workspace)

    def test_baseurl(self):
        self.assertEqual(self._workspace.baseurl, 'https://api.segmentapis.com')

    def test_api_version(self):
        stable = 'stable'
        self.assertEqual(self._workspace._api_version(stable), f'application/vnd.segment.{stable}+json')  # pylint: disable=protected-access
