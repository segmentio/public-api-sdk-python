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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class TrackingPlanV1(BaseModel):
    """
    Represents a Tracking Plan.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The Tracking Plan's identifier.  Config API note: analogous to `name`.")
    name: Optional[StrictStr] = Field(None, description="The Tracking Plan's name.  Config API note: equal to `displayName`.")
    slug: Optional[StrictStr] = Field(None, description="URL-friendly slug of this Tracking Plan.  Config API note: equal to `name`.")
    description: Optional[StrictStr] = Field(None, description="The Tracking Plan's description.")
    type: StrictStr = Field(..., description="The Tracking Plan's type.")
    updated_at: Optional[StrictStr] = Field(None, alias="updatedAt", description="The timestamp of the last change to the Tracking Plan.  Config API note: equal to `updateTime`.")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt", description="The timestamp of this Tracking Plan's creation.  Config API note: equal to `createTime`.")
    __properties = ["id", "name", "slug", "description", "type", "updatedAt", "createdAt"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ENGAGE', 'LIVE', 'PROPERTY_LIBRARY', 'RULE_LIBRARY', 'TEMPLATE'):
            raise ValueError("must be one of enum values ('ENGAGE', 'LIVE', 'PROPERTY_LIBRARY', 'RULE_LIBRARY', 'TEMPLATE')")
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
    def from_json(cls, json_str: str) -> TrackingPlanV1:
        """Create an instance of TrackingPlanV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TrackingPlanV1:
        """Create an instance of TrackingPlanV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TrackingPlanV1.parse_obj(obj)

        _obj = TrackingPlanV1.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "updated_at": obj.get("updatedAt"),
            "created_at": obj.get("createdAt")
        })
        return _obj


