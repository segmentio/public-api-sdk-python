# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 55.1.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class WarehouseSyncOverrideV1(BaseModel):
    """
    Represents the override for a Source/collection/property? path to apply to a Warehouse.  # noqa: E501
    """
    source_id: StrictStr = Field(..., alias="sourceId", description="The id of the Source this schema item applies to.")
    collection: Optional[StrictStr] = Field(None, description="The collection the schema item override applies to.")
    enabled: StrictBool = Field(..., description="Enable to apply the override.")
    var_property: Optional[StrictStr] = Field(None, alias="property", description="A property within the collection to which the override applies.")
    __properties = ["sourceId", "collection", "enabled", "property"]

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
    def from_json(cls, json_str: str) -> WarehouseSyncOverrideV1:
        """Create an instance of WarehouseSyncOverrideV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WarehouseSyncOverrideV1:
        """Create an instance of WarehouseSyncOverrideV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WarehouseSyncOverrideV1.parse_obj(obj)

        _obj = WarehouseSyncOverrideV1.parse_obj({
            "source_id": obj.get("sourceId"),
            "collection": obj.get("collection"),
            "enabled": obj.get("enabled"),
            "var_property": obj.get("property")
        })
        return _obj


