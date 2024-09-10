# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 54.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from segment_public_api.models.integration_option_beta import IntegrationOptionBeta
from segment_public_api.models.logos_beta import LogosBeta

class WarehouseMetadataV1(BaseModel):
    """
    The metadata for an instance of Segment’s data Warehouse product.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of this object.")
    name: StrictStr = Field(..., description="The name of this object.")
    slug: StrictStr = Field(..., description="A human-readable, unique identifier for object.")
    description: StrictStr = Field(..., description="A description, in English, of this object.")
    logos: LogosBeta = Field(...)
    options: conlist(IntegrationOptionBeta) = Field(..., description="The Integration options for this object.")
    __properties = ["id", "name", "slug", "description", "logos", "options"]

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
    def from_json(cls, json_str: str) -> WarehouseMetadataV1:
        """Create an instance of WarehouseMetadataV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of logos
        if self.logos:
            _dict['logos'] = self.logos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WarehouseMetadataV1:
        """Create an instance of WarehouseMetadataV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WarehouseMetadataV1.parse_obj(obj)

        _obj = WarehouseMetadataV1.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "description": obj.get("description"),
            "logos": LogosBeta.from_dict(obj.get("logos")) if obj.get("logos") is not None else None,
            "options": [IntegrationOptionBeta.from_dict(_item) for _item in obj.get("options")] if obj.get("options") is not None else None
        })
        return _obj


