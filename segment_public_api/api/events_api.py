# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.5.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conlist

from typing import List, Optional

from segment_public_api.models.get_events_volume_from_workspace200_response import GetEventsVolumeFromWorkspace200Response
from segment_public_api.models.pagination_input import PaginationInput

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EventsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_events_volume_from_workspace(self, granularity : Annotated[StrictStr, Field(..., description="The size of each bucket in the requested window.  This parameter exists in v1.")], start_time : Annotated[StrictStr, Field(..., description="The ISO8601 formatted timestamp that corresponds to the beginning of the requested time frame, inclusive.  This parameter exists in v1.")], end_time : Annotated[StrictStr, Field(..., description="The ISO8601 formatted timestamp that corresponds to the end of the requested time frame, noninclusive. Segment recommends that you lag queries 1 minute behind clock time to reduce the risk for latency to impact the counts.  This parameter exists in v1.")], group_by : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A comma-delimited list of strings that represents the dimensions to group the result by. The options are: `eventName`, `eventType` and `source`.  This parameter exists in v1.")] = None, source_id : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given SourceIds.  This parameter exists in v1.")] = None, event_name : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given EventNames.  This parameter exists in v1.")] = None, event_type : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given EventTypes.  This parameter exists in v1.")] = None, app_version : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given AppVersions.  This parameter exists in v1.")] = None, pagination : Annotated[Optional[PaginationInput], Field(description="Pagination input for event volume by Workspace.  This parameter exists in v1.")] = None, **kwargs) -> GetEventsVolumeFromWorkspace200Response:  # noqa: E501
        """Get Events Volume from Workspace  # noqa: E501

        Enumerates the Workspace event volumes over time in minute increments.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events_volume_from_workspace(granularity, start_time, end_time, group_by, source_id, event_name, event_type, app_version, pagination, async_req=True)
        >>> result = thread.get()

        :param granularity: The size of each bucket in the requested window.  This parameter exists in v1. (required)
        :type granularity: str
        :param start_time: The ISO8601 formatted timestamp that corresponds to the beginning of the requested time frame, inclusive.  This parameter exists in v1. (required)
        :type start_time: str
        :param end_time: The ISO8601 formatted timestamp that corresponds to the end of the requested time frame, noninclusive. Segment recommends that you lag queries 1 minute behind clock time to reduce the risk for latency to impact the counts.  This parameter exists in v1. (required)
        :type end_time: str
        :param group_by: A comma-delimited list of strings that represents the dimensions to group the result by. The options are: `eventName`, `eventType` and `source`.  This parameter exists in v1.
        :type group_by: List[str]
        :param source_id: A list of strings which filters the results to the given SourceIds.  This parameter exists in v1.
        :type source_id: List[str]
        :param event_name: A list of strings which filters the results to the given EventNames.  This parameter exists in v1.
        :type event_name: List[str]
        :param event_type: A list of strings which filters the results to the given EventTypes.  This parameter exists in v1.
        :type event_type: List[str]
        :param app_version: A list of strings which filters the results to the given AppVersions.  This parameter exists in v1.
        :type app_version: List[str]
        :param pagination: Pagination input for event volume by Workspace.  This parameter exists in v1.
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
        :rtype: GetEventsVolumeFromWorkspace200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_events_volume_from_workspace_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_events_volume_from_workspace_with_http_info(granularity, start_time, end_time, group_by, source_id, event_name, event_type, app_version, pagination, **kwargs)  # noqa: E501

    @validate_arguments
    def get_events_volume_from_workspace_with_http_info(self, granularity : Annotated[StrictStr, Field(..., description="The size of each bucket in the requested window.  This parameter exists in v1.")], start_time : Annotated[StrictStr, Field(..., description="The ISO8601 formatted timestamp that corresponds to the beginning of the requested time frame, inclusive.  This parameter exists in v1.")], end_time : Annotated[StrictStr, Field(..., description="The ISO8601 formatted timestamp that corresponds to the end of the requested time frame, noninclusive. Segment recommends that you lag queries 1 minute behind clock time to reduce the risk for latency to impact the counts.  This parameter exists in v1.")], group_by : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A comma-delimited list of strings that represents the dimensions to group the result by. The options are: `eventName`, `eventType` and `source`.  This parameter exists in v1.")] = None, source_id : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given SourceIds.  This parameter exists in v1.")] = None, event_name : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given EventNames.  This parameter exists in v1.")] = None, event_type : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given EventTypes.  This parameter exists in v1.")] = None, app_version : Annotated[Optional[conlist(conlist(StrictStr))], Field(description="A list of strings which filters the results to the given AppVersions.  This parameter exists in v1.")] = None, pagination : Annotated[Optional[PaginationInput], Field(description="Pagination input for event volume by Workspace.  This parameter exists in v1.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Events Volume from Workspace  # noqa: E501

        Enumerates the Workspace event volumes over time in minute increments.   The rate limit for this endpoint is 60 requests per minute, which is lower than the default due to access pattern restrictions. Once reached, this endpoint will respond with the 429 HTTP status code with headers indicating the limit parameters. See [Rate Limiting](/#tag/Rate-Limits) for more information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events_volume_from_workspace_with_http_info(granularity, start_time, end_time, group_by, source_id, event_name, event_type, app_version, pagination, async_req=True)
        >>> result = thread.get()

        :param granularity: The size of each bucket in the requested window.  This parameter exists in v1. (required)
        :type granularity: str
        :param start_time: The ISO8601 formatted timestamp that corresponds to the beginning of the requested time frame, inclusive.  This parameter exists in v1. (required)
        :type start_time: str
        :param end_time: The ISO8601 formatted timestamp that corresponds to the end of the requested time frame, noninclusive. Segment recommends that you lag queries 1 minute behind clock time to reduce the risk for latency to impact the counts.  This parameter exists in v1. (required)
        :type end_time: str
        :param group_by: A comma-delimited list of strings that represents the dimensions to group the result by. The options are: `eventName`, `eventType` and `source`.  This parameter exists in v1.
        :type group_by: List[str]
        :param source_id: A list of strings which filters the results to the given SourceIds.  This parameter exists in v1.
        :type source_id: List[str]
        :param event_name: A list of strings which filters the results to the given EventNames.  This parameter exists in v1.
        :type event_name: List[str]
        :param event_type: A list of strings which filters the results to the given EventTypes.  This parameter exists in v1.
        :type event_type: List[str]
        :param app_version: A list of strings which filters the results to the given AppVersions.  This parameter exists in v1.
        :type app_version: List[str]
        :param pagination: Pagination input for event volume by Workspace.  This parameter exists in v1.
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
        :rtype: tuple(GetEventsVolumeFromWorkspace200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'granularity',
            'start_time',
            'end_time',
            'group_by',
            'source_id',
            'event_name',
            'event_type',
            'app_version',
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
                    " to method get_events_volume_from_workspace" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('granularity') is not None:  # noqa: E501
            _query_params.append(('granularity', _params['granularity']))

        if _params.get('start_time') is not None:  # noqa: E501
            _query_params.append(('startTime', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            _query_params.append(('endTime', _params['end_time']))

        if _params.get('group_by') is not None:  # noqa: E501
            _query_params.append(('groupBy', _params['group_by']))
            _collection_formats['groupBy'] = 'csv'

        if _params.get('source_id') is not None:  # noqa: E501
            _query_params.append(('sourceId', _params['source_id']))
            _collection_formats['sourceId'] = 'csv'

        if _params.get('event_name') is not None:  # noqa: E501
            _query_params.append(('eventName', _params['event_name']))
            _collection_formats['eventName'] = 'csv'

        if _params.get('event_type') is not None:  # noqa: E501
            _query_params.append(('eventType', _params['event_type']))
            _collection_formats['eventType'] = 'csv'

        if _params.get('app_version') is not None:  # noqa: E501
            _query_params.append(('appVersion', _params['app_version']))
            _collection_formats['appVersion'] = 'csv'

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
            '200': "GetEventsVolumeFromWorkspace200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/events/volume', 'GET',
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
