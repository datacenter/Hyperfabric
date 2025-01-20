from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.config_add_management_ports_request import ConfigAddManagementPortsRequest
from ...models.config_management_ports_response import ConfigManagementPortsResponse
from ...types import Response


def _get_kwargs(
    fabric_id: str,
    node_id: str,
    *,
    body: ConfigAddManagementPortsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/fabrics/{fabric_id}/nodes/{node_id}/managementPorts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ConfigManagementPortsResponse]]:
    if response.status_code == 200:
        response_200 = ConfigManagementPortsResponse.from_dict(response.json())

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
) -> Response[Union[CommonRestError, ConfigManagementPortsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: ConfigAddManagementPortsRequest,
) -> Response[Union[CommonRestError, ConfigManagementPortsResponse]]:
    """Add one or more management ports configuration to a specific node in a fabric.

    Args:
        fabric_id (str):
        node_id (str):
        body (ConfigAddManagementPortsRequest): Description not available

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigManagementPortsResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        node_id=node_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: ConfigAddManagementPortsRequest,
) -> Optional[Union[CommonRestError, ConfigManagementPortsResponse]]:
    """Add one or more management ports configuration to a specific node in a fabric.

    Args:
        fabric_id (str):
        node_id (str):
        body (ConfigAddManagementPortsRequest): Description not available

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigManagementPortsResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        node_id=node_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: ConfigAddManagementPortsRequest,
) -> Response[Union[CommonRestError, ConfigManagementPortsResponse]]:
    """Add one or more management ports configuration to a specific node in a fabric.

    Args:
        fabric_id (str):
        node_id (str):
        body (ConfigAddManagementPortsRequest): Description not available

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ConfigManagementPortsResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        node_id=node_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: ConfigAddManagementPortsRequest,
) -> Optional[Union[CommonRestError, ConfigManagementPortsResponse]]:
    """Add one or more management ports configuration to a specific node in a fabric.

    Args:
        fabric_id (str):
        node_id (str):
        body (ConfigAddManagementPortsRequest): Description not available

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ConfigManagementPortsResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
