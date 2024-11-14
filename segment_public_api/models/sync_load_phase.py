# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class SyncLoadPhase(BaseModel):
    """
    Object representing the load phase + details.  # noqa: E501
    """
    deliver_success_count: StrictStr = Field(..., alias="deliverSuccessCount", description="Counts the subset of records successfully delivered to the downstream Destination.")
    deliver_failure_count: StrictStr = Field(..., alias="deliverFailureCount", description="Counts the subset of records status that failed to be delivered by either receiving a permanent error (for example, 400 Bad Request) or by exhausting all retries for temporary errors (for example, 429 Too Many Requests).")
    error_code: StrictStr = Field(..., alias="errorCode", description="Error code indicates a fatal sync error code, if applicable.")
    started_at: StrictStr = Field(..., alias="startedAt", description="Time that the load phase started.")
    finished_at: StrictStr = Field(..., alias="finishedAt", description="Time that the load phase finished.")
    __properties = ["deliverSuccessCount", "deliverFailureCount", "errorCode", "startedAt", "finishedAt"]

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
    def from_json(cls, json_str: str) -> SyncLoadPhase:
        """Create an instance of SyncLoadPhase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SyncLoadPhase:
        """Create an instance of SyncLoadPhase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SyncLoadPhase.parse_obj(obj)

        _obj = SyncLoadPhase.parse_obj({
            "deliver_success_count": obj.get("deliverSuccessCount"),
            "deliver_failure_count": obj.get("deliverFailureCount"),
            "error_code": obj.get("errorCode"),
            "started_at": obj.get("startedAt"),
            "finished_at": obj.get("finishedAt")
        })
        return _obj


