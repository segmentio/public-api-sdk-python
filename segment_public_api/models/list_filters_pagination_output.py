# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 54.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class ListFiltersPaginationOutput(BaseModel):
    """
    Pagination for list filters.  # noqa: E501
    """
    current: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Current.")
    next: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Next.")
    total_entries: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalEntries", description="Total entries.")
    __properties = ["current", "next", "totalEntries"]

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
    def from_json(cls, json_str: str) -> ListFiltersPaginationOutput:
        """Create an instance of ListFiltersPaginationOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListFiltersPaginationOutput:
        """Create an instance of ListFiltersPaginationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListFiltersPaginationOutput.parse_obj(obj)

        _obj = ListFiltersPaginationOutput.parse_obj({
            "current": obj.get("current"),
            "next": obj.get("next"),
            "total_entries": obj.get("totalEntries")
        })
        return _obj


