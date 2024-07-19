# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.4.0
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
from segment_public_api.models.event_source_v1 import EventSourceV1
from segment_public_api.models.source_event_volume_datapoint_v1 import SourceEventVolumeDatapointV1

class SourceEventVolumeV1(BaseModel):
    """
    SourceEventVolume represents a time series of event volume for a Workspace broken down by the dimensions which the customer specifies (optional parameters).  # noqa: E501
    """
    source: Optional[EventSourceV1] = None
    event_name: Optional[StrictStr] = Field(None, alias="eventName", description="The name of the event, if applicable.")
    event_type: Optional[StrictStr] = Field(None, alias="eventType", description="The event type, if applicable.")
    total: Union[StrictFloat, StrictInt] = Field(..., description="The total count for all events in the requested time frame.")
    series: conlist(SourceEventVolumeDatapointV1) = Field(..., description="A list of the event counts broken down by the requested granularity.")
    __properties = ["source", "eventName", "eventType", "total", "series"]

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
    def from_json(cls, json_str: str) -> SourceEventVolumeV1:
        """Create an instance of SourceEventVolumeV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in series (list)
        _items = []
        if self.series:
            for _item in self.series:
                if _item:
                    _items.append(_item.to_dict())
            _dict['series'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SourceEventVolumeV1:
        """Create an instance of SourceEventVolumeV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SourceEventVolumeV1.parse_obj(obj)

        _obj = SourceEventVolumeV1.parse_obj({
            "source": EventSourceV1.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "event_name": obj.get("eventName"),
            "event_type": obj.get("eventType"),
            "total": obj.get("total"),
            "series": [SourceEventVolumeDatapointV1.from_dict(_item) for _item in obj.get("series")] if obj.get("series") is not None else None
        })
        return _obj


