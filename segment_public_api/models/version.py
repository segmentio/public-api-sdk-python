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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class Version(BaseModel):
    """
    Represents a Function Version in a list.  # noqa: E501
    """
    id: StrictStr = Field(..., description="An identifier for this version.")
    author: Optional[StrictStr] = Field(None, description="Author of this version.")
    code: StrictStr = Field(..., description="Source code of this version.")
    is_deployed: Optional[StrictBool] = Field(None, alias="isDeployed", description="The deployed status of this version.")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt", description="The time of this Version's creation.")
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt", description="The time of this Version's latest update.")
    deployed_at: Optional[StrictStr] = Field(None, alias="deployedAt", description="The time of this Version's last deployment.")
    __properties = ["id", "author", "code", "isDeployed", "createdAt", "updatedAt", "deployedAt"]

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
    def from_json(cls, json_str: str) -> Version:
        """Create an instance of Version from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Version:
        """Create an instance of Version from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Version.parse_obj(obj)

        _obj = Version.parse_obj({
            "id": obj.get("id"),
            "author": obj.get("author"),
            "code": obj.get("code"),
            "is_deployed": obj.get("isDeployed"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "deployed_at": obj.get("deployedAt")
        })
        return _obj


