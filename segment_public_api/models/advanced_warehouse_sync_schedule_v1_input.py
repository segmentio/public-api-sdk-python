# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 36.3.1
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
from segment_public_api.models.warehouse_advanced_sync_v1 import WarehouseAdvancedSyncV1

class AdvancedWarehouseSyncScheduleV1Input(BaseModel):
    """
    Defines the advanced sync schedule for a Warehouse.  # noqa: E501
    """
    times: conlist(WarehouseAdvancedSyncV1) = Field(..., description="A list that contains the times when syncs should occur.")
    timezone: StrictStr = Field(..., description="A TZ-database timezone for this sync schedule.")
    __properties = ["times", "timezone"]

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
    def from_json(cls, json_str: str) -> AdvancedWarehouseSyncScheduleV1Input:
        """Create an instance of AdvancedWarehouseSyncScheduleV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in times (list)
        _items = []
        if self.times:
            for _item in self.times:
                if _item:
                    _items.append(_item.to_dict())
            _dict['times'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedWarehouseSyncScheduleV1Input:
        """Create an instance of AdvancedWarehouseSyncScheduleV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedWarehouseSyncScheduleV1Input.parse_obj(obj)

        _obj = AdvancedWarehouseSyncScheduleV1Input.parse_obj({
            "times": [WarehouseAdvancedSyncV1.from_dict(_item) for _item in obj.get("times")] if obj.get("times") is not None else None,
            "timezone": obj.get("timezone")
        })
        return _obj


