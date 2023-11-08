# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class CreateCloudSourceRegulationV1Input(BaseModel):
    """
    The input to create a Cloud Source-scoped regulation.  # noqa: E501
    """
    regulation_type: StrictStr = Field(..., alias="regulationType", description="The regulation type to create.")
    subject_type: StrictStr = Field(..., alias="subjectType", description="The subject type. Must be `objectId` for Cloud Sources.")
    subject_ids: conlist(StrictStr) = Field(..., alias="subjectIds", description="The list of `userId` or `objectId` values of the subjects to regulate.  Config API note: equal to `parent` but allows an array.")
    collection: StrictStr = Field(..., description="The Cloud Source collection to regulate.")
    __properties = ["regulationType", "subjectType", "subjectIds", "collection"]

    @validator('regulation_type')
    def regulation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DELETE_INTERNAL', 'DELETE_ONLY', 'SUPPRESS_ONLY', 'SUPPRESS_WITH_DELETE', 'UNSUPPRESS'):
            raise ValueError("must be one of enum values ('DELETE_INTERNAL', 'DELETE_ONLY', 'SUPPRESS_ONLY', 'SUPPRESS_WITH_DELETE', 'UNSUPPRESS')")
        return value

    @validator('subject_type')
    def subject_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('OBJECT_ID'):
            raise ValueError("must be one of enum values ('OBJECT_ID')")
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
    def from_json(cls, json_str: str) -> CreateCloudSourceRegulationV1Input:
        """Create an instance of CreateCloudSourceRegulationV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateCloudSourceRegulationV1Input:
        """Create an instance of CreateCloudSourceRegulationV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateCloudSourceRegulationV1Input.parse_obj(obj)

        _obj = CreateCloudSourceRegulationV1Input.parse_obj({
            "regulation_type": obj.get("regulationType"),
            "subject_type": obj.get("subjectType"),
            "subject_ids": obj.get("subjectIds"),
            "collection": obj.get("collection")
        })
        return _obj


