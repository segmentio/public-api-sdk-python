# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 37.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from segment_public_api.models.destination_metadata_action_field_v1 import DestinationMetadataActionFieldV1

class DestinationMetadataActionV1(BaseModel):
    """
    Represents an Action, a building block of behavior that can be performed by the Destination.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The primary key of the action.")
    slug: StrictStr = Field(..., description="A machine-readable key unique to the action definition.")
    name: StrictStr = Field(..., description="A human-readable name for the action.")
    description: StrictStr = Field(..., description="A human-readable description of the action. May include Markdown.")
    platform: StrictStr = Field(..., description="The platform on which this action runs.")
    hidden: StrictBool = Field(..., description="Whether the action should be hidden.")
    default_trigger: Optional[StrictStr] = Field(..., alias="defaultTrigger", description="The default value used as the trigger when connecting this action.")
    fields: conlist(DestinationMetadataActionFieldV1) = Field(..., description="The fields expected in order to perform the action.")
    __properties = ["id", "slug", "name", "description", "platform", "hidden", "defaultTrigger", "fields"]

    @validator('platform')
    def platform_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CLOUD', 'MOBILE', 'WEB'):
            raise ValueError("must be one of enum values ('CLOUD', 'MOBILE', 'WEB')")
        return value

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
    def from_json(cls, json_str: str) -> DestinationMetadataActionV1:
        """Create an instance of DestinationMetadataActionV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # set to None if default_trigger (nullable) is None
        # and __fields_set__ contains the field
        if self.default_trigger is None and "default_trigger" in self.__fields_set__:
            _dict['defaultTrigger'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationMetadataActionV1:
        """Create an instance of DestinationMetadataActionV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationMetadataActionV1.parse_obj(obj)

        _obj = DestinationMetadataActionV1.parse_obj({
            "id": obj.get("id"),
            "slug": obj.get("slug"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "platform": obj.get("platform"),
            "hidden": obj.get("hidden"),
            "default_trigger": obj.get("defaultTrigger"),
            "fields": [DestinationMetadataActionFieldV1.from_dict(_item) for _item in obj.get("fields")] if obj.get("fields") is not None else None
        })
        return _obj


