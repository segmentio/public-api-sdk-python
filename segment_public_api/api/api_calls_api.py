# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from segment_public_api.models.get_daily_per_source_api_calls_usage200_response import GetDailyPerSourceAPICallsUsage200Response
from segment_public_api.models.get_daily_workspace_api_calls_usage200_response import GetDailyWorkspaceAPICallsUsage200Response
from segment_public_api.models.pagination_input import PaginationInput

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class APICallsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_daily_per_source_api_calls_usage(self, period : Annotated[StrictStr, Field(..., description="The start of the usage month in the ISO-8601 format.  This parameter exists in v1.")], pagination : Annotated[PaginationInput, Field(..., description="Pagination input for per Source API calls counts.  This parameter exists in v1.")], **kwargs) -> GetDailyPerSourceAPICallsUsage200Response:  # noqa: E501
        """Get Daily Per Source API Calls Usage  # noqa: E501

        Provides daily cumulative per-source API call counts for a usage period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_daily_per_source_api_calls_usage(period, pagination, async_req=True)
        >>> result = thread.get()

        :param period: The start of the usage month in the ISO-8601 format.  This parameter exists in v1. (required)
        :type period: str
        :param pagination: Pagination input for per Source API calls counts.  This parameter exists in v1. (required)
        :type pagination: PaginationInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDailyPerSourceAPICallsUsage200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_daily_per_source_api_calls_usage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_daily_per_source_api_calls_usage_with_http_info(period, pagination, **kwargs)  # noqa: E501

    @validate_arguments
    def get_daily_per_source_api_calls_usage_with_http_info(self, period : Annotated[StrictStr, Field(..., description="The start of the usage month in the ISO-8601 format.  This parameter exists in v1.")], pagination : Annotated[PaginationInput, Field(..., description="Pagination input for per Source API calls counts.  This parameter exists in v1.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Daily Per Source API Calls Usage  # noqa: E501

        Provides daily cumulative per-source API call counts for a usage period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_daily_per_source_api_calls_usage_with_http_info(period, pagination, async_req=True)
        >>> result = thread.get()

        :param period: The start of the usage month in the ISO-8601 format.  This parameter exists in v1. (required)
        :type period: str
        :param pagination: Pagination input for per Source API calls counts.  This parameter exists in v1. (required)
        :type pagination: PaginationInput
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
        :rtype: tuple(GetDailyPerSourceAPICallsUsage200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'period',
            'pagination'
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
                    " to method get_daily_per_source_api_calls_usage" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('period') is not None:  # noqa: E501
            _query_params.append(('period', _params['period']))

        if _params.get('pagination') is not None:  # noqa: E501
            _query_params.append(('pagination', _params['pagination']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1+json', 'application/json', 'application/vnd.segment.v1beta+json', 'application/vnd.segment.v1alpha+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "GetDailyPerSourceAPICallsUsage200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/usage/api-calls/sources/daily', 'GET',
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
    def get_daily_workspace_api_calls_usage(self, period : Annotated[StrictStr, Field(..., description="The start of the usage month in the ISO-8601 format.  This parameter exists in v1.")], pagination : Annotated[PaginationInput, Field(..., description="Pagination input for Workspace API call counts.  This parameter exists in v1.")], **kwargs) -> GetDailyWorkspaceAPICallsUsage200Response:  # noqa: E501
        """Get Daily Workspace API Calls Usage  # noqa: E501

        Provides daily cumulative API call counts for a usage period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_daily_workspace_api_calls_usage(period, pagination, async_req=True)
        >>> result = thread.get()

        :param period: The start of the usage month in the ISO-8601 format.  This parameter exists in v1. (required)
        :type period: str
        :param pagination: Pagination input for Workspace API call counts.  This parameter exists in v1. (required)
        :type pagination: PaginationInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDailyWorkspaceAPICallsUsage200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_daily_workspace_api_calls_usage_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_daily_workspace_api_calls_usage_with_http_info(period, pagination, **kwargs)  # noqa: E501

    @validate_arguments
    def get_daily_workspace_api_calls_usage_with_http_info(self, period : Annotated[StrictStr, Field(..., description="The start of the usage month in the ISO-8601 format.  This parameter exists in v1.")], pagination : Annotated[PaginationInput, Field(..., description="Pagination input for Workspace API call counts.  This parameter exists in v1.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Daily Workspace API Calls Usage  # noqa: E501

        Provides daily cumulative API call counts for a usage period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_daily_workspace_api_calls_usage_with_http_info(period, pagination, async_req=True)
        >>> result = thread.get()

        :param period: The start of the usage month in the ISO-8601 format.  This parameter exists in v1. (required)
        :type period: str
        :param pagination: Pagination input for Workspace API call counts.  This parameter exists in v1. (required)
        :type pagination: PaginationInput
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
        :rtype: tuple(GetDailyWorkspaceAPICallsUsage200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'period',
            'pagination'
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
                    " to method get_daily_workspace_api_calls_usage" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('period') is not None:  # noqa: E501
            _query_params.append(('period', _params['period']))

        if _params.get('pagination') is not None:  # noqa: E501
            _query_params.append(('pagination', _params['pagination']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1+json', 'application/json', 'application/vnd.segment.v1beta+json', 'application/vnd.segment.v1alpha+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "GetDailyWorkspaceAPICallsUsage200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/usage/api-calls/daily', 'GET',
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
