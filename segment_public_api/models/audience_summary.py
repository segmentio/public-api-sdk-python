# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from segment_public_api.models.definition1 import Definition1

class AudienceSummary(BaseModel):
    """
    Defines an Audience.  # noqa: E501
    """
    id: StrictStr = Field(..., description="Audience id.")
    space_id: StrictStr = Field(..., alias="spaceId", description="Space id for the audience.")
    name: StrictStr = Field(..., description="Name of the audience.")
    description: StrictStr = Field(..., description="Description of the audience.")
    key: StrictStr = Field(..., description="Key for the audience.")
    enabled: StrictBool = Field(..., description="Enabled/disabled status for the audience.")
    definition: Optional[Definition1] = Field(...)
    status: Optional[StrictStr] = Field(None, description="Status for the audience.  Possible values: Backfilling, Computing, Failed, Live, Awaiting Destinations, Disabled.")
    created_by: StrictStr = Field(..., alias="createdBy", description="User id who created the audience.")
    updated_by: StrictStr = Field(..., alias="updatedBy", description="User id who last updated the audience.")
    created_at: StrictStr = Field(..., alias="createdAt", description="Date the audience was created.")
    updated_at: StrictStr = Field(..., alias="updatedAt", description="Date the audience was last updated.")
    __properties = ["id", "spaceId", "name", "description", "key", "enabled", "definition", "status", "createdBy", "updatedBy", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> AudienceSummary:
        """Create an instance of AudienceSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # set to None if definition (nullable) is None
        # and __fields_set__ contains the field
        if self.definition is None and "definition" in self.__fields_set__:
            _dict['definition'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AudienceSummary:
        """Create an instance of AudienceSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AudienceSummary.parse_obj(obj)

        _obj = AudienceSummary.parse_obj({
            "id": obj.get("id"),
            "space_id": obj.get("spaceId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "key": obj.get("key"),
            "enabled": obj.get("enabled"),
            "definition": Definition1.from_dict(obj.get("definition")) if obj.get("definition") is not None else None,
            "status": obj.get("status"),
            "created_by": obj.get("createdBy"),
            "updated_by": obj.get("updatedBy"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


