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


from typing import List
from pydantic import BaseModel, Field, conlist
from segment_public_api.models.rule_input_v1 import RuleInputV1

class ReplaceRulesInTrackingPlanV1Input(BaseModel):
    """
    Replaces Tracking Plan rules.  # noqa: E501
    """
    rules: conlist(RuleInputV1) = Field(..., description="Rules to replace.")
    __properties = ["rules"]

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
    def from_json(cls, json_str: str) -> ReplaceRulesInTrackingPlanV1Input:
        """Create an instance of ReplaceRulesInTrackingPlanV1Input from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReplaceRulesInTrackingPlanV1Input:
        """Create an instance of ReplaceRulesInTrackingPlanV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReplaceRulesInTrackingPlanV1Input.parse_obj(obj)

        _obj = ReplaceRulesInTrackingPlanV1Input.parse_obj({
            "rules": [RuleInputV1.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj


