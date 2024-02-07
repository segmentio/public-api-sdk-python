# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 40.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr

from typing import Optional, Union

from segment_public_api.models.echo200_response import Echo200Response

from segment_public_api.api_client import ApiClient
from segment_public_api.api_response import ApiResponse
from segment_public_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TestingApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def echo(self, message : Annotated[StrictStr, Field(..., description="Sets the response `message` field. The response contains this field's entry.  This parameter exists in alpha.")], delay : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="The desired response delay, in milliseconds.  This parameter exists in alpha.")] = None, trigger_error : Annotated[Optional[StrictBool], Field(description="If `true`, returns an HTTP `4xx` error that contains the string in `message`.  This parameter exists in alpha.")] = None, trigger_multiple_errors : Annotated[Optional[StrictBool], Field(description="If `true`, returns an HTTP `4xx` error that contains the value of the `message` field in the error message array.  This has no effect if the request sets `triggerError`.  This parameter exists in alpha.")] = None, trigger_unexpected_error : Annotated[Optional[StrictBool], Field(description="If `true`, triggers a `500` error.  This has no effect if the request sets either `triggerError` or `triggerMultipleErrors`.  This parameter exists in alpha.")] = None, status_code : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Sets the HTTP status code to return.  This parameter exists in alpha.")] = None, **kwargs) -> Echo200Response:  # noqa: E501
        """Echo  # noqa: E501

        Public Echo endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.echo(message, delay, trigger_error, trigger_multiple_errors, trigger_unexpected_error, status_code, async_req=True)
        >>> result = thread.get()

        :param message: Sets the response `message` field. The response contains this field's entry.  This parameter exists in alpha. (required)
        :type message: str
        :param delay: The desired response delay, in milliseconds.  This parameter exists in alpha.
        :type delay: float
        :param trigger_error: If `true`, returns an HTTP `4xx` error that contains the string in `message`.  This parameter exists in alpha.
        :type trigger_error: bool
        :param trigger_multiple_errors: If `true`, returns an HTTP `4xx` error that contains the value of the `message` field in the error message array.  This has no effect if the request sets `triggerError`.  This parameter exists in alpha.
        :type trigger_multiple_errors: bool
        :param trigger_unexpected_error: If `true`, triggers a `500` error.  This has no effect if the request sets either `triggerError` or `triggerMultipleErrors`.  This parameter exists in alpha.
        :type trigger_unexpected_error: bool
        :param status_code: Sets the HTTP status code to return.  This parameter exists in alpha.
        :type status_code: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Echo200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the echo_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.echo_with_http_info(message, delay, trigger_error, trigger_multiple_errors, trigger_unexpected_error, status_code, **kwargs)  # noqa: E501

    @validate_arguments
    def echo_with_http_info(self, message : Annotated[StrictStr, Field(..., description="Sets the response `message` field. The response contains this field's entry.  This parameter exists in alpha.")], delay : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="The desired response delay, in milliseconds.  This parameter exists in alpha.")] = None, trigger_error : Annotated[Optional[StrictBool], Field(description="If `true`, returns an HTTP `4xx` error that contains the string in `message`.  This parameter exists in alpha.")] = None, trigger_multiple_errors : Annotated[Optional[StrictBool], Field(description="If `true`, returns an HTTP `4xx` error that contains the value of the `message` field in the error message array.  This has no effect if the request sets `triggerError`.  This parameter exists in alpha.")] = None, trigger_unexpected_error : Annotated[Optional[StrictBool], Field(description="If `true`, triggers a `500` error.  This has no effect if the request sets either `triggerError` or `triggerMultipleErrors`.  This parameter exists in alpha.")] = None, status_code : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Sets the HTTP status code to return.  This parameter exists in alpha.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Echo  # noqa: E501

        Public Echo endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.echo_with_http_info(message, delay, trigger_error, trigger_multiple_errors, trigger_unexpected_error, status_code, async_req=True)
        >>> result = thread.get()

        :param message: Sets the response `message` field. The response contains this field's entry.  This parameter exists in alpha. (required)
        :type message: str
        :param delay: The desired response delay, in milliseconds.  This parameter exists in alpha.
        :type delay: float
        :param trigger_error: If `true`, returns an HTTP `4xx` error that contains the string in `message`.  This parameter exists in alpha.
        :type trigger_error: bool
        :param trigger_multiple_errors: If `true`, returns an HTTP `4xx` error that contains the value of the `message` field in the error message array.  This has no effect if the request sets `triggerError`.  This parameter exists in alpha.
        :type trigger_multiple_errors: bool
        :param trigger_unexpected_error: If `true`, triggers a `500` error.  This has no effect if the request sets either `triggerError` or `triggerMultipleErrors`.  This parameter exists in alpha.
        :type trigger_unexpected_error: bool
        :param status_code: Sets the HTTP status code to return.  This parameter exists in alpha.
        :type status_code: float
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
        :rtype: tuple(Echo200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'message',
            'delay',
            'trigger_error',
            'trigger_multiple_errors',
            'trigger_unexpected_error',
            'status_code'
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
                    " to method echo" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('message') is not None:  # noqa: E501
            _query_params.append(('message', _params['message']))

        if _params.get('delay') is not None:  # noqa: E501
            _query_params.append(('delay', _params['delay']))

        if _params.get('trigger_error') is not None:  # noqa: E501
            _query_params.append(('triggerError', _params['trigger_error']))

        if _params.get('trigger_multiple_errors') is not None:  # noqa: E501
            _query_params.append(('triggerMultipleErrors', _params['trigger_multiple_errors']))

        if _params.get('trigger_unexpected_error') is not None:  # noqa: E501
            _query_params.append(('triggerUnexpectedError', _params['trigger_unexpected_error']))

        if _params.get('status_code') is not None:  # noqa: E501
            _query_params.append(('statusCode', _params['status_code']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.segment.v1+json', 'application/json', 'application/vnd.segment.v1alpha+json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['token']  # noqa: E501

        _response_types_map = {
            '200': "Echo200Response",
            '404': "RequestErrorEnvelope",
            '422': "RequestErrorEnvelope",
            '429': "RequestErrorEnvelope",
        }

        return self.api_client.call_api(
            '/echo', 'GET',
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
