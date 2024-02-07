# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 40.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from segment_public_api.models.property_rename_beta import PropertyRenameBeta
from segment_public_api.models.property_value_transformation_beta import PropertyValueTransformationBeta

class CreateTransformationBetaInput(BaseModel):
    """
    The input to create a Transformation.  # noqa: E501
    """
    name: StrictStr = Field(..., description="The name of the Transformation.")
    source_id: StrictStr = Field(..., alias="sourceId", description="The Source to be associated with the Transformation.")
    destination_metadata_id: Optional[StrictStr] = Field(None, alias="destinationMetadataId", description="The optional Destination metadata id to be associated with the Transformation.")
    enabled: StrictBool = Field(..., description="If the Transformation should be enabled.")
    var_if: StrictStr = Field(..., alias="if", description="If statement ([FQL](https://segment.com/docs/config-api/fql/)) to match events.  For standard event matchers, use the following:  Track -\\> \"event='\\<eventName\\>'\"  Identify -\\> \"type='identify'\"  Group -\\> \"type='group'\"")
    new_event_name: Optional[StrictStr] = Field(None, alias="newEventName", description="Optional new event name for renaming events. Works only for 'track' event type.")
    property_renames: Optional[conlist(PropertyRenameBeta)] = Field(None, alias="propertyRenames", description="Optional array for renaming properties collected by your events.")
    property_value_transformations: Optional[conlist(PropertyValueTransformationBeta)] = Field(None, alias="propertyValueTransformations", description="Optional array for transforming properties and values collected by your events. Limited to 10 properties.")
    __properties = ["name", "sourceId", "destinationMetadataId", "enabled", "if", "newEventName", "propertyRenames", "propertyValueTransformations"]

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
    def from_json(cls, json_str: str) -> CreateTransformationBetaInput:
        """Create an instance of CreateTransformationBetaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in property_renames (list)
        _items = []
        if self.property_renames:
            for _item in self.property_renames:
                if _item:
                    _items.append(_item.to_dict())
            _dict['propertyRenames'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in property_value_transformations (list)
        _items = []
        if self.property_value_transformations:
            for _item in self.property_value_transformations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['propertyValueTransformations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTransformationBetaInput:
        """Create an instance of CreateTransformationBetaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTransformationBetaInput.parse_obj(obj)

        _obj = CreateTransformationBetaInput.parse_obj({
            "name": obj.get("name"),
            "source_id": obj.get("sourceId"),
            "destination_metadata_id": obj.get("destinationMetadataId"),
            "enabled": obj.get("enabled"),
            "var_if": obj.get("if"),
            "new_event_name": obj.get("newEventName"),
            "property_renames": [PropertyRenameBeta.from_dict(_item) for _item in obj.get("propertyRenames")] if obj.get("propertyRenames") is not None else None,
            "property_value_transformations": [PropertyValueTransformationBeta.from_dict(_item) for _item in obj.get("propertyValueTransformations")] if obj.get("propertyValueTransformations") is not None else None
        })
        return _obj


