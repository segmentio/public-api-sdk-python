# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 46.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class MtuSnapshotV1(BaseModel):
    """
    A snapshot of MTU metrics within the given usage period.  # noqa: E501
    """
    period_start: Union[StrictFloat, StrictInt] = Field(..., alias="periodStart", description="The start of the usage period, in unix time (seconds since epoch).")
    period_end: Union[StrictFloat, StrictInt] = Field(..., alias="periodEnd", description="The end of the usage period, in unix time (seconds since epoch).")
    anonymous: StrictStr = Field(..., description="A bigint of the number of anonymous users in this snapshot.")
    anonymous_identified: StrictStr = Field(..., alias="anonymousIdentified", description="A bigint of the number of anonymous identified users in this snapshot.")
    identified: StrictStr = Field(..., description="A bigint of the number of identified users in this snapshot.")
    never_identified: StrictStr = Field(..., alias="neverIdentified", description="A bigint of the number of never identified users in this snapshot.")
    timestamp: StrictStr = Field(..., description="The timestamp of this snapshot within the billing cycle, in the ISO-8601 format.")
    __properties = ["periodStart", "periodEnd", "anonymous", "anonymousIdentified", "identified", "neverIdentified", "timestamp"]

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
    def from_json(cls, json_str: str) -> MtuSnapshotV1:
        """Create an instance of MtuSnapshotV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MtuSnapshotV1:
        """Create an instance of MtuSnapshotV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MtuSnapshotV1.parse_obj(obj)

        _obj = MtuSnapshotV1.parse_obj({
            "period_start": obj.get("periodStart"),
            "period_end": obj.get("periodEnd"),
            "anonymous": obj.get("anonymous"),
            "anonymous_identified": obj.get("anonymousIdentified"),
            "identified": obj.get("identified"),
            "never_identified": obj.get("neverIdentified"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


