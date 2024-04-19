# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class GroupSubscriptionStatusResponse(BaseModel):
    """
    GroupSubscriptionStatusResponse
    """
    name: StrictStr = Field(..., description="Name of the group.")
    status: StrictStr = Field(..., description="The user subscribed, unsubscribed, or on initial status.")
    id: StrictStr = Field(..., description="The group id.")
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt", description="The timestamp of this subscription status's last change.")
    __properties = ["name", "status", "id", "updatedAt"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
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
    def from_json(cls, json_str: str) -> GroupSubscriptionStatusResponse:
        """Create an instance of GroupSubscriptionStatusResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GroupSubscriptionStatusResponse:
        """Create an instance of GroupSubscriptionStatusResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GroupSubscriptionStatusResponse.parse_obj(obj)

        _obj = GroupSubscriptionStatusResponse.parse_obj({
            "name": obj.get("name"),
            "status": obj.get("status"),
            "id": obj.get("id"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


