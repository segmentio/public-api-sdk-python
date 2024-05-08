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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator

class GetEventsVolumeFromWorkspaceV1Query(BaseModel):
    """
    GetEventVolumeOutputQuery represents the input query sent to output.  # noqa: E501
    """
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="Workspace being requested.")
    granularity: StrictStr = Field(..., description="Granularity corresponds to the requested bucket granularity.")
    start_time: StrictStr = Field(..., alias="startTime", description="StartTime is the ISO8601 formatted timestamp corresponding to the beginning of the requested time frame, inclusive.")
    end_time: StrictStr = Field(..., alias="endTime", description="EndTime is the ISO8601 formatted timestamp corresponding to the end of the requested time frame, noninclusive.")
    group_by: Optional[conlist(StrictStr)] = Field(None, alias="groupBy", description="GroupBy is a comma-delimited list of strings representing the dimensions to group the result by. The current options are: `eventName` or `eventType`.")
    source_id: Optional[conlist(StrictStr)] = Field(None, alias="sourceId", description="List of strings which allow you to restrict the result to just the given Sources.")
    event_name: Optional[conlist(StrictStr)] = Field(None, alias="eventName", description="EventName is a list of strings which allow you to restrict the result to just the given event names.")
    event_type: Optional[conlist(StrictStr)] = Field(None, alias="eventType", description="EventType is a list of strings which allow you to restrict the result to just the given event types.")
    app_version: Optional[conlist(StrictStr)] = Field(None, alias="appVersion", description="AppVersion is a list of strings which allow you to restrict the result to just the given application versions.")
    limit: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Limit is the total number of items in the result.")
    __properties = ["workspaceId", "granularity", "startTime", "endTime", "groupBy", "sourceId", "eventName", "eventType", "appVersion", "limit"]

    @validator('granularity')
    def granularity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DAY', 'HOUR', 'MINUTE'):
            raise ValueError("must be one of enum values ('DAY', 'HOUR', 'MINUTE')")
        return value

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
    def from_json(cls, json_str: str) -> GetEventsVolumeFromWorkspaceV1Query:
        """Create an instance of GetEventsVolumeFromWorkspaceV1Query from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetEventsVolumeFromWorkspaceV1Query:
        """Create an instance of GetEventsVolumeFromWorkspaceV1Query from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetEventsVolumeFromWorkspaceV1Query.parse_obj(obj)

        _obj = GetEventsVolumeFromWorkspaceV1Query.parse_obj({
            "workspace_id": obj.get("workspaceId"),
            "granularity": obj.get("granularity"),
            "start_time": obj.get("startTime"),
            "end_time": obj.get("endTime"),
            "group_by": obj.get("groupBy"),
            "source_id": obj.get("sourceId"),
            "event_name": obj.get("eventName"),
            "event_type": obj.get("eventType"),
            "app_version": obj.get("appVersion"),
            "limit": obj.get("limit")
        })
        return _obj


