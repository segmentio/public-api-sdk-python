# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.13.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class WorkspaceV1(BaseModel):
    """
    An organized group of Sources and Destinations managed by a team.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The unique identifier.")
    slug: StrictStr = Field(..., description="The URL-friendly slug.")
    name: StrictStr = Field(..., description="The human-readable name.")
    __properties = ["id", "slug", "name"]

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
    def from_json(cls, json_str: str) -> WorkspaceV1:
        """Create an instance of WorkspaceV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkspaceV1:
        """Create an instance of WorkspaceV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkspaceV1.parse_obj(obj)

        _obj = WorkspaceV1.parse_obj({
            "id": obj.get("id"),
            "slug": obj.get("slug"),
            "name": obj.get("name")
        })
        return _obj


