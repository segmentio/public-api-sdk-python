# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 55.1.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from segment_public_api.models.group_subscription_status import GroupSubscriptionStatus

class MessagesSubscriptionRequest(BaseModel):
    """
    MessagesSubscriptionRequest
    """
    key: StrictStr = Field(..., description="Key is the phone number or email.")
    type: StrictStr = Field(..., description="Type is communication medium used.")
    status: Optional[StrictStr] = Field(None, description="The user subscribed, unsubscribed, or on initial status globally.")
    groups: Optional[conlist(GroupSubscriptionStatus)] = Field(None, description="Optional groups subscription status.")
    __properties = ["key", "type", "status", "groups"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ANDROID_PUSH', 'EMAIL', 'IOS_PUSH', 'SMS', 'WHATSAPP'):
            raise ValueError("must be one of enum values ('ANDROID_PUSH', 'EMAIL', 'IOS_PUSH', 'SMS', 'WHATSAPP')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DID_NOT_SUBSCRIBE', 'SUBSCRIBED', 'UNSUBSCRIBED'):
            raise ValueError("must be one of enum values ('DID_NOT_SUBSCRIBE', 'SUBSCRIBED', 'UNSUBSCRIBED')")
        return value

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
    def from_json(cls, json_str: str) -> MessagesSubscriptionRequest:
        """Create an instance of MessagesSubscriptionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item in self.groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['groups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessagesSubscriptionRequest:
        """Create an instance of MessagesSubscriptionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessagesSubscriptionRequest.parse_obj(obj)

        _obj = MessagesSubscriptionRequest.parse_obj({
            "key": obj.get("key"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "groups": [GroupSubscriptionStatus.from_dict(_item) for _item in obj.get("groups")] if obj.get("groups") is not None else None
        })
        return _obj


