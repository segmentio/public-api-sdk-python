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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from segment_public_api.models.breakdown_beta import BreakdownBeta

class MetricBeta(BaseModel):
    """
    The event delivery metric.  # noqa: E501
    """
    metric_name: StrictStr = Field(..., alias="metricName", description="The name of the metric.")
    total: Union[StrictFloat, StrictInt] = Field(..., description="Number of occurrences of the metric.")
    breakdown: Optional[conlist(BreakdownBeta)] = Field(None, description="Breakdown of metrics within a metric.")
    __properties = ["metricName", "total", "breakdown"]

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
    def from_json(cls, json_str: str) -> MetricBeta:
        """Create an instance of MetricBeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in breakdown (list)
        _items = []
        if self.breakdown:
            for _item in self.breakdown:
                if _item:
                    _items.append(_item.to_dict())
            _dict['breakdown'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetricBeta:
        """Create an instance of MetricBeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetricBeta.parse_obj(obj)

        _obj = MetricBeta.parse_obj({
            "metric_name": obj.get("metricName"),
            "total": obj.get("total"),
            "breakdown": [BreakdownBeta.from_dict(_item) for _item in obj.get("breakdown")] if obj.get("breakdown") is not None else None
        })
        return _obj


