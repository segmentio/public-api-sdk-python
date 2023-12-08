# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.4.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class DestinationFilterActionV1(BaseModel):
    """
    Represents a Destination filter action.  # noqa: E501
    """
    type: StrictStr = Field(..., description="The kind of Transformation to apply to any matched properties.")
    fields: Optional[Dict[str, Any]] = Field(None, description="A dictionary of paths to object keys that this filter applies to.  The literal string '' represents the top level of the object.")
    percent: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="A decimal between 0 and 1 used for 'sample' type events and influences the likelihood of sampling to occur.")
    path: Optional[StrictStr] = Field(None, description="The JSON path to a property within a payload object from which Segment generates a deterministic sampling rate.")
    __properties = ["type", "fields", "percent", "path"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ALLOW_PROPERTIES', 'DROP', 'DROP_PROPERTIES', 'SAMPLE'):
            raise ValueError("must be one of enum values ('ALLOW_PROPERTIES', 'DROP', 'DROP_PROPERTIES', 'SAMPLE')")
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
    def from_json(cls, json_str: str) -> DestinationFilterActionV1:
        """Create an instance of DestinationFilterActionV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationFilterActionV1:
        """Create an instance of DestinationFilterActionV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationFilterActionV1.parse_obj(obj)

        _obj = DestinationFilterActionV1.parse_obj({
            "type": obj.get("type"),
            "fields": obj.get("fields"),
            "percent": obj.get("percent"),
            "path": obj.get("path")
        })
        return _obj


