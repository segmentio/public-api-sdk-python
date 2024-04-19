# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 49.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from segment_public_api.models.sync_extract_phase import SyncExtractPhase
from segment_public_api.models.sync_load_phase import SyncLoadPhase

class ReverseETLSyncOutput(BaseModel):
    """
    Defines the result of getting the sync status of a RETL connection.  # noqa: E501
    """
    sync_id: StrictStr = Field(..., alias="syncId", description="The id of the sync.")
    model_id: StrictStr = Field(..., alias="modelId", description="The Model id of the sync.")
    source_id: StrictStr = Field(..., alias="sourceId", description="The Source id of the sync.")
    sync_status: StrictStr = Field(..., alias="syncStatus", description="The status of the sync. It currently can be IN_PROGRESS, FAIL, SUCCESS, PARTIAL_SUCCESS.")
    duration: StrictStr = Field(..., description="The duration of the sync.")
    started_at: StrictStr = Field(..., alias="startedAt", description="When the sync started.")
    finished_at: Optional[StrictStr] = Field(None, alias="finishedAt", description="When the sync started.")
    extract_phase: Optional[SyncExtractPhase] = Field(None, alias="extractPhase")
    load_phase: Optional[SyncLoadPhase] = Field(None, alias="loadPhase")
    error: Optional[StrictStr] = Field(None, description="Error message if applicable.")
    error_code: Optional[StrictStr] = Field(None, alias="errorCode", description="Error code indicates a fatal sync error code, if applicable.")
    __properties = ["syncId", "modelId", "sourceId", "syncStatus", "duration", "startedAt", "finishedAt", "extractPhase", "loadPhase", "error", "errorCode"]

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
    def from_json(cls, json_str: str) -> ReverseETLSyncOutput:
        """Create an instance of ReverseETLSyncOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of extract_phase
        if self.extract_phase:
            _dict['extractPhase'] = self.extract_phase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of load_phase
        if self.load_phase:
            _dict['loadPhase'] = self.load_phase.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReverseETLSyncOutput:
        """Create an instance of ReverseETLSyncOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReverseETLSyncOutput.parse_obj(obj)

        _obj = ReverseETLSyncOutput.parse_obj({
            "sync_id": obj.get("syncId"),
            "model_id": obj.get("modelId"),
            "source_id": obj.get("sourceId"),
            "sync_status": obj.get("syncStatus"),
            "duration": obj.get("duration"),
            "started_at": obj.get("startedAt"),
            "finished_at": obj.get("finishedAt"),
            "extract_phase": SyncExtractPhase.from_dict(obj.get("extractPhase")) if obj.get("extractPhase") is not None else None,
            "load_phase": SyncLoadPhase.from_dict(obj.get("loadPhase")) if obj.get("loadPhase") is not None else None,
            "error": obj.get("error"),
            "error_code": obj.get("errorCode")
        })
        return _obj


