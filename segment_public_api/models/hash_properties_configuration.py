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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class HashPropertiesConfiguration(BaseModel):
    """
    HashPropertiesConfiguration
    """
    algorithm: StrictStr = Field(..., description="Which algorithm to use to hash to properties.")
    key: Optional[StrictStr] = Field(None, description="Optional key to hash with.")
    encoding: Optional[StrictStr] = Field(None, description="Optional encoding to use for the hashing.")
    paths: conlist(StrictStr) = Field(..., description="The paths to the properties to be hashed.")
    __properties = ["algorithm", "key", "encoding", "paths"]

    @validator('encoding')
    def encoding_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BASE16', 'BASE64', 'BASE64URL', 'HEX'):
            raise ValueError("must be one of enum values ('BASE16', 'BASE64', 'BASE64URL', 'HEX')")
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
    def from_json(cls, json_str: str) -> HashPropertiesConfiguration:
        """Create an instance of HashPropertiesConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HashPropertiesConfiguration:
        """Create an instance of HashPropertiesConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HashPropertiesConfiguration.parse_obj(obj)

        _obj = HashPropertiesConfiguration.parse_obj({
            "algorithm": obj.get("algorithm"),
            "key": obj.get("key"),
            "encoding": obj.get("encoding"),
            "paths": obj.get("paths")
        })
        return _obj


