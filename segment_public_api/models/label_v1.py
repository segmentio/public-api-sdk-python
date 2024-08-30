# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 53.2.1
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

class LabelV1(BaseModel):
    """
    A label lets Workspace owners assign permissions to users, and grant these users access to groups.  A Workspace owner may use labels to grant users access to groups of resources.  When you add a label to a Source or Personas Spaces, any users granted access to that label gain access to those resources.  All Workspaces include labels for Dev (development) and Prod (production) environments. On top of those, Free and Team plan customers may create up to five labels.  Customers with the Enterprise pricing package may create an unlimited number of labels.  # noqa: E501
    """
    key: StrictStr = Field(..., description="The key that represents the name of this label.")
    value: StrictStr = Field(..., description="The value associated with the key of this label.")
    description: Optional[StrictStr] = Field(None, description="An optional description of the purpose of this label.")
    __properties = ["key", "value", "description"]

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
    def from_json(cls, json_str: str) -> LabelV1:
        """Create an instance of LabelV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LabelV1:
        """Create an instance of LabelV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LabelV1.parse_obj(obj)

        _obj = LabelV1.parse_obj({
            "key": obj.get("key"),
            "value": obj.get("value"),
            "description": obj.get("description")
        })
        return _obj


