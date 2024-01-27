# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 39.0.0
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

class CreateDestinationSubscriptionAlphaInput(BaseModel):
    """
    The basic input parameters for creating a Destination subscription.  # noqa: E501
    """
    name: StrictStr = Field(..., description="A user-defined name for the subscription.")
    action_id: StrictStr = Field(..., alias="actionId", description="The associated action id the subscription should trigger.")
    trigger: StrictStr = Field(..., description="The FQL statement.")
    enabled: StrictBool = Field(..., description="Is the subscription enabled.")
    settings: Optional[Dict[str, Any]] = Field(None, description="Represents settings used to configure an action subscription.")
    model_id: Optional[StrictStr] = Field(None, alias="modelId", description="When creating a Reverse ETL connection, indicates the Model being used to extract data.")
    __properties = ["name", "actionId", "trigger", "enabled", "settings", "modelId"]

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
    def from_json(cls, json_str: str) -> CreateDestinationSubscriptionAlphaInput:
        """Create an instance of CreateDestinationSubscriptionAlphaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateDestinationSubscriptionAlphaInput:
        """Create an instance of CreateDestinationSubscriptionAlphaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateDestinationSubscriptionAlphaInput.parse_obj(obj)

        _obj = CreateDestinationSubscriptionAlphaInput.parse_obj({
            "name": obj.get("name"),
            "action_id": obj.get("actionId"),
            "trigger": obj.get("trigger"),
            "enabled": obj.get("enabled"),
            "settings": obj.get("settings"),
            "model_id": obj.get("modelId")
        })
        return _obj


