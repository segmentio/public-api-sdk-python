from unittest import mock

from papi.constructs import functions
from papi.common import common, enum
from tests.unittests import base_constructs


class TestFunctions(base_constructs.BaseConstructTest):

    def setUp(self):
        super().setUp()
        self._id = 'M4IdvFGSk9'
        self._array = ['1', '2', '3']
        self._function = common.bunch(
            id=self._id,
            code='code',
            settings='settings',
            display_name='display_name',
            logo_url='logo_url',
            description='description'
        )

    def test_add_function_from_funcion_without_override(self):
        self._initialize_workspace(post_response=common.bunch(function=self._id))
        function = TestFunctions._create_add_parameter(
            enum.FunctionType.SOURCE,
            self._function.code,
            self._function.settings,
            self._function.display_name,
            self._function.logo_url,
            self._function.description
        )
        ret = functions.Functions(self._workspace).add_from_function(function)
        self._workspace.post.assert_called_once_with('/functions', mock.ANY)
        actual_param = self._workspace.post.call_args[0][1]
        self.assert_equal_objects(actual_param, function)
        self.assertEqual(ret, self._id)

    def test_add_source_function_with_options(self):
        self._initialize_workspace(post_response=common.bunch(function=self._id))
        ret = functions.Functions(self._workspace).add(
            enum.FunctionType.SOURCE,
            self._function.code,
            self._function.settings,
            self._function.display_name,
            self._function.logo_url,
            self._function.description
        )
        self._workspace.post.assert_called_once_with('/functions', mock.ANY)
        expected_param = TestFunctions._create_add_parameter(enum.FunctionType.SOURCE, self._function.code, self._function.settings,
                                                             self._function.display_name, self._function.logo_url, self._function.description)
        actual_param = self._workspace.post.call_args[0][1]
        self.assert_equal_objects(actual_param, expected_param)
        self.assertEqual(ret, self._id)

    @staticmethod
    def _create_add_parameter(function_type, code, settings, display_name, logo_url, description):
        param = common.bunch(
            code=code,
            settings=settings,
            resourceType=function_type,
            displayName=display_name,
            logoUrl=logo_url,
            description=description
        )
        return param

    def test_all_without_filter(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            ret = functions.Functions(self._workspace).all()
            mock_iterator.assert_has_calls([
                mock.call('/functions', 'functions', {'resourceType': enum.FunctionType.SOURCE}),
                mock.call('/functions', 'functions', {'resourceType': enum.FunctionType.DESTINATION})
            ])
            self.assertEqual(list(ret), self._array * 2)

    def test_all_with_filter(self):
        with mock.patch("papi.objects.Segment.Workspace.iterator") as mock_iterator:
            mock_iterator.return_value = self._array
            function_type = enum.FunctionType.SOURCE
            ret = functions.Functions(self._workspace).all(function_type)
            mock_iterator.assert_called_once_with('/functions', 'functions', {'resourceType': function_type})
            self.assertEqual(ret, self._array)

    def test_get(self):
        get_response = common.bunch(function=self._id)
        self._initialize_workspace(get_response=get_response)
        ret = functions.Functions(self._workspace).get(self._id)
        self._workspace.get.assert_called_once_with(f'/functions/{self._id}')
        self.assertEqual(ret, self._id)

    def test_get_function_code(self):
        get_response = common.bunch(function=common.bunch(code=self._function.code))
        self._initialize_workspace(get_response=get_response)
        ret = functions.Functions(self._workspace).get_function_code(self._id)
        self._workspace.get.assert_called_once_with(f'/functions/{self._id}')
        self.assertEqual(ret, self._function.code)

    def test_function_deploy(self):
        post_response = common.bunch(functionDeployment='Success')
        self._initialize_workspace(post_response=post_response)
        ret = functions.Functions(self._workspace).deploy(self._id)
        self._workspace.post.assert_called_once_with(f'/functions/{self._id}/deploy')
        self.assertEqual(ret, post_response.functionDeployment)

    def test_delete(self):
        delete_response = 'Success'
        self._initialize_workspace(delete_response=delete_response)
        ret = functions.Functions(self._workspace).delete(self._id)
        self._workspace.delete.assert_called_once_with(f'/functions/{self._id}', {'functionId': self._id})
        self.assertEqual(ret, delete_response)

    def test_update(self):
        patch_response = common.bunch(function=self._id)
        self._initialize_workspace(patch_response=patch_response)
        ret = functions.Functions(self._workspace).update(
            self._id,
            self._function.code,
            self._function.settings,
            self._function.display_name,
            self._function.logo_url,
            self._function.description
        )
        self._workspace.patch.assert_called_once_with(f'/functions/{self._id}', mock.ANY)
        expected_param = common.bunch(
            functionId=self._id,
            code=self._function.code,
            settings=self._function.settings,
            displayName=self._function.display_name,
            logoUrl=self._function.logo_url,
            description=self._function.description,
        )
        actual_param = self._workspace.patch.call_args[0][1]
        self.assert_equal_objects(actual_param, expected_param)
        self.assertEqual(ret, self._id)
