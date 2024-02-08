# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 42.0.0
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
from segment_public_api.models.function_setting_v1 import FunctionSettingV1

class UpdateFunctionV1Input(BaseModel):
    """
    Update a Function.  # noqa: E501
    """
    code: Optional[StrictStr] = Field(None, description="The Function code.")
    settings: Optional[conlist(FunctionSettingV1)] = Field(None, description="The list of settings for this Function.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="A display name for this Function.")
    logo_url: Optional[StrictStr] = Field(None, alias="logoUrl", description="A logo for this Function.")
    description: Optional[StrictStr] = Field(None, description="A description for this Function.")
    __properties = ["code", "settings", "displayName", "logoUrl", "description"]

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
    def from_json(cls, json_str: str) -> UpdateFunctionV1Input:
        """Create an instance of UpdateFunctionV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in settings (list)
        _items = []
        if self.settings:
            for _item in self.settings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['settings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateFunctionV1Input:
        """Create an instance of UpdateFunctionV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateFunctionV1Input.parse_obj(obj)

        _obj = UpdateFunctionV1Input.parse_obj({
            "code": obj.get("code"),
            "settings": [FunctionSettingV1.from_dict(_item) for _item in obj.get("settings")] if obj.get("settings") is not None else None,
            "display_name": obj.get("displayName"),
            "logo_url": obj.get("logoUrl"),
            "description": obj.get("description")
        })
        return _obj


