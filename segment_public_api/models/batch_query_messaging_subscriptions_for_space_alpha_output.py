# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.4.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from segment_public_api.models.get_messaging_subscription_failure_response import GetMessagingSubscriptionFailureResponse
from segment_public_api.models.get_messaging_subscription_success_response import GetMessagingSubscriptionSuccessResponse
from segment_public_api.models.message_subscription_response_error import MessageSubscriptionResponseError
from segment_public_api.models.pagination_output import PaginationOutput

class BatchQueryMessagingSubscriptionsForSpaceAlphaOutput(BaseModel):
    """
    Batch get response.  # noqa: E501
    """
    successes: conlist(GetMessagingSubscriptionSuccessResponse) = Field(..., description="Array of successful subscription status.")
    failures: conlist(GetMessagingSubscriptionFailureResponse) = Field(..., description="Validation errors due to invalid types or email/phone numbers.")
    errors: conlist(MessageSubscriptionResponseError) = Field(..., description="General errors when making the request such as invalid payload or wrong http method errors.")
    pagination: Optional[PaginationOutput] = None
    __properties = ["successes", "failures", "errors", "pagination"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BatchQueryMessagingSubscriptionsForSpaceAlphaOutput:
        """Create an instance of BatchQueryMessagingSubscriptionsForSpaceAlphaOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in successes (list)
        _items = []
        if self.successes:
            for _item in self.successes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['successes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in failures (list)
        _items = []
        if self.failures:
            for _item in self.failures:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failures'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BatchQueryMessagingSubscriptionsForSpaceAlphaOutput:
        """Create an instance of BatchQueryMessagingSubscriptionsForSpaceAlphaOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BatchQueryMessagingSubscriptionsForSpaceAlphaOutput.parse_obj(obj)

        _obj = BatchQueryMessagingSubscriptionsForSpaceAlphaOutput.parse_obj({
            "successes": [GetMessagingSubscriptionSuccessResponse.from_dict(_item) for _item in obj.get("successes")] if obj.get("successes") is not None else None,
            "failures": [GetMessagingSubscriptionFailureResponse.from_dict(_item) for _item in obj.get("failures")] if obj.get("failures") is not None else None,
            "errors": [MessageSubscriptionResponseError.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None,
            "pagination": PaginationOutput.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None
        })
        return _obj


