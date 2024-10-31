# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 55.2.0
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

class IdentifySourceSettingsV1(BaseModel):
    """
    IdentifySourceSettingsV1
    """
    allow_unplanned_traits: Optional[StrictBool] = Field(None, alias="allowUnplannedTraits", description="Enable to allow unplanned identify traits.  Config API note: equal to `allowUnplannedIdentifyTraits`.")
    allow_traits_on_violations: Optional[StrictBool] = Field(None, alias="allowTraitsOnViolations", description="Enable to allow identify traits on violations.  Config API note: equal to `allowIdentifyTraitsOnViolations`.")
    common_event_on_violations: Optional[StrictStr] = Field(None, alias="commonEventOnViolations", description="The common identify event on violations.  Config API note: equal to `commonIdentifyEventOnViolations`.")
    __properties = ["allowUnplannedTraits", "allowTraitsOnViolations", "commonEventOnViolations"]

    @validator('common_event_on_violations')
    def common_event_on_violations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ALLOW', 'BLOCK', 'OMIT_TRAITS'):
            raise ValueError("must be one of enum values ('ALLOW', 'BLOCK', 'OMIT_TRAITS')")
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
    def from_json(cls, json_str: str) -> IdentifySourceSettingsV1:
        """Create an instance of IdentifySourceSettingsV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentifySourceSettingsV1:
        """Create an instance of IdentifySourceSettingsV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentifySourceSettingsV1.parse_obj(obj)

        _obj = IdentifySourceSettingsV1.parse_obj({
            "allow_unplanned_traits": obj.get("allowUnplannedTraits"),
            "allow_traits_on_violations": obj.get("allowTraitsOnViolations"),
            "common_event_on_violations": obj.get("commonEventOnViolations")
        })
        return _obj


