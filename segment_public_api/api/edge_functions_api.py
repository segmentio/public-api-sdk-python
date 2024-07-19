# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.4.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import constr

from segment_public_api.models.create_edge_functions200_response import CreateEdgeFunctions200Response
from segment_public_api.models.create_edge_functions_alpha_input import CreateEdgeFunctionsAlphaInput
from segment_public_api.models.disable_edge_functions200_response import DisableEdgeFunctions200Response
from segment_public_api.models.generate_upload_url_for_edge_functions200_response import GenerateUploadURLForEdgeFunctions200Response
from segment_public_api.models.get_latest_from_edge_functions200_response import GetLatestFromEdgeFunctions200Response

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EdgeFunctionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_edge_functions(self, source_id : constr(strict=True), create_edge_functions_alpha_input : CreateEdgeFunctionsAlphaInput, **kwargs) -> CreateEdgeFunctions200Response:  # noqa: E501
        """Create Edge Functions  # noqa: E501

        Create EdgeFunctions for your Source given a valid upload URL for an Edge Functions bundle.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_edge_functions(source_id, create_edge_functions_alpha_input, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param create_edge_functions_alpha_input: (required)
        :type create_edge_functions_alpha_input: CreateEdgeFunctionsAlphaInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateEdgeFunctions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_edge_functions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_edge_functions_with_http_info(source_id, create_edge_functions_alpha_input, **kwargs)  # noqa: E501

    @validate_arguments
    def create_edge_functions_with_http_info(self, source_id : constr(strict=True), create_edge_functions_alpha_input : CreateEdgeFunctionsAlphaInput, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Edge Functions  # noqa: E501

        Create EdgeFunctions for your Source given a valid upload URL for an Edge Functions bundle.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_edge_functions_with_http_info(source_id, create_edge_functions_alpha_input, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param create_edge_functions_alpha_input: (required)
        :type create_edge_functions_alpha_input: CreateEdgeFunctionsAlphaInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CreateEdgeFunctions200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'source_id',
            'create_edge_functions_alpha_input'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_edge_functions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['source_id']:
            _path_params['sourceId'] = _params['source_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_edge_functions_alpha_input'] is not None:
            _body_params = _params['create_edge_functions_alpha_input']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1alpha+json', 'application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/vnd.segment.v1alpha+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "CreateEdgeFunctions200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/sources/{sourceId}/edge-functions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def disable_edge_functions(self, source_id : constr(strict=True), **kwargs) -> DisableEdgeFunctions200Response:  # noqa: E501
        """Disable Edge Functions  # noqa: E501

        Disable Edge Functions for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_edge_functions(source_id, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DisableEdgeFunctions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the disable_edge_functions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.disable_edge_functions_with_http_info(source_id, **kwargs)  # noqa: E501

    @validate_arguments
    def disable_edge_functions_with_http_info(self, source_id : constr(strict=True), **kwargs) -> ApiResponse:  # noqa: E501
        """Disable Edge Functions  # noqa: E501

        Disable Edge Functions for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_edge_functions_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DisableEdgeFunctions200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'source_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_edge_functions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['source_id']:
            _path_params['sourceId'] = _params['source_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1alpha+json', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "DisableEdgeFunctions200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/sources/{sourceId}/edge-functions/disable', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def generate_upload_url_for_edge_functions(self, source_id : constr(strict=True), **kwargs) -> GenerateUploadURLForEdgeFunctions200Response:  # noqa: E501
        """Generate Upload URL for Edge Functions  # noqa: E501

        Generate a temporary upload URL that can be used to upload an Edge Functions bundle.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_upload_url_for_edge_functions(source_id, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GenerateUploadURLForEdgeFunctions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the generate_upload_url_for_edge_functions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.generate_upload_url_for_edge_functions_with_http_info(source_id, **kwargs)  # noqa: E501

    @validate_arguments
    def generate_upload_url_for_edge_functions_with_http_info(self, source_id : constr(strict=True), **kwargs) -> ApiResponse:  # noqa: E501
        """Generate Upload URL for Edge Functions  # noqa: E501

        Generate a temporary upload URL that can be used to upload an Edge Functions bundle.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.generate_upload_url_for_edge_functions_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GenerateUploadURLForEdgeFunctions200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'source_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_upload_url_for_edge_functions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['source_id']:
            _path_params['sourceId'] = _params['source_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1alpha+json', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "GenerateUploadURLForEdgeFunctions200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/sources/{sourceId}/edge-functions/upload-url', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_latest_from_edge_functions(self, source_id : constr(strict=True), **kwargs) -> GetLatestFromEdgeFunctions200Response:  # noqa: E501
        """Get Latest from Edge Functions  # noqa: E501

        Get the latest Edge Functions for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_from_edge_functions(source_id, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetLatestFromEdgeFunctions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_latest_from_edge_functions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_latest_from_edge_functions_with_http_info(source_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_latest_from_edge_functions_with_http_info(self, source_id : constr(strict=True), **kwargs) -> ApiResponse:  # noqa: E501
        """Get Latest from Edge Functions  # noqa: E501

        Get the latest Edge Functions for your Source.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending an email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Edge Functions feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_latest_from_edge_functions_with_http_info(source_id, async_req=True)
        >>> result = thread.get()

        :param source_id: (required)
        :type source_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetLatestFromEdgeFunctions200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'source_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_from_edge_functions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['source_id']:
            _path_params['sourceId'] = _params['source_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1alpha+json', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "GetLatestFromEdgeFunctions200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/sources/{sourceId}/edge-functions/latest', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
