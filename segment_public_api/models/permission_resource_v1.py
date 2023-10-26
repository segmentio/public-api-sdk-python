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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from segment_public_api.models.allowed_label_beta import AllowedLabelBeta

class PermissionResourceV1(BaseModel):
    """
    The most basic representation of a resource belonging to a set of permissions.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of this resource.")
    type: StrictStr = Field(..., description="The type for this resource.")
    labels: Optional[conlist(AllowedLabelBeta)] = Field(None, description="The labels that further refine access to this resource. Labels are exclusive to Workspace-level permissions.")
    __properties = ["id", "type", "labels"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FUNCTION', 'SOURCE', 'SPACE', 'WAREHOUSE', 'WORKSPACE'):
            raise ValueError("must be one of enum values ('FUNCTION', 'SOURCE', 'SPACE', 'WAREHOUSE', 'WORKSPACE')")
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
    def from_json(cls, json_str: str) -> PermissionResourceV1:
        """Create an instance of PermissionResourceV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermissionResourceV1:
        """Create an instance of PermissionResourceV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PermissionResourceV1.parse_obj(obj)

        _obj = PermissionResourceV1.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "labels": [AllowedLabelBeta.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None
        })
        return _obj


