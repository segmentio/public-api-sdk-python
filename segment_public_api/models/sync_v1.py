# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.0.0
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
from segment_public_api.models.sync_notice_v1 import SyncNoticeV1

class SyncV1(BaseModel):
    """
    Represents a sync between a Source and Warehouse.  A sync occurs when data from a Source is loaded into a Warehouse.  # noqa: E501
    """
    source_id: StrictStr = Field(..., alias="sourceId", description="The id of the Source loaded in the sync.")
    start: StrictStr = Field(..., description="The start time of the sync.")
    end: Optional[StrictStr] = Field(..., description="The time the sync completed. Returns null if unfinished.")
    status: StrictStr = Field(..., description="The status of the sync.")
    duration: Union[StrictFloat, StrictInt] = Field(..., description="The duration of the sync in seconds. Returns the partial duration if the sync has not finished yet.")
    human_duration: StrictStr = Field(..., alias="humanDuration", description="The human-readable counterpart of `duration`.")
    count: Union[StrictFloat, StrictInt] = Field(..., description="The number of rows synced into the Warehouse.")
    notices: conlist(SyncNoticeV1) = Field(..., description="Notices that contain the events that occurred during the sync.")
    __properties = ["sourceId", "start", "end", "status", "duration", "humanDuration", "count", "notices"]

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
    def from_json(cls, json_str: str) -> SyncV1:
        """Create an instance of SyncV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item in self.notices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notices'] = _items
        # set to None if end (nullable) is None
        # and __fields_set__ contains the field
        if self.end is None and "end" in self.__fields_set__:
            _dict['end'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SyncV1:
        """Create an instance of SyncV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SyncV1.parse_obj(obj)

        _obj = SyncV1.parse_obj({
            "source_id": obj.get("sourceId"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "status": obj.get("status"),
            "duration": obj.get("duration"),
            "human_duration": obj.get("humanDuration"),
            "count": obj.get("count"),
            "notices": [SyncNoticeV1.from_dict(_item) for _item in obj.get("notices")] if obj.get("notices") is not None else None
        })
        return _obj


