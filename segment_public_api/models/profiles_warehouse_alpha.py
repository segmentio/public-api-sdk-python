# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.0.1
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from segment_public_api.models.warehouse_metadata_v1 import WarehouseMetadataV1

class ProfilesWarehouseAlpha(BaseModel):
    """
    Defines a Profiles data Warehouse used as a Destination for Segment data.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of the Warehouse.")
    space_id: StrictStr = Field(..., alias="spaceId", description="The Space id.")
    metadata: WarehouseMetadataV1 = Field(...)
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="The id of the Workspace that owns this Warehouse.")
    enabled: StrictBool = Field(..., description="When set to true, this Warehouse receives data.")
    settings: Dict[str, Any] = Field(..., description="A key-value object that contains instance-specific Warehouse settings.")
    schema_name: Optional[StrictStr] = Field(None, alias="schemaName", description="The custom schema name that Segment uses on the Warehouse side.")
    __properties = ["id", "spaceId", "metadata", "workspaceId", "enabled", "settings", "schemaName"]

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
    def from_json(cls, json_str: str) -> ProfilesWarehouseAlpha:
        """Create an instance of ProfilesWarehouseAlpha from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProfilesWarehouseAlpha:
        """Create an instance of ProfilesWarehouseAlpha from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProfilesWarehouseAlpha.parse_obj(obj)

        _obj = ProfilesWarehouseAlpha.parse_obj({
            "id": obj.get("id"),
            "space_id": obj.get("spaceId"),
            "metadata": WarehouseMetadataV1.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "workspace_id": obj.get("workspaceId"),
            "enabled": obj.get("enabled"),
            "settings": obj.get("settings"),
            "schema_name": obj.get("schemaName")
        })
        return _obj


