from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.state_counters_response import StateCountersResponse
from ...types import Response


def _get_kwargs(
    fabric_id: str,
    device_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/fabrics/{fabric_id}/devices/{device_id}/counters",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, StateCountersResponse]]:
    if response.status_code == 200:
        response_200 = StateCountersResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CommonRestError.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = CommonRestError.from_dict(response.json())

        return response_409
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
) -> Response[Union[CommonRestError, StateCountersResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CommonRestError, StateCountersResponse]]:
    """Get the list of counters information of a specific device.

    Args:
        fabric_id (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, StateCountersResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CommonRestError, StateCountersResponse]]:
    """Get the list of counters information of a specific device.

    Args:
        fabric_id (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, StateCountersResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        device_id=device_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CommonRestError, StateCountersResponse]]:
    """Get the list of counters information of a specific device.

    Args:
        fabric_id (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, StateCountersResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CommonRestError, StateCountersResponse]]:
    """Get the list of counters information of a specific device.

    Args:
        fabric_id (str):
        device_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, StateCountersResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            device_id=device_id,
            client=client,
        )
    ).parsed
