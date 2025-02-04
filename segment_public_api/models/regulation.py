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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from segment_public_api.models.stream_status_v1 import StreamStatusV1

class Regulation(BaseModel):
    """
    The regulate request.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of the regulate request.")
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="The id of the Workspace that the regulate request belongs to.")
    overall_status: StrictStr = Field(..., alias="overallStatus", description="The current status of the regulate request.")
    finished_at: Optional[StrictStr] = Field(None, alias="finishedAt", description="The timestamp of when the request finished.")
    created_at: StrictStr = Field(..., alias="createdAt", description="The timestamp of the creation of the request.")
    stream_status: conlist(StreamStatusV1) = Field(..., alias="streamStatus", description="The status of each stream including all the Destinations that correspond to the stream.")
    __properties = ["id", "workspaceId", "overallStatus", "finishedAt", "createdAt", "streamStatus"]

    @validator('overall_status')
    def overall_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('FAILED', 'FINISHED', 'INITIALIZED', 'INVALID', 'IN_PROGRESS', 'NOT_SUPPORTED', 'PARTIAL_SUCCESS'):
            raise ValueError("must be one of enum values ('FAILED', 'FINISHED', 'INITIALIZED', 'INVALID', 'IN_PROGRESS', 'NOT_SUPPORTED', 'PARTIAL_SUCCESS')")
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
    def from_json(cls, json_str: str) -> Regulation:
        """Create an instance of Regulation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in stream_status (list)
        _items = []
        if self.stream_status:
            for _item in self.stream_status:
                if _item:
                    _items.append(_item.to_dict())
            _dict['streamStatus'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Regulation:
        """Create an instance of Regulation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Regulation.parse_obj(obj)

        _obj = Regulation.parse_obj({
            "id": obj.get("id"),
            "workspace_id": obj.get("workspaceId"),
            "overall_status": obj.get("overallStatus"),
            "finished_at": obj.get("finishedAt"),
            "created_at": obj.get("createdAt"),
            "stream_status": [StreamStatusV1.from_dict(_item) for _item in obj.get("streamStatus")] if obj.get("streamStatus") is not None else None
        })
        return _obj


