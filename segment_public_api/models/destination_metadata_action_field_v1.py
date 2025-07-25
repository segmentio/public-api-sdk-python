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


from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator

class DestinationMetadataActionFieldV1(BaseModel):
    """
    Represents a field used in configuring an action.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The primary key of the field.")
    sort_order: Union[StrictFloat, StrictInt] = Field(..., alias="sortOrder", description="The order this particular field is (used in the UI for displaying the fields in a specified order).")
    field_key: StrictStr = Field(..., alias="fieldKey", description="A unique machine-readable key for the field. Should ideally match the expected key in the action\\'s API request.")
    label: StrictStr = Field(..., description="A human-readable label for this value.")
    type: StrictStr = Field(..., description="The data type for this value.")
    description: StrictStr = Field(..., description="A human-readable description of this value. You can use Markdown.")
    placeholder: Optional[StrictStr] = Field(None, description="An example value displayed but not saved.")
    default_value: Optional[Any] = Field(None, alias="defaultValue", description="A default value that is saved the first time an action is created.")
    required: StrictBool = Field(..., description="Whether this field is required.")
    multiple: StrictBool = Field(..., description="Whether a user can provide multiples of this field.")
    choices: Optional[Any] = Field(None, description="A list of machine-readable value/label pairs to populate a static dropdown.")
    dynamic: StrictBool = Field(..., description="Whether this field should execute a dynamic request to fetch choices to populate a dropdown. When true, `choices` is ignored.")
    allow_null: StrictBool = Field(..., alias="allowNull", description="Whether this field allows null values.")
    hidden: Optional[StrictBool] = Field(None, description="Whether the action field should be hidden or not.")
    __properties = ["id", "sortOrder", "fieldKey", "label", "type", "description", "placeholder", "defaultValue", "required", "multiple", "choices", "dynamic", "allowNull", "hidden"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('BOOLEAN', 'DATETIME', 'HIDDEN', 'INTEGER', 'NUMBER', 'OBJECT', 'PASSWORD', 'STRING', 'TEXT'):
            raise ValueError("must be one of enum values ('BOOLEAN', 'DATETIME', 'HIDDEN', 'INTEGER', 'NUMBER', 'OBJECT', 'PASSWORD', 'STRING', 'TEXT')")
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
    def from_json(cls, json_str: str) -> DestinationMetadataActionFieldV1:
        """Create an instance of DestinationMetadataActionFieldV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if default_value (nullable) is None
        # and __fields_set__ contains the field
        if self.default_value is None and "default_value" in self.__fields_set__:
            _dict['defaultValue'] = None

        # set to None if choices (nullable) is None
        # and __fields_set__ contains the field
        if self.choices is None and "choices" in self.__fields_set__:
            _dict['choices'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationMetadataActionFieldV1:
        """Create an instance of DestinationMetadataActionFieldV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationMetadataActionFieldV1.parse_obj(obj)

        _obj = DestinationMetadataActionFieldV1.parse_obj({
            "id": obj.get("id"),
            "sort_order": obj.get("sortOrder"),
            "field_key": obj.get("fieldKey"),
            "label": obj.get("label"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "placeholder": obj.get("placeholder"),
            "default_value": obj.get("defaultValue"),
            "required": obj.get("required"),
            "multiple": obj.get("multiple"),
            "choices": obj.get("choices"),
            "dynamic": obj.get("dynamic"),
            "allow_null": obj.get("allowNull"),
            "hidden": obj.get("hidden")
        })
        return _obj


