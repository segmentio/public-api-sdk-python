# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 47.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from segment_public_api.models.allowed_label_beta import AllowedLabelBeta
from segment_public_api.models.resource_v1 import ResourceV1

class InvitePermissionV1(BaseModel):
    """
    Defines a permission to apply to the user in an invite.  # noqa: E501
    """
    role_id: StrictStr = Field(..., alias="roleId", description="The id of the role.")
    resources: Optional[conlist(ResourceV1)] = Field(None, description="The resources to grant the invited users access to.")
    labels: Optional[conlist(AllowedLabelBeta)] = Field(None, description="The labels that determine which resources to grant users access to.")
    __properties = ["roleId", "resources", "labels"]

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
    def from_json(cls, json_str: str) -> InvitePermissionV1:
        """Create an instance of InvitePermissionV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvitePermissionV1:
        """Create an instance of InvitePermissionV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InvitePermissionV1.parse_obj(obj)

        _obj = InvitePermissionV1.parse_obj({
            "role_id": obj.get("roleId"),
            "resources": [ResourceV1.from_dict(_item) for _item in obj.get("resources")] if obj.get("resources") is not None else None,
            "labels": [AllowedLabelBeta.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None
        })
        return _obj


