import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsMetadata")


@_attrs_define
class ModelsMetadata:
    """Metadata defines metadata of all objects in the service.

    Attributes:
        created_at (Union[Unset, datetime.datetime]): Object creation timestamp.
        created_by (Union[Unset, str]): UserId of the user who created the object.
        modified_at (Union[Unset, datetime.datetime]): Last object modification timestamp.
        modified_by (Union[Unset, str]): UserId of the user who modified the object.
        revision_id (Union[Unset, str]): The revision identifier.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    modified_by: Union[Unset, str] = UNSET
    revision_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by

        revision_id = self.revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("createdBy", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        modified_by = d.pop("modifiedBy", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        models_metadata = cls(
            created_at=created_at,
            created_by=created_by,
            modified_at=modified_at,
            modified_by=modified_by,
            revision_id=revision_id,
        )

        models_metadata.additional_properties = d
        return models_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
