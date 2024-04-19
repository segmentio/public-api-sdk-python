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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

class PreviewDestinationFilterV1Output(BaseModel):
    """
    Preview output from applying the Destination filter. Segment modifies or nullifies payloads depending on the provided filter actions.  # noqa: E501
    """
    input_payload: Dict[str, Any] = Field(..., alias="inputPayload", description="The pre-filter JSON input.")
    result: Optional[Dict[str, Any]] = Field(..., description="The filtered JSON output.")
    __properties = ["inputPayload", "result"]

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
    def from_json(cls, json_str: str) -> PreviewDestinationFilterV1Output:
        """Create an instance of PreviewDestinationFilterV1Output from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if result (nullable) is None
        # and __fields_set__ contains the field
        if self.result is None and "result" in self.__fields_set__:
            _dict['result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreviewDestinationFilterV1Output:
        """Create an instance of PreviewDestinationFilterV1Output from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PreviewDestinationFilterV1Output.parse_obj(obj)

        _obj = PreviewDestinationFilterV1Output.parse_obj({
            "input_payload": obj.get("inputPayload"),
            "result": obj.get("result")
        })
        return _obj


