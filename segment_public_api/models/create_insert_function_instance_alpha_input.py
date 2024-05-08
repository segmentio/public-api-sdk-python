# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.2.0
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

class CreateInsertFunctionInstanceAlphaInput(BaseModel):
    """
    Creates an insert Function instance.  # noqa: E501
    """
    function_id: StrictStr = Field(..., alias="functionId", description="Insert Function id to which this instance is associated.")
    integration_id: StrictStr = Field(..., alias="integrationId", description="The Source or Destination id to be connected.")
    enabled: Optional[StrictBool] = Field(None, description="Whether this insert Function instance should be enabled for the Destination.")
    name: StrictStr = Field(..., description="Defines the display name of the insert Function instance.")
    settings: Dict[str, Any] = Field(..., description="An object that contains settings for this insert Function instance based on the settings present in the insert Function class.")
    __properties = ["functionId", "integrationId", "enabled", "name", "settings"]

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
    def from_json(cls, json_str: str) -> CreateInsertFunctionInstanceAlphaInput:
        """Create an instance of CreateInsertFunctionInstanceAlphaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateInsertFunctionInstanceAlphaInput:
        """Create an instance of CreateInsertFunctionInstanceAlphaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateInsertFunctionInstanceAlphaInput.parse_obj(obj)

        _obj = CreateInsertFunctionInstanceAlphaInput.parse_obj({
            "function_id": obj.get("functionId"),
            "integration_id": obj.get("integrationId"),
            "enabled": obj.get("enabled"),
            "name": obj.get("name"),
            "settings": obj.get("settings")
        })
        return _obj


