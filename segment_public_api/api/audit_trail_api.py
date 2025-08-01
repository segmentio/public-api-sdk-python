# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.13.0
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

from typing import Optional

from segment_public_api.models.list_audit_events200_response import ListAuditEvents200Response
from segment_public_api.models.pagination_input import PaginationInput

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuditTrailApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def list_audit_events(self, start_time : Annotated[Optional[StrictStr], Field(description="Filter response to events that happened after this time.  This parameter exists in v1.")] = None, end_time : Annotated[Optional[StrictStr], Field(description="Filter response to events that happened before this time. Defaults to the current time, or the end time from the pagination cursor.  This parameter exists in v1.")] = None, resource_id : Annotated[Optional[StrictStr], Field(description="Filter response to events that affect a specific resource, for example, a single Source.  This parameter exists in v1.")] = None, resource_type : Annotated[Optional[StrictStr], Field(description="Filter response to events that affect a specific type, for example, Sources, Warehouses, and Tracking Plans.  This parameter exists in v1.")] = None, pagination : Annotated[Optional[PaginationInput], Field(description="Defines the pagination parameters.  This parameter exists in v1.")] = None, **kwargs) -> ListAuditEvents200Response:  # noqa: E501
        """List Audit Events  # noqa: E501

        Returns a list of Audit Trail events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_audit_events(start_time, end_time, resource_id, resource_type, pagination, async_req=True)
        >>> result = thread.get()

        :param start_time: Filter response to events that happened after this time.  This parameter exists in v1.
        :type start_time: str
        :param end_time: Filter response to events that happened before this time. Defaults to the current time, or the end time from the pagination cursor.  This parameter exists in v1.
        :type end_time: str
        :param resource_id: Filter response to events that affect a specific resource, for example, a single Source.  This parameter exists in v1.
        :type resource_id: str
        :param resource_type: Filter response to events that affect a specific type, for example, Sources, Warehouses, and Tracking Plans.  This parameter exists in v1.
        :type resource_type: str
        :param pagination: Defines the pagination parameters.  This parameter exists in v1.
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
        :rtype: ListAuditEvents200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_audit_events_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_audit_events_with_http_info(start_time, end_time, resource_id, resource_type, pagination, **kwargs)  # noqa: E501

    @validate_arguments
    def list_audit_events_with_http_info(self, start_time : Annotated[Optional[StrictStr], Field(description="Filter response to events that happened after this time.  This parameter exists in v1.")] = None, end_time : Annotated[Optional[StrictStr], Field(description="Filter response to events that happened before this time. Defaults to the current time, or the end time from the pagination cursor.  This parameter exists in v1.")] = None, resource_id : Annotated[Optional[StrictStr], Field(description="Filter response to events that affect a specific resource, for example, a single Source.  This parameter exists in v1.")] = None, resource_type : Annotated[Optional[StrictStr], Field(description="Filter response to events that affect a specific type, for example, Sources, Warehouses, and Tracking Plans.  This parameter exists in v1.")] = None, pagination : Annotated[Optional[PaginationInput], Field(description="Defines the pagination parameters.  This parameter exists in v1.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Audit Events  # noqa: E501

        Returns a list of Audit Trail events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_audit_events_with_http_info(start_time, end_time, resource_id, resource_type, pagination, async_req=True)
        >>> result = thread.get()

        :param start_time: Filter response to events that happened after this time.  This parameter exists in v1.
        :type start_time: str
        :param end_time: Filter response to events that happened before this time. Defaults to the current time, or the end time from the pagination cursor.  This parameter exists in v1.
        :type end_time: str
        :param resource_id: Filter response to events that affect a specific resource, for example, a single Source.  This parameter exists in v1.
        :type resource_id: str
        :param resource_type: Filter response to events that affect a specific type, for example, Sources, Warehouses, and Tracking Plans.  This parameter exists in v1.
        :type resource_type: str
        :param pagination: Defines the pagination parameters.  This parameter exists in v1.
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
        :rtype: tuple(ListAuditEvents200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'start_time',
            'end_time',
            'resource_id',
            'resource_type',
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
                    " to method list_audit_events" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('start_time') is not None:  # noqa: E501
            _query_params.append(('startTime', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            _query_params.append(('endTime', _params['end_time']))

        if _params.get('resource_id') is not None:  # noqa: E501
            _query_params.append(('resourceId', _params['resource_id']))

        if _params.get('resource_type') is not None:  # noqa: E501
            _query_params.append(('resourceType', _params['resource_type']))

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
            '200': "ListAuditEvents200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/audit-events', 'GET',
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
