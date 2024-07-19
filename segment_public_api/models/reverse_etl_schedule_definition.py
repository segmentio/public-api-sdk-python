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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from segment_public_api.models.config import Config

class ReverseEtlScheduleDefinition(BaseModel):
    """
    Defines a configuration object used for scheduling, which can vary depending on the configured strategy.  # noqa: E501
    """
    strategy: StrictStr = Field(..., description="Strategy supports three modes: Periodic, Specific Days, or Manual.")
    config: Optional[Config] = None
    __properties = ["strategy", "config"]

    @validator('strategy')
    def strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MANUAL', 'PERIODIC', 'SPECIFIC_DAYS'):
            raise ValueError("must be one of enum values ('MANUAL', 'PERIODIC', 'SPECIFIC_DAYS')")
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
    def from_json(cls, json_str: str) -> ReverseEtlScheduleDefinition:
        """Create an instance of ReverseEtlScheduleDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # set to None if config (nullable) is None
        # and __fields_set__ contains the field
        if self.config is None and "config" in self.__fields_set__:
            _dict['config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReverseEtlScheduleDefinition:
        """Create an instance of ReverseEtlScheduleDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReverseEtlScheduleDefinition.parse_obj(obj)

        _obj = ReverseEtlScheduleDefinition.parse_obj({
            "strategy": obj.get("strategy"),
            "config": Config.from_dict(obj.get("config")) if obj.get("config") is not None else None
        })
        return _obj


