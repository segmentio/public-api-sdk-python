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



from pydantic import BaseModel, Field, StrictStr
from segment_public_api.models.destination_input import DestinationInput

class AddDestinationToAudienceAlphaInput(BaseModel):
    """
    Input to Add a Destination into an Audience.  # noqa: E501
    """
    version_schema: StrictStr = Field(..., alias="versionSchema", description="Version Schema.")
    workspace_id: StrictStr = Field(..., alias="workspaceId", description="The id of the Workspace the audience exists within.")
    destination: DestinationInput = Field(...)
    __properties = ["versionSchema", "workspaceId", "destination"]

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
    def from_json(cls, json_str: str) -> AddDestinationToAudienceAlphaInput:
        """Create an instance of AddDestinationToAudienceAlphaInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddDestinationToAudienceAlphaInput:
        """Create an instance of AddDestinationToAudienceAlphaInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddDestinationToAudienceAlphaInput.parse_obj(obj)

        _obj = AddDestinationToAudienceAlphaInput.parse_obj({
            "version_schema": obj.get("versionSchema"),
            "workspace_id": obj.get("workspaceId"),
            "destination": DestinationInput.from_dict(obj.get("destination")) if obj.get("destination") is not None else None
        })
        return _obj


