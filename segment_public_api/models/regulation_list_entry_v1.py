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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class RegulationListEntryV1(BaseModel):
    """
    RegulationListEntryV1
    """
    id: StrictStr = Field(..., description="The id of the regulate request.")
    subject_type: StrictStr = Field(..., alias="subjectType", description="The subject type.")
    subjects: conlist(StrictStr) = Field(..., description="The list of `userId` or `objectId` values of the subjects to regulate.")
    status: StrictStr = Field(..., description="The current status of the regulate request.")
    created_at: StrictStr = Field(..., alias="createdAt", description="The timestamp of the creation of the request.")
    regulation_type: StrictStr = Field(..., alias="regulationType", description="The regulation type.")
    finished_at: Optional[StrictStr] = Field(None, alias="finishedAt", description="The timestamp of when the request finished.")
    __properties = ["id", "subjectType", "subjects", "status", "createdAt", "regulationType", "finishedAt"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FAILED', 'FINISHED', 'INITIALIZED', 'INVALID', 'NOT_SUPPORTED', 'PARTIAL_SUCCESS', 'RUNNING'):
            raise ValueError("must be one of enum values ('FAILED', 'FINISHED', 'INITIALIZED', 'INVALID', 'NOT_SUPPORTED', 'PARTIAL_SUCCESS', 'RUNNING')")
        return value

    @validator('regulation_type')
    def regulation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DELETE_INTERNAL', 'DELETE_ONLY', 'SUPPRESS_ONLY', 'SUPPRESS_WITH_DELETE', 'SUPPRESS_WITH_DELETE_INTERNAL', 'UNSUPPRESS'):
            raise ValueError("must be one of enum values ('DELETE_INTERNAL', 'DELETE_ONLY', 'SUPPRESS_ONLY', 'SUPPRESS_WITH_DELETE', 'SUPPRESS_WITH_DELETE_INTERNAL', 'UNSUPPRESS')")
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
    def from_json(cls, json_str: str) -> RegulationListEntryV1:
        """Create an instance of RegulationListEntryV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegulationListEntryV1:
        """Create an instance of RegulationListEntryV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegulationListEntryV1.parse_obj(obj)

        _obj = RegulationListEntryV1.parse_obj({
            "id": obj.get("id"),
            "subject_type": obj.get("subjectType"),
            "subjects": obj.get("subjects"),
            "status": obj.get("status"),
            "created_at": obj.get("createdAt"),
            "regulation_type": obj.get("regulationType"),
            "finished_at": obj.get("finishedAt")
        })
        return _obj


