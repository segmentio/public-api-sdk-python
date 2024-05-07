# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from segment_public_api.models.destination_filter_action_v1 import DestinationFilterActionV1

class CreateFilterForDestinationV1Input(BaseModel):
    """
    Input for CreateDestinationFilterV1.  # noqa: E501
    """
    source_id: StrictStr = Field(..., alias="sourceId", description="The id of the Source associated with this filter.")
    var_if: StrictStr = Field(..., alias="if", description="The filter's condition.")
    actions: conlist(DestinationFilterActionV1) = Field(..., description="Actions for the Destination filter.")
    title: StrictStr = Field(..., description="The title of the filter.")
    description: Optional[StrictStr] = Field(None, description="The description of the filter.")
    enabled: StrictBool = Field(..., description="When set to true, the Destination filter is active.")
    __properties = ["sourceId", "if", "actions", "title", "description", "enabled"]

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
    def from_json(cls, json_str: str) -> CreateFilterForDestinationV1Input:
        """Create an instance of CreateFilterForDestinationV1Input from a JSON string"""
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
    def from_dict(cls, obj: dict) -> CreateFilterForDestinationV1Input:
        """Create an instance of CreateFilterForDestinationV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateFilterForDestinationV1Input.parse_obj(obj)

        _obj = CreateFilterForDestinationV1Input.parse_obj({
            "source_id": obj.get("sourceId"),
            "var_if": obj.get("if"),
            "actions": [DestinationFilterActionV1.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "enabled": obj.get("enabled")
        })
        return _obj


