# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 54.3.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from segment_public_api.models.permission_v1 import PermissionV1

class UserV1(BaseModel):
    """
    A user belonging to a Segment Workspace.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The unique identifier of this user.  Config API note: analogous to `name`.")
    name: StrictStr = Field(..., description="The human-readable name of this user.")
    email: StrictStr = Field(..., description="The email address associated with this user.")
    permissions: Optional[conlist(PermissionV1)] = Field(None, description="The permissions associated with this user.")
    __properties = ["id", "name", "email", "permissions"]

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
    def from_json(cls, json_str: str) -> UserV1:
        """Create an instance of UserV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserV1:
        """Create an instance of UserV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserV1.parse_obj(obj)

        _obj = UserV1.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "permissions": [PermissionV1.from_dict(_item) for _item in obj.get("permissions")] if obj.get("permissions") is not None else None
        })
        return _obj


