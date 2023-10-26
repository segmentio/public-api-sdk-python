# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 36.3.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictBool, StrictStr

class ReverseEtlModel(BaseModel):
    """
    Defines a Reverse ETL Model.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of the Model.")
    source_id: StrictStr = Field(..., alias="sourceId", description="The id for the attached Source.")
    name: StrictStr = Field(..., description="A short, human-readable description of the Model.")
    description: StrictStr = Field(..., description="A longer, more descriptive explanation of the Model.")
    enabled: StrictBool = Field(..., description="Indicates whether the Model should have syncs enabled. When disabled, no syncs will be triggered, regardless of the enabled status of the attached destinations/subscriptions.")
    schedule_strategy: StrictStr = Field(..., alias="scheduleStrategy", description="Determines the strategy used for triggering syncs, which will be used in conjunction with scheduleConfig.  Possible values: \"manual\", \"periodic\", \"specific_days\".")
    schedule_config: Dict[str, Any] = Field(..., alias="scheduleConfig", description="Defines a configuration object used for scheduling, which can vary depending on the configured strategy, but must always be an object with at least 1 level of keys.")
    query: StrictStr = Field(..., description="The SQL query that will be executed to extract data from the connected Source.")
    query_identifier_column: StrictStr = Field(..., alias="queryIdentifierColumn", description="Indicates the column named in `query` that should be used to uniquely identify the extracted records.")
    __properties = ["id", "sourceId", "name", "description", "enabled", "scheduleStrategy", "scheduleConfig", "query", "queryIdentifierColumn"]

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
    def from_json(cls, json_str: str) -> ReverseEtlModel:
        """Create an instance of ReverseEtlModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReverseEtlModel:
        """Create an instance of ReverseEtlModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReverseEtlModel.parse_obj(obj)

        _obj = ReverseEtlModel.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "enabled": obj.get("enabled"),
            "schedule_strategy": obj.get("scheduleStrategy"),
            "schedule_config": obj.get("scheduleConfig"),
            "query": obj.get("query"),
            "query_identifier_column": obj.get("queryIdentifierColumn")
        })
        return _obj


