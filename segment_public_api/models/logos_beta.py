# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 36.3.1
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class LogosBeta(BaseModel):
    """
    Represents a logo.  # noqa: E501
    """
    default: StrictStr = Field(..., description="The default URL for this logo.")
    mark: Optional[StrictStr] = Field(None, description="The logo mark.")
    alt: Optional[StrictStr] = Field(None, description="The alternative text for this logo.")
    __properties = ["default", "mark", "alt"]

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
    def from_json(cls, json_str: str) -> LogosBeta:
        """Create an instance of LogosBeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if mark (nullable) is None
        # and __fields_set__ contains the field
        if self.mark is None and "mark" in self.__fields_set__:
            _dict['mark'] = None

        # set to None if alt (nullable) is None
        # and __fields_set__ contains the field
        if self.alt is None and "alt" in self.__fields_set__:
            _dict['alt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LogosBeta:
        """Create an instance of LogosBeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LogosBeta.parse_obj(obj)

        _obj = LogosBeta.parse_obj({
            "default": obj.get("default"),
            "mark": obj.get("mark"),
            "alt": obj.get("alt")
        })
        return _obj


