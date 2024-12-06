# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.1.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class UpdateWarehouseV1Input(BaseModel):
    """
    Updates an existing Warehouse based on a set of parameters.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="An optional human-readable name to associate with this Warehouse.")
    enabled: Optional[StrictBool] = Field(None, description="Enable to allow this Warehouse to receive data.")
    settings: Dict[str, Any] = Field(..., description="A key-value object that contains instance-specific Warehouse settings.")
    __properties = ["name", "enabled", "settings"]

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
    def from_json(cls, json_str: str) -> UpdateWarehouseV1Input:
        """Create an instance of UpdateWarehouseV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateWarehouseV1Input:
        """Create an instance of UpdateWarehouseV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateWarehouseV1Input.parse_obj(obj)

        _obj = UpdateWarehouseV1Input.parse_obj({
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "settings": obj.get("settings")
        })
        return _obj


