import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemaAssertConfigBgpPeerEstablishedData")


@_attrs_define
class SchemaAssertConfigBgpPeerEstablishedData:
    """Description not available

    Attributes:
        fabric_id (Union[Unset, str]): Description not available
        generation_id (Union[Unset, str]): Description not available
        implicit (Union[Unset, bool]): Description not available
        latch_time (Union[Unset, str]): Description not available
        latched_at (Union[Unset, datetime.datetime]): Description not available
        org_id (Union[Unset, str]): Description not available
        peer_ip (Union[Unset, str]): Description not available
        peer_remote_as (Union[Unset, int]): Description not available
        vrf_name (Union[Unset, str]): Description not available
    """

    fabric_id: Union[Unset, str] = UNSET
    generation_id: Union[Unset, str] = UNSET
    implicit: Union[Unset, bool] = UNSET
    latch_time: Union[Unset, str] = UNSET
    latched_at: Union[Unset, datetime.datetime] = UNSET
    org_id: Union[Unset, str] = UNSET
    peer_ip: Union[Unset, str] = UNSET
    peer_remote_as: Union[Unset, int] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fabric_id = self.fabric_id

        generation_id = self.generation_id

        implicit = self.implicit

        latch_time = self.latch_time

        latched_at: Union[Unset, str] = UNSET
        if not isinstance(self.latched_at, Unset):
            latched_at = self.latched_at.isoformat()

        org_id = self.org_id

        peer_ip = self.peer_ip

        peer_remote_as = self.peer_remote_as

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id
        if generation_id is not UNSET:
            field_dict["generationId"] = generation_id
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if latch_time is not UNSET:
            field_dict["latchTime"] = latch_time
        if latched_at is not UNSET:
            field_dict["latchedAt"] = latched_at
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if peer_ip is not UNSET:
            field_dict["peerIp"] = peer_ip
        if peer_remote_as is not UNSET:
            field_dict["peerRemoteAs"] = peer_remote_as
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        fabric_id = d.pop("fabricId", UNSET)

        generation_id = d.pop("generationId", UNSET)

        implicit = d.pop("implicit", UNSET)

        latch_time = d.pop("latchTime", UNSET)

        _latched_at = d.pop("latchedAt", UNSET)
        latched_at: Union[Unset, datetime.datetime]
        if isinstance(_latched_at, Unset):
            latched_at = UNSET
        else:
            latched_at = isoparse(_latched_at)

        org_id = d.pop("orgId", UNSET)

        peer_ip = d.pop("peerIp", UNSET)

        peer_remote_as = d.pop("peerRemoteAs", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        schema_assert_config_bgp_peer_established_data = cls(
            fabric_id=fabric_id,
            generation_id=generation_id,
            implicit=implicit,
            latch_time=latch_time,
            latched_at=latched_at,
            org_id=org_id,
            peer_ip=peer_ip,
            peer_remote_as=peer_remote_as,
            vrf_name=vrf_name,
        )

        schema_assert_config_bgp_peer_established_data.additional_properties = d
        return schema_assert_config_bgp_peer_established_data

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
