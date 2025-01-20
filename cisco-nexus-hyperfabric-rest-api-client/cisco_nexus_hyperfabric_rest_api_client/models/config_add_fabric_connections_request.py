from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_port_connection import ModelsPortConnection


T = TypeVar("T", bound="ConfigAddFabricConnectionsRequest")


@_attrs_define
class ConfigAddFabricConnectionsRequest:
    """Add one or more connections to a specific fabric.

    Attributes:
        connections (Union[Unset, list['ModelsPortConnection']]): The connections for the fabric.
        fabric_id (Union[Unset, str]): The fabric id or name.
    """

    connections: Union[Unset, list["ModelsPortConnection"]] = UNSET
    fabric_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        fabric_id = self.fabric_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connections is not UNSET:
            field_dict["connections"] = connections
        if fabric_id is not UNSET:
            field_dict["fabricId"] = fabric_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.models_port_connection import ModelsPortConnection

        d = src_dict.copy()
        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in _connections or []:
            connections_item = ModelsPortConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        fabric_id = d.pop("fabricId", UNSET)

        config_add_fabric_connections_request = cls(
            connections=connections,
            fabric_id=fabric_id,
        )

        config_add_fabric_connections_request.additional_properties = d
        return config_add_fabric_connections_request

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
