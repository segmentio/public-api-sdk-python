# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 50.1.0
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from segment_public_api.models.function_setting_v1 import FunctionSettingV1

class Function(BaseModel):
    """
    A Function object.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="An identifier for this Function.")
    resource_type: Optional[StrictStr] = Field(None, alias="resourceType", description="The Function type.  Config API note: equal to `type`.")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt", description="The time this Function was created.")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="The id of the user who created this Function.")
    code: Optional[StrictStr] = Field(None, description="The Function code.")
    deployed_at: Optional[StrictStr] = Field(None, alias="deployedAt", description="The time of this Function's last deployment.")
    settings: Optional[conlist(FunctionSettingV1)] = Field(None, description="The list of settings for this Function.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="A display name for this Function.")
    description: Optional[StrictStr] = Field(None, description="A description for this Function.")
    logo_url: Optional[StrictStr] = Field(None, alias="logoUrl", description="The URL of the logo for this Function.")
    preview_webhook_url: Optional[StrictStr] = Field(None, alias="previewWebhookUrl", description="The preview webhook URL for this Function.")
    batch_max_count: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="batchMaxCount", description="The max count of the batch for this Function.")
    catalog_id: Optional[StrictStr] = Field(None, alias="catalogId", description="The catalog id of this Function.")
    is_latest_version: Optional[StrictBool] = Field(None, alias="isLatestVersion", description="Whether the deployment of this Function is the latest version.")
    __properties = ["id", "resourceType", "createdAt", "createdBy", "code", "deployedAt", "settings", "displayName", "description", "logoUrl", "previewWebhookUrl", "batchMaxCount", "catalogId", "isLatestVersion"]

    @validator('resource_type')
    def resource_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DESTINATION', 'INSERT_DESTINATION', 'SOURCE'):
            raise ValueError("must be one of enum values ('DESTINATION', 'INSERT_DESTINATION', 'SOURCE')")
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
    def from_json(cls, json_str: str) -> Function:
        """Create an instance of Function from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in settings (list)
        _items = []
        if self.settings:
            for _item in self.settings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['settings'] = _items
        # set to None if deployed_at (nullable) is None
        # and __fields_set__ contains the field
        if self.deployed_at is None and "deployed_at" in self.__fields_set__:
            _dict['deployedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Function:
        """Create an instance of Function from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Function.parse_obj(obj)

        _obj = Function.parse_obj({
            "id": obj.get("id"),
            "resource_type": obj.get("resourceType"),
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "code": obj.get("code"),
            "deployed_at": obj.get("deployedAt"),
            "settings": [FunctionSettingV1.from_dict(_item) for _item in obj.get("settings")] if obj.get("settings") is not None else None,
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "logo_url": obj.get("logoUrl"),
            "preview_webhook_url": obj.get("previewWebhookUrl"),
            "batch_max_count": obj.get("batchMaxCount"),
            "catalog_id": obj.get("catalogId"),
            "is_latest_version": obj.get("isLatestVersion")
        })
        return _obj


