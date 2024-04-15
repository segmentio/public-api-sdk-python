# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 48.0.0
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

class CreateSourceV1Input(BaseModel):
    """
    Create a new Source based on a set of parameters.  # noqa: E501
    """
    slug: StrictStr = Field(..., description="The slug by which to identify the Source in the Segment app.")
    enabled: StrictBool = Field(..., description="Enable to allow this Source to send data. Defaults to true.")
    metadata_id: StrictStr = Field(..., alias="metadataId", description="The id of the Source metadata from which this instance of the Source derives.  All Source metadata is available under `/catalog/sources`.")
    settings: Optional[Dict[str, Any]] = Field(None, description="A key-value object that contains instance-specific settings for a Source.  The `options` field in the Source metadata defines the schema of this object.")
    __properties = ["slug", "enabled", "metadataId", "settings"]

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
    def from_json(cls, json_str: str) -> CreateSourceV1Input:
        """Create an instance of CreateSourceV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSourceV1Input:
        """Create an instance of CreateSourceV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSourceV1Input.parse_obj(obj)

        _obj = CreateSourceV1Input.parse_obj({
            "slug": obj.get("slug"),
            "enabled": obj.get("enabled"),
            "metadata_id": obj.get("metadataId"),
            "settings": obj.get("settings")
        })
        return _obj


