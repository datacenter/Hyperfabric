import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_path_path_id import SchemaPathPathId


T = TypeVar("T", bound="SchemaVlanCounters")


@_attrs_define
class SchemaVlanCounters:
    """Description not available

    Attributes:
        bytes_in (Union[Unset, int]): Description not available
        bytes_out (Union[Unset, int]): Description not available
        collected_at (Union[Unset, datetime.datetime]): Description not available
        err_in (Union[Unset, int]): Description not available
        err_out (Union[Unset, int]): Description not available
        err_pkts_in (Union[Unset, int]): Description not available
        err_pkts_out (Union[Unset, int]): Description not available
        id (Union[Unset, SchemaPathPathId]): PathId identifies the specific "schema coordinates" identifier of an object
            in the schema tree.
        pkts_in (Union[Unset, int]): Description not available
        pkts_out (Union[Unset, int]): Description not available
    """

    bytes_in: Union[Unset, int] = UNSET
    bytes_out: Union[Unset, int] = UNSET
    collected_at: Union[Unset, datetime.datetime] = UNSET
    err_in: Union[Unset, int] = UNSET
    err_out: Union[Unset, int] = UNSET
    err_pkts_in: Union[Unset, int] = UNSET
    err_pkts_out: Union[Unset, int] = UNSET
    id: Union[Unset, "SchemaPathPathId"] = UNSET
    pkts_in: Union[Unset, int] = UNSET
    pkts_out: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_in = self.bytes_in

        bytes_out = self.bytes_out

        collected_at: Union[Unset, str] = UNSET
        if not isinstance(self.collected_at, Unset):
            collected_at = self.collected_at.isoformat()

        err_in = self.err_in

        err_out = self.err_out

        err_pkts_in = self.err_pkts_in

        err_pkts_out = self.err_pkts_out

        id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        pkts_in = self.pkts_in

        pkts_out = self.pkts_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_in is not UNSET:
            field_dict["bytesIn"] = bytes_in
        if bytes_out is not UNSET:
            field_dict["bytesOut"] = bytes_out
        if collected_at is not UNSET:
            field_dict["collectedAt"] = collected_at
        if err_in is not UNSET:
            field_dict["errIn"] = err_in
        if err_out is not UNSET:
            field_dict["errOut"] = err_out
        if err_pkts_in is not UNSET:
            field_dict["errPktsIn"] = err_pkts_in
        if err_pkts_out is not UNSET:
            field_dict["errPktsOut"] = err_pkts_out
        if id is not UNSET:
            field_dict["id"] = id
        if pkts_in is not UNSET:
            field_dict["pktsIn"] = pkts_in
        if pkts_out is not UNSET:
            field_dict["pktsOut"] = pkts_out

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.schema_path_path_id import SchemaPathPathId

        d = src_dict.copy()
        bytes_in = d.pop("bytesIn", UNSET)

        bytes_out = d.pop("bytesOut", UNSET)

        _collected_at = d.pop("collectedAt", UNSET)
        collected_at: Union[Unset, datetime.datetime]
        if isinstance(_collected_at, Unset):
            collected_at = UNSET
        else:
            collected_at = isoparse(_collected_at)

        err_in = d.pop("errIn", UNSET)

        err_out = d.pop("errOut", UNSET)

        err_pkts_in = d.pop("errPktsIn", UNSET)

        err_pkts_out = d.pop("errPktsOut", UNSET)

        _id = d.pop("id", UNSET)
        id: Union[Unset, SchemaPathPathId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = SchemaPathPathId.from_dict(_id)

        pkts_in = d.pop("pktsIn", UNSET)

        pkts_out = d.pop("pktsOut", UNSET)

        schema_vlan_counters = cls(
            bytes_in=bytes_in,
            bytes_out=bytes_out,
            collected_at=collected_at,
            err_in=err_in,
            err_out=err_out,
            err_pkts_in=err_pkts_in,
            err_pkts_out=err_pkts_out,
            id=id,
            pkts_in=pkts_in,
            pkts_out=pkts_out,
        )

        schema_vlan_counters.additional_properties = d
        return schema_vlan_counters

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
