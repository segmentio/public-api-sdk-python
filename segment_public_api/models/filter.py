# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.2.0
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

class Filter(BaseModel):
    """
    Filter output.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The newly created filter id.")
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="The Workspace id to create the filter.")
    integration_id: StrictStr = Field(..., alias="integrationId", description="The Integration id of the resource.")
    enabled: Optional[StrictBool] = Field(None, description="Whether the filter is enabled.")
    name: Optional[StrictStr] = Field(None, description="The name of the filter.")
    description: Optional[StrictStr] = Field(None, description="The description of the filter.")
    var_if: Optional[StrictStr] = Field(None, alias="if", description="The \"if\" statement for a filter.")
    drop: Optional[StrictBool] = Field(None, description="Whether the event is dropped.")
    created_at: StrictStr = Field(..., alias="createdAt", description="The timestamp of this filter's creation.")
    updated_at: StrictStr = Field(..., alias="updatedAt", description="The timestamp of this filter's last change.")
    __properties = ["id", "workspaceId", "integrationId", "enabled", "name", "description", "if", "drop", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> Filter:
        """Create an instance of Filter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Filter:
        """Create an instance of Filter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Filter.parse_obj(obj)

        _obj = Filter.parse_obj({
            "id": obj.get("id"),
            "workspace_id": obj.get("workspaceId"),
            "integration_id": obj.get("integrationId"),
            "enabled": obj.get("enabled"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "var_if": obj.get("if"),
            "drop": obj.get("drop"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


