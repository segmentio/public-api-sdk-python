# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.1.1
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class CreateFilterForSpaceInput(BaseModel):
    """
    Input for CreateFilter.  # noqa: E501
    """
    integration_id: StrictStr = Field(..., alias="integrationId", description="The Space id to filter on.")
    enabled: Optional[StrictBool] = Field(None, description="Whether the filter is enabled.")
    name: StrictStr = Field(..., description="The name of the filter.")
    description: Optional[StrictStr] = Field(None, description="The description of the filter.")
    var_if: StrictStr = Field(..., alias="if", description="The \"if\" statement for a filter.")
    drop: Optional[StrictBool] = Field(None, description="Whether the event is dropped.")
    __properties = ["integrationId", "enabled", "name", "description", "if", "drop"]

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
    def from_json(cls, json_str: str) -> CreateFilterForSpaceInput:
        """Create an instance of CreateFilterForSpaceInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateFilterForSpaceInput:
        """Create an instance of CreateFilterForSpaceInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateFilterForSpaceInput.parse_obj(obj)

        _obj = CreateFilterForSpaceInput.parse_obj({
            "integration_id": obj.get("integrationId"),
            "enabled": obj.get("enabled"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "var_if": obj.get("if"),
            "drop": obj.get("drop")
        })
        return _obj


