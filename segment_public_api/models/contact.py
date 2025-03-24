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

class Contact(BaseModel):
    """
    The contact info for Integration Owners.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Name of this contact.")
    email: StrictStr = Field(..., description="Email of this contact.")
    role: Optional[StrictStr] = Field(None, description="Role of this contact.")
    is_primary: Optional[StrictBool] = Field(None, alias="isPrimary", description="Whether this is a primary contact.")
    __properties = ["name", "email", "role", "isPrimary"]

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
    def from_json(cls, json_str: str) -> Contact:
        """Create an instance of Contact from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Contact:
        """Create an instance of Contact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Contact.parse_obj(obj)

        _obj = Contact.parse_obj({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "role": obj.get("role"),
            "is_primary": obj.get("isPrimary")
        })
        return _obj


