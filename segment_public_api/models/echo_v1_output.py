# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 55.2.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictStr, validator

class EchoV1Output(BaseModel):
    """
    Echo response.  # noqa: E501
    """
    method: StrictStr = Field(..., description="The HTTP method used for this round-trip.  Currently, this endpoint supports only `get` and `post` methods.")
    message: StrictStr = Field(..., description="The string passed in the `message` input field.")
    headers: Dict[str, Any] = Field(..., description="The request's HTTP headers.")
    __properties = ["method", "message", "headers"]

    @validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('get', 'post'):
            raise ValueError("must be one of enum values ('get', 'post')")
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
    def from_json(cls, json_str: str) -> EchoV1Output:
        """Create an instance of EchoV1Output from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EchoV1Output:
        """Create an instance of EchoV1Output from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EchoV1Output.parse_obj(obj)

        _obj = EchoV1Output.parse_obj({
            "method": obj.get("method"),
            "message": obj.get("message"),
            "headers": obj.get("headers")
        })
        return _obj


