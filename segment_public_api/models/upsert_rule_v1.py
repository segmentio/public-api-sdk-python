# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.3.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class UpsertRuleV1(BaseModel):
    """
    UpsertRuleV1
    """
    new_key: Optional[StrictStr] = Field(None, alias="newKey", description="This rule's new intended key.")
    type: StrictStr = Field(..., description="The type for this Tracking Plan rule.")
    key: Optional[StrictStr] = Field(None, description="Key to this rule (free-form string like 'Button clicked').")
    json_schema: Optional[Any] = Field(..., alias="jsonSchema", description="JSON Schema of this rule.")
    version: Union[StrictFloat, StrictInt] = Field(..., description="Version of this rule.")
    __properties = ["newKey", "type", "key", "jsonSchema", "version"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('COMMON', 'GROUP', 'IDENTIFY', 'PAGE', 'SCREEN', 'TRACK'):
            raise ValueError("must be one of enum values ('COMMON', 'GROUP', 'IDENTIFY', 'PAGE', 'SCREEN', 'TRACK')")
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
    def from_json(cls, json_str: str) -> UpsertRuleV1:
        """Create an instance of UpsertRuleV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if json_schema (nullable) is None
        # and __fields_set__ contains the field
        if self.json_schema is None and "json_schema" in self.__fields_set__:
            _dict['jsonSchema'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpsertRuleV1:
        """Create an instance of UpsertRuleV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpsertRuleV1.parse_obj(obj)

        _obj = UpsertRuleV1.parse_obj({
            "new_key": obj.get("newKey"),
            "type": obj.get("type"),
            "key": obj.get("key"),
            "json_schema": obj.get("jsonSchema"),
            "version": obj.get("version")
        })
        return _obj


