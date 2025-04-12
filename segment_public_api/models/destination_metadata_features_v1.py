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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class DestinationMetadataFeaturesV1(BaseModel):
    """
    Represents features that a given Destination supports.  # noqa: E501
    """
    cloud_mode_instances: Optional[StrictStr] = Field(None, alias="cloudModeInstances", description="This Destination's support level for cloud mode instances. The values '0' and 'NONE', and '1' and 'SINGLE' are equivalent.")
    device_mode_instances: Optional[StrictStr] = Field(None, alias="deviceModeInstances", description="This Destination's support level for device mode instances. Support for multiple device mode instances is currently not planned. The values '0' and 'NONE', and '1' and 'SINGLE' are equivalent.")
    replay: Optional[StrictBool] = Field(None, description="Whether this Destination supports replays.")
    browser_unbundling: Optional[StrictBool] = Field(None, alias="browserUnbundling", description="Whether this Destination supports browser unbundling.")
    browser_unbundling_public: Optional[StrictBool] = Field(None, alias="browserUnbundlingPublic", description="Whether this Destination supports public browser unbundling.")
    __properties = ["cloudModeInstances", "deviceModeInstances", "replay", "browserUnbundling", "browserUnbundlingPublic"]

    @validator('cloud_mode_instances')
    def cloud_mode_instances_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('0', '1', 'MULTIPLE', 'NONE', 'SINGLE'):
            raise ValueError("must be one of enum values ('0', '1', 'MULTIPLE', 'NONE', 'SINGLE')")
        return value

    @validator('device_mode_instances')
    def device_mode_instances_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('0', '1', 'NONE', 'SINGLE'):
            raise ValueError("must be one of enum values ('0', '1', 'NONE', 'SINGLE')")
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
    def from_json(cls, json_str: str) -> DestinationMetadataFeaturesV1:
        """Create an instance of DestinationMetadataFeaturesV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationMetadataFeaturesV1:
        """Create an instance of DestinationMetadataFeaturesV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationMetadataFeaturesV1.parse_obj(obj)

        _obj = DestinationMetadataFeaturesV1.parse_obj({
            "cloud_mode_instances": obj.get("cloudModeInstances"),
            "device_mode_instances": obj.get("deviceModeInstances"),
            "replay": obj.get("replay"),
            "browser_unbundling": obj.get("browserUnbundling"),
            "browser_unbundling_public": obj.get("browserUnbundlingPublic")
        })
        return _obj


