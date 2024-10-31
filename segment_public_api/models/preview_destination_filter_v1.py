# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 55.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from segment_public_api.models.destination_filter_action_v1 import DestinationFilterActionV1

class PreviewDestinationFilterV1(BaseModel):
    """
    A simplified Destination filter that includes the if and actions for a DestinationFilterV1.  # noqa: E501
    """
    var_if: StrictStr = Field(..., alias="if", description="A FQL statement which determines if the provided filter's actions will apply to the provided JSON payload. The literal string \"all\" will result in this filter to all events. For guidance on using FQL, see the Segment documentation site.")
    actions: conlist(DestinationFilterActionV1) = Field(..., description="The filtering action to take on events that match the \"if\" statement. Action types must be one of: \"drop\", \"allow_properties\", \"drop_properties\" or \"sample\".")
    __properties = ["if", "actions"]

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
    def from_json(cls, json_str: str) -> PreviewDestinationFilterV1:
        """Create an instance of PreviewDestinationFilterV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreviewDestinationFilterV1:
        """Create an instance of PreviewDestinationFilterV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreviewDestinationFilterV1.parse_obj(obj)

        _obj = PreviewDestinationFilterV1.parse_obj({
            "var_if": obj.get("if"),
            "actions": [DestinationFilterActionV1.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None
        })
        return _obj


