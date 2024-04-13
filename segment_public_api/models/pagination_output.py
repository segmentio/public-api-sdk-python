# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 48.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class PaginationOutput(BaseModel):
    """
    Pagination metadata for a list response.  Responses return this object alongside a list of resources, which provides the necessary metadata for manipulating a paginated collection. In operations that return lists, it's always present, though some of its fields might not be.  # noqa: E501
    """
    current: StrictStr = Field(..., description="The current cursor within a collection.  Consumers of the API must treat this value as opaque.")
    next: Optional[StrictStr] = Field(None, description="A pointer to the next page.  This does not return when you retrieve the last page.  Consumers of the API must treat this value as opaque.")
    previous: Optional[StrictStr] = Field(None, description="A pointer to the previous page.  This does not return when you retrieve the first page.  Consumers of the API must treat this value as opaque.")
    total_entries: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalEntries", description="The total number of entries available in the collection.  If calculating it impacts performance, the response may omit this field.")
    __properties = ["current", "next", "previous", "totalEntries"]

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
    def from_json(cls, json_str: str) -> PaginationOutput:
        """Create an instance of PaginationOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if next (nullable) is None
        # and __fields_set__ contains the field
        if self.next is None and "next" in self.__fields_set__:
            _dict['next'] = None

        # set to None if previous (nullable) is None
        # and __fields_set__ contains the field
        if self.previous is None and "previous" in self.__fields_set__:
            _dict['previous'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaginationOutput:
        """Create an instance of PaginationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaginationOutput.parse_obj(obj)

        _obj = PaginationOutput.parse_obj({
            "current": obj.get("current"),
            "next": obj.get("next"),
            "previous": obj.get("previous"),
            "total_entries": obj.get("totalEntries")
        })
        return _obj


