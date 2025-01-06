from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.config_fabric_connections_response import ConfigFabricConnectionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fabric_id: str,
    *,
    candidate: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["candidate"] = candidate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/fabrics/{fabric_id}/connections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ConfigFabricConnectionsResponse]]:
    if response.status_code == 200:
        response_200 = ConfigFabricConnectionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ConfigFabricConnectionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
) -> Response[Union[CommonRestError, ConfigFabricConnectionsResponse]]:
    """Get the list of connections configuration information in a specific fabric.

    Args:
        fabric_id (str):
        candidate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigFabricConnectionsResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        candidate=candidate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
) -> Optional[Union[CommonRestError, ConfigFabricConnectionsResponse]]:
    """Get the list of connections configuration information in a specific fabric.

    Args:
        fabric_id (str):
        candidate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigFabricConnectionsResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        client=client,
        candidate=candidate,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
) -> Response[Union[CommonRestError, ConfigFabricConnectionsResponse]]:
    """Get the list of connections configuration information in a specific fabric.

    Args:
        fabric_id (str):
        candidate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigFabricConnectionsResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        candidate=candidate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    *,
    client: AuthenticatedClient,
    candidate: Union[Unset, str] = UNSET,
) -> Optional[Union[CommonRestError, ConfigFabricConnectionsResponse]]:
    """Get the list of connections configuration information in a specific fabric.

    Args:
        fabric_id (str):
        candidate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigFabricConnectionsResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            client=client,
            candidate=candidate,
        )
    ).parsed
