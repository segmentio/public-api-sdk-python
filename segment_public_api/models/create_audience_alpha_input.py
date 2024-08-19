# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 53.1.0
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
from segment_public_api.models.audience_computation_definition import AudienceComputationDefinition
from segment_public_api.models.audience_options import AudienceOptions

class CreateAudienceAlphaInput(BaseModel):
    """
    Input to create an audience.  # noqa: E501
    """
    name: StrictStr = Field(..., description="Name of the audience.")
    enabled: Optional[StrictBool] = Field(None, description="Determines whether a computation is enabled.")
    description: Optional[StrictStr] = Field(None, description="Description of the audience.")
    definition: AudienceComputationDefinition = Field(...)
    options: Optional[AudienceOptions] = None
    __properties = ["name", "enabled", "description", "definition", "options"]

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
    def from_json(cls, json_str: str) -> CreateAudienceAlphaInput:
        """Create an instance of CreateAudienceAlphaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateAudienceAlphaInput:
        """Create an instance of CreateAudienceAlphaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateAudienceAlphaInput.parse_obj(obj)

        _obj = CreateAudienceAlphaInput.parse_obj({
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "description": obj.get("description"),
            "definition": AudienceComputationDefinition.from_dict(obj.get("definition")) if obj.get("definition") is not None else None,
            "options": AudienceOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None
        })
        return _obj


