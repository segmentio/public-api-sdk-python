# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 53.2.1
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

class CreateDestinationV1Input(BaseModel):
    """
    Creates a new Destination.  # noqa: E501
    """
    source_id: StrictStr = Field(..., alias="sourceId", description="The id of the Source to connect to this Destination instance.  Config API note: analogous to `parent`.")
    metadata_id: StrictStr = Field(..., alias="metadataId", description="The id of the metadata to link to the new Destination.")
    enabled: Optional[StrictBool] = Field(None, description="Whether this Destination should receive data.")
    name: Optional[StrictStr] = Field(None, description="Defines the display name of the Destination.  Config API note: equal to `displayName`.")
    settings: Dict[str, Any] = Field(..., description="An object that contains settings for the Destination based on the \"required\" and \"advanced\" settings present in the Destination metadata.  Config API note: equal to `config`.")
    __properties = ["sourceId", "metadataId", "enabled", "name", "settings"]

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
    def from_json(cls, json_str: str) -> CreateDestinationV1Input:
        """Create an instance of CreateDestinationV1Input from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateDestinationV1Input:
        """Create an instance of CreateDestinationV1Input from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateDestinationV1Input.parse_obj(obj)

        _obj = CreateDestinationV1Input.parse_obj({
            "source_id": obj.get("sourceId"),
            "metadata_id": obj.get("metadataId"),
            "enabled": obj.get("enabled"),
            "name": obj.get("name"),
            "settings": obj.get("settings")
        })
        return _obj


