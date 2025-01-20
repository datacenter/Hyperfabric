from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_network_port import ModelsNetworkPort


T = TypeVar("T", bound="ConfigPortsResponse")


@_attrs_define
class ConfigPortsResponse:
    """Description not available

    Attributes:
        node_id (Union[Unset, str]): Description not available
        ports (Union[Unset, list['ModelsNetworkPort']]): Description not available
    """

    node_id: Union[Unset, str] = UNSET
    ports: Union[Unset, list["ModelsNetworkPort"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.models_network_port import ModelsNetworkPort

        d = src_dict.copy()
        node_id = d.pop("nodeId", UNSET)

        ports = []
        _ports = d.pop("ports", UNSET)
        for ports_item_data in _ports or []:
            ports_item = ModelsNetworkPort.from_dict(ports_item_data)

            ports.append(ports_item)

        config_ports_response = cls(
            node_id=node_id,
            ports=ports,
        )

        config_ports_response.additional_properties = d
        return config_ports_response

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
