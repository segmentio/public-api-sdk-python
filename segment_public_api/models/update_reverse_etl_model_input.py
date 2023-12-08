# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.4.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class UpdateReverseEtlModelInput(BaseModel):
    """
    Defines how to update an existing Model.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="A short, human-readable description of the Model.")
    description: Optional[StrictStr] = Field(None, description="A longer, more descriptive explanation of the Model.")
    enabled: Optional[StrictBool] = Field(None, description="Indicates whether the Model should have syncs enabled. When disabled, no syncs will be triggered, regardless of the enabled status of the attached destinations/subscriptions.")
    schedule_strategy: Optional[StrictStr] = Field(None, alias="scheduleStrategy", description="Determines the strategy used for triggering syncs, which will be used in conjunction with scheduleConfig.")
    schedule_config: Optional[Dict[str, Any]] = Field(None, alias="scheduleConfig", description="Defines a configuration object used for scheduling, which can vary depending on the configured strategy, but must always be an object with at least 1 level of keys.")
    query: Optional[StrictStr] = Field(None, description="The SQL query that will be executed to extract data from the connected Source.")
    query_identifier_column: Optional[StrictStr] = Field(None, alias="queryIdentifierColumn", description="Indicates the column named in `query` that should be used to uniquely identify the extracted records.")
    __properties = ["name", "description", "enabled", "scheduleStrategy", "scheduleConfig", "query", "queryIdentifierColumn"]

    @validator('schedule_strategy')
    def schedule_strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> UpdateReverseEtlModelInput:
        """Create an instance of UpdateReverseEtlModelInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateReverseEtlModelInput:
        """Create an instance of UpdateReverseEtlModelInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateReverseEtlModelInput.parse_obj(obj)

        _obj = UpdateReverseEtlModelInput.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "enabled": obj.get("enabled"),
            "schedule_strategy": obj.get("scheduleStrategy"),
            "schedule_config": obj.get("scheduleConfig"),
            "query": obj.get("query"),
            "query_identifier_column": obj.get("queryIdentifierColumn")
        })
        return _obj


