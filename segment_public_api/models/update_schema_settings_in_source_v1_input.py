# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from segment_public_api.models.group_source_settings_v1 import GroupSourceSettingsV1
from segment_public_api.models.identify_source_settings_v1 import IdentifySourceSettingsV1
from segment_public_api.models.track_source_settings_v1 import TrackSourceSettingsV1

class UpdateSchemaSettingsInSourceV1Input(BaseModel):
    """
    Input to update a Source's settings.  # noqa: E501
    """
    track: Optional[TrackSourceSettingsV1] = None
    identify: Optional[IdentifySourceSettingsV1] = None
    group: Optional[GroupSourceSettingsV1] = None
    forwarding_violations_to: Optional[StrictStr] = Field(None, alias="forwardingViolationsTo", description="Source id to forward violations to.")
    forwarding_blocked_events_to: Optional[StrictStr] = Field(None, alias="forwardingBlockedEventsTo", description="Source id to forward blocked events to.")
    __properties = ["track", "identify", "group", "forwardingViolationsTo", "forwardingBlockedEventsTo"]

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
    def from_json(cls, json_str: str) -> UpdateSchemaSettingsInSourceV1Input:
        """Create an instance of UpdateSchemaSettingsInSourceV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of track
        if self.track:
            _dict['track'] = self.track.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identify
        if self.identify:
            _dict['identify'] = self.identify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateSchemaSettingsInSourceV1Input:
        """Create an instance of UpdateSchemaSettingsInSourceV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateSchemaSettingsInSourceV1Input.parse_obj(obj)

        _obj = UpdateSchemaSettingsInSourceV1Input.parse_obj({
            "track": TrackSourceSettingsV1.from_dict(obj.get("track")) if obj.get("track") is not None else None,
            "identify": IdentifySourceSettingsV1.from_dict(obj.get("identify")) if obj.get("identify") is not None else None,
            "group": GroupSourceSettingsV1.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "forwarding_violations_to": obj.get("forwardingViolationsTo"),
            "forwarding_blocked_events_to": obj.get("forwardingBlockedEventsTo")
        })
        return _obj


