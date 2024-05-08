# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, constr

from segment_public_api.models.batch_query_messaging_subscriptions_for_space200_response import BatchQueryMessagingSubscriptionsForSpace200Response
from segment_public_api.models.batch_query_messaging_subscriptions_for_space_alpha_input import BatchQueryMessagingSubscriptionsForSpaceAlphaInput
from segment_public_api.models.get_space200_response import GetSpace200Response
from segment_public_api.models.list_spaces200_response import ListSpaces200Response
from segment_public_api.models.pagination_input import PaginationInput
from segment_public_api.models.replace_messaging_subscriptions_in_spaces200_response import ReplaceMessagingSubscriptionsInSpaces200Response
from segment_public_api.models.replace_messaging_subscriptions_in_spaces_alpha_input import ReplaceMessagingSubscriptionsInSpacesAlphaInput

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SpacesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def batch_query_messaging_subscriptions_for_space(self, space_id : constr(strict=True), batch_query_messaging_subscriptions_for_space_alpha_input : BatchQueryMessagingSubscriptionsForSpaceAlphaInput, **kwargs) -> BatchQueryMessagingSubscriptionsForSpace200Response:  # noqa: E501
        """Batch Query Messaging Subscriptions for Space  # noqa: E501

        Get Messaging Subscriptions for space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.batch_query_messaging_subscriptions_for_space(space_id, batch_query_messaging_subscriptions_for_space_alpha_input, async_req=True)
        >>> result = thread.get()

        :param space_id: (required)
        :type space_id: str
        :param batch_query_messaging_subscriptions_for_space_alpha_input: (required)
        :type batch_query_messaging_subscriptions_for_space_alpha_input: BatchQueryMessagingSubscriptionsForSpaceAlphaInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BatchQueryMessagingSubscriptionsForSpace200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the batch_query_messaging_subscriptions_for_space_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.batch_query_messaging_subscriptions_for_space_with_http_info(space_id, batch_query_messaging_subscriptions_for_space_alpha_input, **kwargs)  # noqa: E501

    @validate_arguments
    def batch_query_messaging_subscriptions_for_space_with_http_info(self, space_id : constr(strict=True), batch_query_messaging_subscriptions_for_space_alpha_input : BatchQueryMessagingSubscriptionsForSpaceAlphaInput, **kwargs) -> ApiResponse:  # noqa: E501
        """Batch Query Messaging Subscriptions for Space  # noqa: E501

        Get Messaging Subscriptions for space.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.batch_query_messaging_subscriptions_for_space_with_http_info(space_id, batch_query_messaging_subscriptions_for_space_alpha_input, async_req=True)
        >>> result = thread.get()

        :param space_id: (required)
        :type space_id: str
        :param batch_query_messaging_subscriptions_for_space_alpha_input: (required)
        :type batch_query_messaging_subscriptions_for_space_alpha_input: BatchQueryMessagingSubscriptionsForSpaceAlphaInput
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
        :rtype: tuple(BatchQueryMessagingSubscriptionsForSpace200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'space_id',
            'batch_query_messaging_subscriptions_for_space_alpha_input'
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
                    " to method batch_query_messaging_subscriptions_for_space" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['space_id']:
            _path_params['spaceId'] = _params['space_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['batch_query_messaging_subscriptions_for_space_alpha_input'] is not None:
            _body_params = _params['batch_query_messaging_subscriptions_for_space_alpha_input']

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
            '200': "BatchQueryMessagingSubscriptionsForSpace200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/spaces/{spaceId}/messaging-subscriptions/batch', 'POST',
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
    def get_space(self, space_id : constr(strict=True), **kwargs) -> GetSpace200Response:  # noqa: E501
        """Get Space  # noqa: E501

        Returns the Space by id.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_space(space_id, async_req=True)
        >>> result = thread.get()

        :param space_id: (required)
        :type space_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetSpace200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_space_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_space_with_http_info(space_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_space_with_http_info(self, space_id : constr(strict=True), **kwargs) -> ApiResponse:  # noqa: E501
        """Get Space  # noqa: E501

        Returns the Space by id.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_space_with_http_info(space_id, async_req=True)
        >>> result = thread.get()

        :param space_id: (required)
        :type space_id: str
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
        :rtype: tuple(GetSpace200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'space_id'
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
                    " to method get_space" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['space_id']:
            _path_params['spaceId'] = _params['space_id']


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
            '200': "GetSpace200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/spaces/{spaceId}', 'GET',
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
    def list_spaces(self, pagination : Annotated[PaginationInput, Field(..., description="Pagination params  This parameter exists in alpha.")], **kwargs) -> ListSpaces200Response:  # noqa: E501
        """List Spaces  # noqa: E501

        List Spaces.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_spaces(pagination, async_req=True)
        >>> result = thread.get()

        :param pagination: Pagination params  This parameter exists in alpha. (required)
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
        :rtype: ListSpaces200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_spaces_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_spaces_with_http_info(pagination, **kwargs)  # noqa: E501

    @validate_arguments
    def list_spaces_with_http_info(self, pagination : Annotated[PaginationInput, Field(..., description="Pagination params  This parameter exists in alpha.")], **kwargs) -> ApiResponse:  # noqa: E501
        """List Spaces  # noqa: E501

        List Spaces.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_spaces_with_http_info(pagination, async_req=True)
        >>> result = thread.get()

        :param pagination: Pagination params  This parameter exists in alpha. (required)
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
        :rtype: tuple(ListSpaces200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method list_spaces" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
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
            ['application/vnd.segment.v1alpha+json', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "ListSpaces200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/spaces', 'GET',
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
    def replace_messaging_subscriptions_in_spaces(self, space_id : constr(strict=True), replace_messaging_subscriptions_in_spaces_alpha_input : ReplaceMessagingSubscriptionsInSpacesAlphaInput, **kwargs) -> ReplaceMessagingSubscriptionsInSpaces200Response:  # noqa: E501
        """Replace Messaging Subscriptions in Spaces  # noqa: E501

        Replace Messaging Subscriptions in Spaces.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_messaging_subscriptions_in_spaces(space_id, replace_messaging_subscriptions_in_spaces_alpha_input, async_req=True)
        >>> result = thread.get()

        :param space_id: (required)
        :type space_id: str
        :param replace_messaging_subscriptions_in_spaces_alpha_input: (required)
        :type replace_messaging_subscriptions_in_spaces_alpha_input: ReplaceMessagingSubscriptionsInSpacesAlphaInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ReplaceMessagingSubscriptionsInSpaces200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the replace_messaging_subscriptions_in_spaces_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.replace_messaging_subscriptions_in_spaces_with_http_info(space_id, replace_messaging_subscriptions_in_spaces_alpha_input, **kwargs)  # noqa: E501

    @validate_arguments
    def replace_messaging_subscriptions_in_spaces_with_http_info(self, space_id : constr(strict=True), replace_messaging_subscriptions_in_spaces_alpha_input : ReplaceMessagingSubscriptionsInSpacesAlphaInput, **kwargs) -> ApiResponse:  # noqa: E501
        """Replace Messaging Subscriptions in Spaces  # noqa: E501

        Replace Messaging Subscriptions in Spaces.  • This endpoint is in **Alpha** testing.  Please submit any feedback by sending email to friends@segment.com.   • In order to successfully call this endpoint, the specified Workspace needs to have the Spaces feature enabled. Please reach out to your customer success manager for more information.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_messaging_subscriptions_in_spaces_with_http_info(space_id, replace_messaging_subscriptions_in_spaces_alpha_input, async_req=True)
        >>> result = thread.get()

        :param space_id: (required)
        :type space_id: str
        :param replace_messaging_subscriptions_in_spaces_alpha_input: (required)
        :type replace_messaging_subscriptions_in_spaces_alpha_input: ReplaceMessagingSubscriptionsInSpacesAlphaInput
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
        :rtype: tuple(ReplaceMessagingSubscriptionsInSpaces200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'space_id',
            'replace_messaging_subscriptions_in_spaces_alpha_input'
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
                    " to method replace_messaging_subscriptions_in_spaces" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['space_id']:
            _path_params['spaceId'] = _params['space_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['replace_messaging_subscriptions_in_spaces_alpha_input'] is not None:
            _body_params = _params['replace_messaging_subscriptions_in_spaces_alpha_input']

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
            '200': "ReplaceMessagingSubscriptionsInSpaces200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/spaces/{spaceId}/messaging-subscriptions', 'PUT',
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
