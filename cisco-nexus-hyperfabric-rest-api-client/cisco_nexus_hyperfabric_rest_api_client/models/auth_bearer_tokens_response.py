from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_bearer_token import AuthBearerToken


T = TypeVar("T", bound="AuthBearerTokensResponse")


@_attrs_define
class AuthBearerTokensResponse:
    """Returns a list of bearer tokens.

    Attributes:
        tokens (Union[Unset, list['AuthBearerToken']]): A list of bearer tokens.
    """

    tokens: Union[Unset, list["AuthBearerToken"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokens: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = []
            for tokens_item_data in self.tokens:
                tokens_item = tokens_item_data.to_dict()
                tokens.append(tokens_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.auth_bearer_token import AuthBearerToken

        d = src_dict.copy()
        tokens = []
        _tokens = d.pop("tokens", UNSET)
        for tokens_item_data in _tokens or []:
            tokens_item = AuthBearerToken.from_dict(tokens_item_data)

            tokens.append(tokens_item)

        auth_bearer_tokens_response = cls(
            tokens=tokens,
        )

        auth_bearer_tokens_response.additional_properties = d
        return auth_bearer_tokens_response

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
