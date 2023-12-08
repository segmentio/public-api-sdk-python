# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 38.4.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from segment_public_api.models.label_v1 import LabelV1
from segment_public_api.models.source_metadata_v1 import SourceMetadataV1

class SourceAlpha(BaseModel):
    """
    Defines a data Source for Segment data.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of the Source.  Config API note: analogous to `name`.")
    slug: StrictStr = Field(..., description="The slug used to identify the Source in the Segment app.  Config API note: equal to `name`.")
    name: Optional[StrictStr] = Field(None, description="The name of the Source.  Config API note: equal to `displayName`.")
    metadata: SourceMetadataV1 = Field(...)
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="The id of the Workspace that owns the Source.  Config API note: equal to `parent`.")
    enabled: StrictBool = Field(..., description="Enable to receive data from the Source.")
    write_keys: conlist(StrictStr) = Field(..., alias="writeKeys", description="The write keys used to send data from the Source. This field is left empty when the current token does not have the 'source admin' permission.")
    settings: Optional[Dict[str, Any]] = Field(None, description="A key-value object that contains instance-specific settings for a Source.  The `options` field in the Source metadata defines the schema of this object.")
    labels: conlist(LabelV1) = Field(..., description="A list of labels applied to the Source.")
    __properties = ["id", "slug", "name", "metadata", "workspaceId", "enabled", "writeKeys", "settings", "labels"]

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
    def from_json(cls, json_str: str) -> SourceAlpha:
        """Create an instance of SourceAlpha from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SourceAlpha:
        """Create an instance of SourceAlpha from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SourceAlpha.parse_obj(obj)

        _obj = SourceAlpha.parse_obj({
            "id": obj.get("id"),
            "slug": obj.get("slug"),
            "name": obj.get("name"),
            "metadata": SourceMetadataV1.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "workspace_id": obj.get("workspaceId"),
            "enabled": obj.get("enabled"),
            "write_keys": obj.get("writeKeys"),
            "settings": obj.get("settings"),
            "labels": [LabelV1.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None
        })
        return _obj


