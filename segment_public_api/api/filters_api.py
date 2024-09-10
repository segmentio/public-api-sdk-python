# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 54.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, constr

from typing import Optional

from segment_public_api.models.create_filter200_response import CreateFilter200Response
from segment_public_api.models.create_filter_input import CreateFilterInput
from segment_public_api.models.delete_filter_by_id200_response import DeleteFilterById200Response
from segment_public_api.models.get_filter_by_id200_response import GetFilterById200Response
from segment_public_api.models.list_filters_by_integration_id200_response import ListFiltersByIntegrationId200Response
from segment_public_api.models.list_filters_pagination_input import ListFiltersPaginationInput
from segment_public_api.models.update_filter_by_id200_response import UpdateFilterById200Response
from segment_public_api.models.update_filter_by_id_input import UpdateFilterByIdInput

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FiltersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_filter(self, create_filter_input : CreateFilterInput, **kwargs) -> CreateFilter200Response:  # noqa: E501
        """Create Filter  # noqa: E501

        Creates a filter.    • When called, this endpoint may generate the `Filter Created` event in the [audit trail](/tag/Audit-Trail).         # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_filter(create_filter_input, async_req=True)
        >>> result = thread.get()

        :param create_filter_input: (required)
        :type create_filter_input: CreateFilterInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateFilter200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_filter_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_filter_with_http_info(create_filter_input, **kwargs)  # noqa: E501

    @validate_arguments
    def create_filter_with_http_info(self, create_filter_input : CreateFilterInput, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Filter  # noqa: E501

        Creates a filter.    • When called, this endpoint may generate the `Filter Created` event in the [audit trail](/tag/Audit-Trail).         # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_filter_with_http_info(create_filter_input, async_req=True)
        >>> result = thread.get()

        :param create_filter_input: (required)
        :type create_filter_input: CreateFilterInput
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
        :rtype: tuple(CreateFilter200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_filter_input'
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
                    " to method create_filter" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_filter_input'] is not None:
            _body_params = _params['create_filter_input']

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
            '200': "CreateFilter200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/filters', 'POST',
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
    def delete_filter_by_id(self, id : constr(strict=True), **kwargs) -> DeleteFilterById200Response:  # noqa: E501
        """Delete Filter By Id  # noqa: E501

        Deletes a filter by id.    • When called, this endpoint may generate the `Filter Deleted` event in the [audit trail](/tag/Audit-Trail).         # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_filter_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DeleteFilterById200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_filter_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_filter_by_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_filter_by_id_with_http_info(self, id : constr(strict=True), **kwargs) -> ApiResponse:  # noqa: E501
        """Delete Filter By Id  # noqa: E501

        Deletes a filter by id.    • When called, this endpoint may generate the `Filter Deleted` event in the [audit trail](/tag/Audit-Trail).         # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_filter_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
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
        :rtype: tuple(DeleteFilterById200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method delete_filter_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


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
            '200': "DeleteFilterById200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/filters/{id}', 'DELETE',
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
    def get_filter_by_id(self, id : constr(strict=True), **kwargs) -> GetFilterById200Response:  # noqa: E501
        """Get Filter By Id  # noqa: E501

        Gets a filter by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_filter_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetFilterById200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_filter_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_filter_by_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_filter_by_id_with_http_info(self, id : constr(strict=True), **kwargs) -> ApiResponse:  # noqa: E501
        """Get Filter By Id  # noqa: E501

        Gets a filter by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_filter_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
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
        :rtype: tuple(GetFilterById200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method get_filter_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


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
            '200': "GetFilterById200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/filters/{id}', 'GET',
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
    def list_filters_by_integration_id(self, integration_id : Annotated[StrictStr, Field(..., description="The integration id used to fetch filters.  This parameter exists in alpha.")], pagination : Annotated[Optional[ListFiltersPaginationInput], Field(description="Pagination parameters.  This parameter exists in alpha.")] = None, **kwargs) -> ListFiltersByIntegrationId200Response:  # noqa: E501
        """List Filters By Integration Id  # noqa: E501

        Lists filters by Integration id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_filters_by_integration_id(integration_id, pagination, async_req=True)
        >>> result = thread.get()

        :param integration_id: The integration id used to fetch filters.  This parameter exists in alpha. (required)
        :type integration_id: str
        :param pagination: Pagination parameters.  This parameter exists in alpha.
        :type pagination: ListFiltersPaginationInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListFiltersByIntegrationId200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_filters_by_integration_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_filters_by_integration_id_with_http_info(integration_id, pagination, **kwargs)  # noqa: E501

    @validate_arguments
    def list_filters_by_integration_id_with_http_info(self, integration_id : Annotated[StrictStr, Field(..., description="The integration id used to fetch filters.  This parameter exists in alpha.")], pagination : Annotated[Optional[ListFiltersPaginationInput], Field(description="Pagination parameters.  This parameter exists in alpha.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Filters By Integration Id  # noqa: E501

        Lists filters by Integration id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_filters_by_integration_id_with_http_info(integration_id, pagination, async_req=True)
        >>> result = thread.get()

        :param integration_id: The integration id used to fetch filters.  This parameter exists in alpha. (required)
        :type integration_id: str
        :param pagination: Pagination parameters.  This parameter exists in alpha.
        :type pagination: ListFiltersPaginationInput
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
        :rtype: tuple(ListFiltersByIntegrationId200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'integration_id',
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
                    " to method list_filters_by_integration_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('integration_id') is not None:  # noqa: E501
            _query_params.append(('integrationId', _params['integration_id']))

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
            '200': "ListFiltersByIntegrationId200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/filters', 'GET',
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
    def update_filter_by_id(self, id : constr(strict=True), update_filter_by_id_input : UpdateFilterByIdInput, **kwargs) -> UpdateFilterById200Response:  # noqa: E501
        """Update Filter By Id  # noqa: E501

        Updates a filter by id.    • When called, this endpoint may generate the `Filter Updated` event in the [audit trail](/tag/Audit-Trail).         # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_filter_by_id(id, update_filter_by_id_input, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param update_filter_by_id_input: (required)
        :type update_filter_by_id_input: UpdateFilterByIdInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UpdateFilterById200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the update_filter_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.update_filter_by_id_with_http_info(id, update_filter_by_id_input, **kwargs)  # noqa: E501

    @validate_arguments
    def update_filter_by_id_with_http_info(self, id : constr(strict=True), update_filter_by_id_input : UpdateFilterByIdInput, **kwargs) -> ApiResponse:  # noqa: E501
        """Update Filter By Id  # noqa: E501

        Updates a filter by id.    • When called, this endpoint may generate the `Filter Updated` event in the [audit trail](/tag/Audit-Trail).         # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_filter_by_id_with_http_info(id, update_filter_by_id_input, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: str
        :param update_filter_by_id_input: (required)
        :type update_filter_by_id_input: UpdateFilterByIdInput
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
        :rtype: tuple(UpdateFilterById200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'update_filter_by_id_input'
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
                    " to method update_filter_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_filter_by_id_input'] is not None:
            _body_params = _params['update_filter_by_id_input']

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
            '200': "UpdateFilterById200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/filters/{id}', 'PATCH',
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
