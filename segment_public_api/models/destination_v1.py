# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 44.0.0
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
from segment_public_api.models.destination_metadata_v1 import DestinationMetadataV1

class DestinationV1(BaseModel):
    """
    Business tools or apps that you can connect to the data flowing through Segment.  This is equal to the Destination object in Config API, with the following fields omitted: - catalogId - createTime - updateTime - connectionMode.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The unique identifier of this instance of a Destination.  Config API note: analogous to `name`.")
    name: Optional[StrictStr] = Field(None, description="The name of this instance of a Destination.  Config API note: equal to `displayName`.")
    enabled: StrictBool = Field(..., description="Whether this instance of a Destination receives data.")
    metadata: DestinationMetadataV1 = Field(...)
    source_id: StrictStr = Field(..., alias="sourceId", description="The id of a Source connected to this instance of a Destination.  Config API note: analogous to `parent`.")
    settings: Dict[str, Any] = Field(..., description="The collection of settings associated with a Destination.  Config API note: equal to `config`.")
    __properties = ["id", "name", "enabled", "metadata", "sourceId", "settings"]

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
    def from_json(cls, json_str: str) -> DestinationV1:
        """Create an instance of DestinationV1 from a JSON string"""
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
    def from_dict(cls, obj: dict) -> DestinationV1:
        """Create an instance of DestinationV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationV1.parse_obj(obj)

        _obj = DestinationV1.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "metadata": DestinationMetadataV1.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "source_id": obj.get("sourceId"),
            "settings": obj.get("settings")
        })
        return _obj


