# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field
from segment_public_api.models.reverse_etl_manual_sync_job_output import ReverseETLManualSyncJobOutput

class CreateReverseETLManualSyncOutput(BaseModel):
    """
    Output for triggering a manual sync for a RETL connection.  # noqa: E501
    """
    reverse_etl_manual_sync: ReverseETLManualSyncJobOutput = Field(..., alias="reverseETLManualSync")
    __properties = ["reverseETLManualSync"]

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
    def from_json(cls, json_str: str) -> CreateReverseETLManualSyncOutput:
        """Create an instance of CreateReverseETLManualSyncOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reverse_etl_manual_sync
        if self.reverse_etl_manual_sync:
            _dict['reverseETLManualSync'] = self.reverse_etl_manual_sync.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateReverseETLManualSyncOutput:
        """Create an instance of CreateReverseETLManualSyncOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateReverseETLManualSyncOutput.parse_obj(obj)

        _obj = CreateReverseETLManualSyncOutput.parse_obj({
            "reverse_etl_manual_sync": ReverseETLManualSyncJobOutput.from_dict(obj.get("reverseETLManualSync")) if obj.get("reverseETLManualSync") is not None else None
        })
        return _obj


