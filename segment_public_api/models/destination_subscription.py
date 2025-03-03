# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.4.0
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
from segment_public_api.models.reverse_etl_schedule_definition import ReverseEtlScheduleDefinition

class DestinationSubscription(BaseModel):
    """
    DestinationSubscription
    """
    id: StrictStr = Field(..., description="The unique identifier for the subscription.")
    name: StrictStr = Field(..., description="The name of the subscription.")
    action_id: StrictStr = Field(..., alias="actionId", description="The unique identifier for the Destination action to trigger.")
    action_slug: StrictStr = Field(..., alias="actionSlug", description="The URL-friendly key for the associated Destination action.")
    destination_id: StrictStr = Field(..., alias="destinationId", description="The associated Destination instance id.")
    enabled: StrictBool = Field(..., description="Is the subscription enabled.")
    settings: Dict[str, Any] = Field(..., description="Represents settings used to configure an action subscription.")
    trigger: StrictStr = Field(..., description="FQL string that describes what events should trigger a Destination action.")
    model_id: Optional[StrictStr] = Field(None, alias="modelId", description="The unique identifier for the linked ReverseETLModel, if this part of a Reverse ETL connection.")
    reverse_etl_schedule: Optional[ReverseEtlScheduleDefinition] = Field(None, alias="reverseETLSchedule")
    __properties = ["id", "name", "actionId", "actionSlug", "destinationId", "enabled", "settings", "trigger", "modelId", "reverseETLSchedule"]

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
    def from_json(cls, json_str: str) -> DestinationSubscription:
        """Create an instance of DestinationSubscription from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reverse_etl_schedule
        if self.reverse_etl_schedule:
            _dict['reverseETLSchedule'] = self.reverse_etl_schedule.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationSubscription:
        """Create an instance of DestinationSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationSubscription.parse_obj(obj)

        _obj = DestinationSubscription.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "action_id": obj.get("actionId"),
            "action_slug": obj.get("actionSlug"),
            "destination_id": obj.get("destinationId"),
            "enabled": obj.get("enabled"),
            "settings": obj.get("settings"),
            "trigger": obj.get("trigger"),
            "model_id": obj.get("modelId"),
            "reverse_etl_schedule": ReverseEtlScheduleDefinition.from_dict(obj.get("reverseETLSchedule")) if obj.get("reverseETLSchedule") is not None else None
        })
        return _obj


