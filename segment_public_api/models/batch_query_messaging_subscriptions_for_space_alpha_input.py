# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.13.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from segment_public_api.models.get_subscription_request import GetSubscriptionRequest

class BatchQueryMessagingSubscriptionsForSpaceAlphaInput(BaseModel):
    """
    Batch get request.  # noqa: E501
    """
    subscriptions: conlist(GetSubscriptionRequest) = Field(..., description="A list of subscriptions to retrieve subscription status.")
    __properties = ["subscriptions"]

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
    def from_json(cls, json_str: str) -> BatchQueryMessagingSubscriptionsForSpaceAlphaInput:
        """Create an instance of BatchQueryMessagingSubscriptionsForSpaceAlphaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in subscriptions (list)
        _items = []
        if self.subscriptions:
            for _item in self.subscriptions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subscriptions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BatchQueryMessagingSubscriptionsForSpaceAlphaInput:
        """Create an instance of BatchQueryMessagingSubscriptionsForSpaceAlphaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BatchQueryMessagingSubscriptionsForSpaceAlphaInput.parse_obj(obj)

        _obj = BatchQueryMessagingSubscriptionsForSpaceAlphaInput.parse_obj({
            "subscriptions": [GetSubscriptionRequest.from_dict(_item) for _item in obj.get("subscriptions")] if obj.get("subscriptions") is not None else None
        })
        return _obj


