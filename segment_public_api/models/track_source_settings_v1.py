# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.3.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class TrackSourceSettingsV1(BaseModel):
    """
    TrackSourceSettingsV1
    """
    allow_unplanned_events: Optional[StrictBool] = Field(None, alias="allowUnplannedEvents", description="Enable to allow unplanned track events.  Config API note: equal to `allowUnplannedTrackEvents`.")
    allow_unplanned_event_properties: Optional[StrictBool] = Field(None, alias="allowUnplannedEventProperties", description="Enable to allow unplanned track event properties.  Config API note: equal to `allowUnplannedTrackEventProperties`.")
    allow_event_on_violations: Optional[StrictBool] = Field(None, alias="allowEventOnViolations", description="Allow track event on violations.  Config API note: equal to `allowTrackEventOnViolations`.")
    allow_properties_on_violations: Optional[StrictBool] = Field(None, alias="allowPropertiesOnViolations", description="Enable to allow track properties on violations.  Config API note: equal to `allowTrackEventPropertiesOnViolations`.")
    common_event_on_violations: Optional[StrictStr] = Field(None, alias="commonEventOnViolations", description="The common track event on violations.  Config API note: equal to `commonTrackEventOnViolations`.")
    __properties = ["allowUnplannedEvents", "allowUnplannedEventProperties", "allowEventOnViolations", "allowPropertiesOnViolations", "commonEventOnViolations"]

    @validator('common_event_on_violations')
    def common_event_on_violations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ALLOW', 'BLOCK', 'OMIT_PROPERTIES'):
            raise ValueError("must be one of enum values ('ALLOW', 'BLOCK', 'OMIT_PROPERTIES')")
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
    def from_json(cls, json_str: str) -> TrackSourceSettingsV1:
        """Create an instance of TrackSourceSettingsV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackSourceSettingsV1:
        """Create an instance of TrackSourceSettingsV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackSourceSettingsV1.parse_obj(obj)

        _obj = TrackSourceSettingsV1.parse_obj({
            "allow_unplanned_events": obj.get("allowUnplannedEvents"),
            "allow_unplanned_event_properties": obj.get("allowUnplannedEventProperties"),
            "allow_event_on_violations": obj.get("allowEventOnViolations"),
            "allow_properties_on_violations": obj.get("allowPropertiesOnViolations"),
            "common_event_on_violations": obj.get("commonEventOnViolations")
        })
        return _obj


