# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.1.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from segment_public_api.models.insert_function_instance_alpha import InsertFunctionInstanceAlpha
from segment_public_api.models.pagination_output import PaginationOutput

class ListInsertFunctionInstancesAlphaOutput(BaseModel):
    """
    Returns a list of insert Function instances connected to the insert Function.  # noqa: E501
    """
    instances: conlist(InsertFunctionInstanceAlpha) = Field(..., description="All insert Function instances found.")
    pagination: PaginationOutput = Field(...)
    __properties = ["instances", "pagination"]

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
    def from_json(cls, json_str: str) -> ListInsertFunctionInstancesAlphaOutput:
        """Create an instance of ListInsertFunctionInstancesAlphaOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in instances (list)
        _items = []
        if self.instances:
            for _item in self.instances:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instances'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListInsertFunctionInstancesAlphaOutput:
        """Create an instance of ListInsertFunctionInstancesAlphaOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListInsertFunctionInstancesAlphaOutput.parse_obj(obj)

        _obj = ListInsertFunctionInstancesAlphaOutput.parse_obj({
            "instances": [InsertFunctionInstanceAlpha.from_dict(_item) for _item in obj.get("instances")] if obj.get("instances") is not None else None,
            "pagination": PaginationOutput.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None
        })
        return _obj


