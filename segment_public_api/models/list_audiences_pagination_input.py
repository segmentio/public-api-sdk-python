# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.13.0
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

class ListAudiencesPaginationInput(BaseModel):
    """
    Fork of Autobahn's PaginationInput. Count is limited to 200 in this fork.  Pagination parameters.  Every resource that returns a list of items in its `Output` object may contain a `PaginationInput` in its `Input` object. Required, though some of its fields are optional.  # noqa: E501
    """
    cursor: Optional[StrictStr] = Field(None, description="The page to request.  Acceptable values to use here are in PaginationOutput objects, in the `current`, `next`, and `previous` keys.  Consumers of the API must treat this value as opaque.")
    count: Union[StrictFloat, StrictInt] = Field(..., description="The number of items to retrieve in a page, between 1 and 200.")
    __properties = ["cursor", "count"]

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
    def from_json(cls, json_str: str) -> ListAudiencesPaginationInput:
        """Create an instance of ListAudiencesPaginationInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListAudiencesPaginationInput:
        """Create an instance of ListAudiencesPaginationInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListAudiencesPaginationInput.parse_obj(obj)

        _obj = ListAudiencesPaginationInput.parse_obj({
            "cursor": obj.get("cursor"),
            "count": obj.get("count")
        })
        return _obj


