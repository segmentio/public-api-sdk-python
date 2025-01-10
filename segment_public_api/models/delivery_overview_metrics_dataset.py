# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.3.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from segment_public_api.models.delivery_overview_metrics_datapoint import DeliveryOverviewMetricsDatapoint

class DeliveryOverviewMetricsDataset(BaseModel):
    """
    Dataset within GetDeliveryOverviewMetricsBetaOutput.  # noqa: E501
    """
    event_name: Optional[StrictStr] = Field(None, alias="eventName", description="The name of the event if group By[] included 'event Name' in the request.")
    app_version: Optional[StrictStr] = Field(None, alias="appVersion", description="The version of the app if group By[] included 'app Version' in the request.")
    event_type: Optional[StrictStr] = Field(None, alias="eventType", description="The event type if group By[] included 'event Type' in the request.")
    discard_reason: Optional[StrictStr] = Field(None, alias="discardReason", description="The discard reason for dropped events if group By[] included 'discard Reason' in the request.")
    total: Union[StrictFloat, StrictInt] = Field(..., description="Holds the count of all event counts over the time frame of the series.")
    series: conlist(DeliveryOverviewMetricsDatapoint) = Field(..., description="A list of the event counts broken down by the requested granularity, time frame, and group By options.")
    total_retry_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalRetryCount", description="The number of events successfully delivered upon retry.")
    __properties = ["eventName", "appVersion", "eventType", "discardReason", "total", "series", "totalRetryCount"]

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
    def from_json(cls, json_str: str) -> DeliveryOverviewMetricsDataset:
        """Create an instance of DeliveryOverviewMetricsDataset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in series (list)
        _items = []
        if self.series:
            for _item in self.series:
                if _item:
                    _items.append(_item.to_dict())
            _dict['series'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeliveryOverviewMetricsDataset:
        """Create an instance of DeliveryOverviewMetricsDataset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeliveryOverviewMetricsDataset.parse_obj(obj)

        _obj = DeliveryOverviewMetricsDataset.parse_obj({
            "event_name": obj.get("eventName"),
            "app_version": obj.get("appVersion"),
            "event_type": obj.get("eventType"),
            "discard_reason": obj.get("discardReason"),
            "total": obj.get("total"),
            "series": [DeliveryOverviewMetricsDatapoint.from_dict(_item) for _item in obj.get("series")] if obj.get("series") is not None else None,
            "total_retry_count": obj.get("totalRetryCount")
        })
        return _obj


