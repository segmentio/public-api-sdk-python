# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool

class AudienceOptions(BaseModel):
    """
    AudienceOptions
    """
    include_historical_data: Optional[StrictBool] = Field(None, alias="includeHistoricalData", description="Determines whether data prior to the audience being created is included when determining audience membership. Note that including historical data may be needed in order to properly handle the definition specified. In these cases, Segment will automatically handle including historical data and the response will return the includeHistoricalData parameter as true.")
    include_anonymous_users: Optional[StrictBool] = Field(None, alias="includeAnonymousUsers", description="Determines whether anonymous users should be included when determining audience membership.")
    __properties = ["includeHistoricalData", "includeAnonymousUsers"]

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
    def from_json(cls, json_str: str) -> AudienceOptions:
        """Create an instance of AudienceOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AudienceOptions:
        """Create an instance of AudienceOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AudienceOptions.parse_obj(obj)

        _obj = AudienceOptions.parse_obj({
            "include_historical_data": obj.get("includeHistoricalData"),
            "include_anonymous_users": obj.get("includeAnonymousUsers")
        })
        return _obj


