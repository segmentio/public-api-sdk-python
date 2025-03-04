# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.4.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from segment_public_api.models.exit_destination_state import ExitDestinationState
from segment_public_api.models.rules_inner import RulesInner

class ExitRulesConfig(BaseModel):
    """
    The exit rules configuration.  # noqa: E501
    """
    enabled: StrictBool = Field(...)
    rules: conlist(RulesInner) = Field(...)
    related_destinations: Optional[conlist(ExitDestinationState)] = Field(None, alias="relatedDestinations")
    __properties = ["enabled", "rules", "relatedDestinations"]

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
    def from_json(cls, json_str: str) -> ExitRulesConfig:
        """Create an instance of ExitRulesConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_destinations (list)
        _items = []
        if self.related_destinations:
            for _item in self.related_destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedDestinations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExitRulesConfig:
        """Create an instance of ExitRulesConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExitRulesConfig.parse_obj(obj)

        _obj = ExitRulesConfig.parse_obj({
            "enabled": obj.get("enabled"),
            "rules": [RulesInner.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None,
            "related_destinations": [ExitDestinationState.from_dict(_item) for _item in obj.get("relatedDestinations")] if obj.get("relatedDestinations") is not None else None
        })
        return _obj


