# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 58.1.1
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from segment_public_api.models.destination_state import DestinationState
from segment_public_api.models.exit_destination_state import ExitDestinationState
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

DESTINATIONSINNER_ANY_OF_SCHEMAS = ["DestinationState", "ExitDestinationState"]

class DestinationsInner(BaseModel):
    """
    DestinationsInner
    """

    # data type: DestinationState
    anyof_schema_1_validator: Optional[DestinationState] = None
    # data type: ExitDestinationState
    anyof_schema_2_validator: Optional[ExitDestinationState] = None
    if TYPE_CHECKING:
        actual_instance: Union[DestinationState, ExitDestinationState]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(DESTINATIONSINNER_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = DestinationsInner.construct()
        error_messages = []
        # validate data type: DestinationState
        if not isinstance(v, DestinationState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DestinationState`")
        else:
            return v

        # validate data type: ExitDestinationState
        if not isinstance(v, ExitDestinationState):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExitDestinationState`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in DestinationsInner with anyOf schemas: DestinationState, ExitDestinationState. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationsInner:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> DestinationsInner:
        """Returns the object represented by the json string"""
        instance = DestinationsInner.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[DestinationState] = None
        try:
            instance.actual_instance = DestinationState.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[ExitDestinationState] = None
        try:
            instance.actual_instance = ExitDestinationState.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DestinationsInner with anyOf schemas: DestinationState, ExitDestinationState. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


