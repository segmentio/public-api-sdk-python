# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.13.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class UpdateActivationForAudienceAlphaInput(BaseModel):
    """
    Input to update an activation.  # noqa: E501
    """
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="The Workspace id.")
    enabled: Optional[StrictBool] = Field(None, description="Determines whether an activation is enabled.")
    event_emitter: Optional[Any] = Field(..., alias="eventEmitter", description="Configuration settings for the event emitter to be created.")
    subscription: Optional[Any] = Field(..., description="Subscription info to connect the event emitter to a Destination attached to the audience.")
    __properties = ["workspaceId", "enabled", "eventEmitter", "subscription"]

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
    def from_json(cls, json_str: str) -> UpdateActivationForAudienceAlphaInput:
        """Create an instance of UpdateActivationForAudienceAlphaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if event_emitter (nullable) is None
        # and __fields_set__ contains the field
        if self.event_emitter is None and "event_emitter" in self.__fields_set__:
            _dict['eventEmitter'] = None

        # set to None if subscription (nullable) is None
        # and __fields_set__ contains the field
        if self.subscription is None and "subscription" in self.__fields_set__:
            _dict['subscription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateActivationForAudienceAlphaInput:
        """Create an instance of UpdateActivationForAudienceAlphaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateActivationForAudienceAlphaInput.parse_obj(obj)

        _obj = UpdateActivationForAudienceAlphaInput.parse_obj({
            "workspace_id": obj.get("workspaceId"),
            "enabled": obj.get("enabled"),
            "event_emitter": obj.get("eventEmitter"),
            "subscription": obj.get("subscription")
        })
        return _obj


