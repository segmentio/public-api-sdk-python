# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 55.0.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class RequestError(BaseModel):
    """
    Represents any error that could have occurred while performing a request.  # noqa: E501
    """
    type: StrictStr = Field(..., description="The type for this error (validation, server, unknown, etc).")
    message: Optional[StrictStr] = Field(None, description="An error message attached to this error.")
    field: Optional[StrictStr] = Field(None, description="The name of an input field from the request that triggered this error.")
    data: Optional[Any] = Field(None, description="Any extra data associated with this error.")
    status: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Http status code.")
    __properties = ["type", "message", "field", "data", "status"]

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
    def from_json(cls, json_str: str) -> RequestError:
        """Create an instance of RequestError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestError:
        """Create an instance of RequestError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestError.parse_obj(obj)

        _obj = RequestError.parse_obj({
            "type": obj.get("type"),
            "message": obj.get("message"),
            "field": obj.get("field"),
            "data": obj.get("data"),
            "status": obj.get("status")
        })
        return _obj


