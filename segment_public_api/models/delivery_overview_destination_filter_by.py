# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 54.3.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class DeliveryOverviewDestinationFilterBy(BaseModel):
    """
    The `DeliveryOverviewDestinationFilterBy` object is a map of the filterable fields and their values.  # noqa: E501
    """
    discard_reason: Optional[conlist(StrictStr)] = Field(None, alias="discardReason", description="A list of strings of discard reasons.  See [Discard Record Documentation](https://segment.com/docs/connections/delivery-overview/#troubleshooting) for valid error codes.")
    event_name: Optional[conlist(StrictStr)] = Field(None, alias="eventName", description="A list of strings of event names.")
    event_type: Optional[conlist(StrictStr)] = Field(None, alias="eventType", description="A list of strings of event types. Valid options are: `alias`, `group`, `identify`, `page`, `screen`, and `track`.")
    app_version: Optional[conlist(StrictStr)] = Field(None, alias="appVersion", description="A list of strings of app versions.")
    subscription_id: Optional[conlist(StrictStr)] = Field(None, alias="subscriptionId", description="A list of strings of subscription IDs for Actions Destinations.")
    activation_id: Optional[conlist(StrictStr)] = Field(None, alias="activationId", description="A list of strings of event context IDs from a Linked Audience mapping/activation.")
    audience_id: Optional[conlist(StrictStr)] = Field(None, alias="audienceId", description="A list of strings of audience IDs for a Linked Audience.")
    space_id: Optional[conlist(StrictStr)] = Field(None, alias="spaceId", description="A list of strings of space IDs for a Linked Audience.")
    __properties = ["discardReason", "eventName", "eventType", "appVersion", "subscriptionId", "activationId", "audienceId", "spaceId"]

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
    def from_json(cls, json_str: str) -> DeliveryOverviewDestinationFilterBy:
        """Create an instance of DeliveryOverviewDestinationFilterBy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeliveryOverviewDestinationFilterBy:
        """Create an instance of DeliveryOverviewDestinationFilterBy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeliveryOverviewDestinationFilterBy.parse_obj(obj)

        _obj = DeliveryOverviewDestinationFilterBy.parse_obj({
            "discard_reason": obj.get("discardReason"),
            "event_name": obj.get("eventName"),
            "event_type": obj.get("eventType"),
            "app_version": obj.get("appVersion"),
            "subscription_id": obj.get("subscriptionId"),
            "activation_id": obj.get("activationId"),
            "audience_id": obj.get("audienceId"),
            "space_id": obj.get("spaceId")
        })
        return _obj


