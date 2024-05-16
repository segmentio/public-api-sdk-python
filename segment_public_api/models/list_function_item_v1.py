# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.1.0
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

class ListFunctionItemV1(BaseModel):
    """
    Represents a Function in a list.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="An identifier for this Function.")
    resource_type: Optional[StrictStr] = Field(None, alias="resourceType", description="The Function type.  Config API note: equal to `type`.")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt", description="The time this Function was created.")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="The id of the user who created this Function.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="A display name for this Function.")
    description: Optional[StrictStr] = Field(None, description="A description for this Function.")
    logo_url: Optional[StrictStr] = Field(None, alias="logoUrl", description="The URL of the logo for this Function.")
    catalog_id: Optional[StrictStr] = Field(None, alias="catalogId", description="The catalog id of this Function.")
    __properties = ["id", "resourceType", "createdAt", "createdBy", "displayName", "description", "logoUrl", "catalogId"]

    @validator('resource_type')
    def resource_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DESTINATION', 'INSERT_DESTINATION', 'SOURCE'):
            raise ValueError("must be one of enum values ('DESTINATION', 'INSERT_DESTINATION', 'SOURCE')")
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
    def from_json(cls, json_str: str) -> ListFunctionItemV1:
        """Create an instance of ListFunctionItemV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListFunctionItemV1:
        """Create an instance of ListFunctionItemV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListFunctionItemV1.parse_obj(obj)

        _obj = ListFunctionItemV1.parse_obj({
            "id": obj.get("id"),
            "resource_type": obj.get("resourceType"),
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "logo_url": obj.get("logoUrl"),
            "catalog_id": obj.get("catalogId")
        })
        return _obj


