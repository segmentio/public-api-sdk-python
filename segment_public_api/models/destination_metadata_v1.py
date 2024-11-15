# coding: utf-8

"""
    Segment Public API

    The Segment Public API helps you manage your Segment Workspaces and its resources. You can use the API to perform CRUD (create, read, update, delete) operations at no extra charge. This includes working with resources such as Sources, Destinations, Warehouses, Tracking Plans, and the Segment Destinations and Sources Catalogs.  All CRUD endpoints in the API follow REST conventions and use standard HTTP methods. Different URL endpoints represent different resources in a Workspace.  See the next sections for more information on how to use the Segment Public API. 

    The version of the OpenAPI document: 57.0.1
    Contact: friends@segment.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from segment_public_api.models.contact import Contact
from segment_public_api.models.destination_metadata_action_v1 import DestinationMetadataActionV1
from segment_public_api.models.destination_metadata_component_v1 import DestinationMetadataComponentV1
from segment_public_api.models.destination_metadata_features_v1 import DestinationMetadataFeaturesV1
from segment_public_api.models.destination_metadata_methods_v1 import DestinationMetadataMethodsV1
from segment_public_api.models.destination_metadata_platforms_v1 import DestinationMetadataPlatformsV1
from segment_public_api.models.destination_metadata_subscription_preset_v1 import DestinationMetadataSubscriptionPresetV1
from segment_public_api.models.integration_option_beta import IntegrationOptionBeta
from segment_public_api.models.logos_beta import LogosBeta

class DestinationMetadataV1(BaseModel):
    """
    Represents a Destination within Segment.  A Destination is a target for Segment to forward data to, and represents a tool or storage Destination.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The id of the Destination metadata.  Config API note: analogous to `name`.")
    name: StrictStr = Field(..., description="The user-friendly name of the Destination.  Config API note: equal to `displayName`.")
    description: StrictStr = Field(..., description="The description of the Destination.")
    slug: StrictStr = Field(..., description="The slug used to identify the Destination in the Segment app.")
    logos: LogosBeta = Field(...)
    options: conlist(IntegrationOptionBeta) = Field(..., description="Options configured for the Destination.")
    status: StrictStr = Field(..., description="Support status of the Destination.")
    previous_names: conlist(StrictStr) = Field(..., alias="previousNames", description="A list of names previously used by the Destination.")
    categories: conlist(StrictStr) = Field(..., description="A list of categories with which the Destination is associated.")
    website: StrictStr = Field(..., description="A website URL for this Destination.")
    components: conlist(DestinationMetadataComponentV1) = Field(..., description="A list of components this Destination provides.")
    supported_features: DestinationMetadataFeaturesV1 = Field(..., alias="supportedFeatures")
    supported_methods: DestinationMetadataMethodsV1 = Field(..., alias="supportedMethods")
    supported_platforms: DestinationMetadataPlatformsV1 = Field(..., alias="supportedPlatforms")
    actions: conlist(DestinationMetadataActionV1) = Field(..., description="Actions available for the Destination.")
    presets: conlist(DestinationMetadataSubscriptionPresetV1) = Field(..., description="Predefined Destination subscriptions that can optionally be applied when connecting a new instance of the Destination.")
    contacts: Optional[conlist(Contact)] = Field(None, description="Contact info for Integration Owners.")
    partner_owned: Optional[StrictBool] = Field(None, alias="partnerOwned", description="Partner Owned flag.")
    supported_regions: Optional[conlist(StrictStr)] = Field(None, alias="supportedRegions", description="A list of supported regions for this Destination.")
    region_endpoints: Optional[conlist(StrictStr)] = Field(None, alias="regionEndpoints", description="The list of regional endpoints for this Destination.")
    multi_instance_supported_version: Optional[StrictStr] = Field(None, alias="multiInstanceSupportedVersion", description="This Destination's support for multiple instance types.")
    __properties = ["id", "name", "description", "slug", "logos", "options", "status", "previousNames", "categories", "website", "components", "supportedFeatures", "supportedMethods", "supportedPlatforms", "actions", "presets", "contacts", "partnerOwned", "supportedRegions", "regionEndpoints", "multiInstanceSupportedVersion"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DEPRECATED', 'PRIVATE_BETA', 'PRIVATE_BUILDING', 'PRIVATE_SUBMITTED', 'PUBLIC', 'PUBLIC_BETA', 'UNAVAILABLE'):
            raise ValueError("must be one of enum values ('DEPRECATED', 'PRIVATE_BETA', 'PRIVATE_BUILDING', 'PRIVATE_SUBMITTED', 'PUBLIC', 'PUBLIC_BETA', 'UNAVAILABLE')")
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
    def from_json(cls, json_str: str) -> DestinationMetadataV1:
        """Create an instance of DestinationMetadataV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of logos
        if self.logos:
            _dict['logos'] = self.logos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item in self.options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['options'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item in self.components:
                if _item:
                    _items.append(_item.to_dict())
            _dict['components'] = _items
        # override the default output from pydantic by calling `to_dict()` of supported_features
        if self.supported_features:
            _dict['supportedFeatures'] = self.supported_features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supported_methods
        if self.supported_methods:
            _dict['supportedMethods'] = self.supported_methods.to_dict()
        # override the default output from pydantic by calling `to_dict()` of supported_platforms
        if self.supported_platforms:
            _dict['supportedPlatforms'] = self.supported_platforms.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in presets (list)
        _items = []
        if self.presets:
            for _item in self.presets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['presets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in contacts (list)
        _items = []
        if self.contacts:
            for _item in self.contacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contacts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationMetadataV1:
        """Create an instance of DestinationMetadataV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DestinationMetadataV1.parse_obj(obj)

        _obj = DestinationMetadataV1.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "slug": obj.get("slug"),
            "logos": LogosBeta.from_dict(obj.get("logos")) if obj.get("logos") is not None else None,
            "options": [IntegrationOptionBeta.from_dict(_item) for _item in obj.get("options")] if obj.get("options") is not None else None,
            "status": obj.get("status"),
            "previous_names": obj.get("previousNames"),
            "categories": obj.get("categories"),
            "website": obj.get("website"),
            "components": [DestinationMetadataComponentV1.from_dict(_item) for _item in obj.get("components")] if obj.get("components") is not None else None,
            "supported_features": DestinationMetadataFeaturesV1.from_dict(obj.get("supportedFeatures")) if obj.get("supportedFeatures") is not None else None,
            "supported_methods": DestinationMetadataMethodsV1.from_dict(obj.get("supportedMethods")) if obj.get("supportedMethods") is not None else None,
            "supported_platforms": DestinationMetadataPlatformsV1.from_dict(obj.get("supportedPlatforms")) if obj.get("supportedPlatforms") is not None else None,
            "actions": [DestinationMetadataActionV1.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "presets": [DestinationMetadataSubscriptionPresetV1.from_dict(_item) for _item in obj.get("presets")] if obj.get("presets") is not None else None,
            "contacts": [Contact.from_dict(_item) for _item in obj.get("contacts")] if obj.get("contacts") is not None else None,
            "partner_owned": obj.get("partnerOwned"),
            "supported_regions": obj.get("supportedRegions"),
            "region_endpoints": obj.get("regionEndpoints"),
            "multi_instance_supported_version": obj.get("multiInstanceSupportedVersion")
        })
        return _obj


