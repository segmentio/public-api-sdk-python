# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class AuditEventV1(BaseModel):
    """
    Represents an Audit Trail event.  # noqa: E501
    """
    id: StrictStr = Field(..., description="Unique identifier for this audit trail event.")
    timestamp: StrictStr = Field(..., description="The timestamp of this event in ISO-8601 format.")
    type: StrictStr = Field(..., description="The type of this event.")
    actor: StrictStr = Field(..., description="The user or API token that triggered this event.")
    actor_email: Optional[StrictStr] = Field(None, alias="actorEmail", description="The email of the user that triggered this event.")
    resource_id: StrictStr = Field(..., alias="resourceId", description="The identifier of the resource affected by this event.")
    resource_type: StrictStr = Field(..., alias="resourceType", description="The kind of resource affected by this event.")
    resource_name: StrictStr = Field(..., alias="resourceName", description="The name of the resource affected by this event.")
    __properties = ["id", "timestamp", "type", "actor", "actorEmail", "resourceId", "resourceType", "resourceName"]

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
    def from_json(cls, json_str: str) -> AuditEventV1:
        """Create an instance of AuditEventV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditEventV1:
        """Create an instance of AuditEventV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditEventV1.parse_obj(obj)

        _obj = AuditEventV1.parse_obj({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "type": obj.get("type"),
            "actor": obj.get("actor"),
            "actor_email": obj.get("actorEmail"),
            "resource_id": obj.get("resourceId"),
            "resource_type": obj.get("resourceType"),
            "resource_name": obj.get("resourceName")
        })
        return _obj


