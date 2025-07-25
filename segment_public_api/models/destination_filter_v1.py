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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from segment_public_api.models.destination_filter_action_v1 import DestinationFilterActionV1

class DestinationFilterV1(BaseModel):
    """
    Represents a Destination filter.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The unique id of this filter.")
    source_id: StrictStr = Field(..., alias="sourceId", description="The id of the Source associated with this filter.")
    destination_id: StrictStr = Field(..., alias="destinationId", description="The id of the Destination associated with this filter.")
    var_if: StrictStr = Field(..., alias="if", description="A condition that defines whether to apply this filter to a payload.")
    actions: conlist(DestinationFilterActionV1) = Field(..., description="A list of actions this filter performs.")
    title: StrictStr = Field(..., description="A title for this filter.")
    description: Optional[StrictStr] = Field(None, description="A description for this filter.")
    enabled: StrictBool = Field(..., description="When set to true, this filter is active.")
    created_at: StrictStr = Field(..., alias="createdAt", description="The timestamp of this filter's creation.")
    updated_at: StrictStr = Field(..., alias="updatedAt", description="The timestamp of this filter's last change.")
    __properties = ["id", "sourceId", "destinationId", "if", "actions", "title", "description", "enabled", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> DestinationFilterV1:
        """Create an instance of DestinationFilterV1 from a JSON string"""
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
    def from_dict(cls, obj: dict) -> DestinationFilterV1:
        """Create an instance of DestinationFilterV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationFilterV1.parse_obj(obj)

        _obj = DestinationFilterV1.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "destination_id": obj.get("destinationId"),
            "var_if": obj.get("if"),
            "actions": [DestinationFilterActionV1.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "enabled": obj.get("enabled"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


