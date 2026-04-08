import logging
import time
from typing import Dict, Optional

import aiohttp

from settings import settings

_cached_token: Optional[str] = None
_cached_token_expiry: float = 0.0


def _auth_is_enabled() -> bool:
    return bool(settings.AUTH_ENABLED)


def _token_is_valid() -> bool:
    return _cached_token is not None and time.time() < _cached_token_expiry


def _require_auth_config() -> None:
    missing = [
        name
        for name, value in [
            ("AUTH_SERVER_URL", settings.AUTH_SERVER_URL),
            ("AUTH_REALM", settings.AUTH_REALM),
            ("AUTH_CLIENT_ID", settings.AUTH_CLIENT_ID),
            ("AUTH_CLIENT_SECRET", settings.AUTH_CLIENT_SECRET),
        ]
        if not value
    ]
    if missing:
        raise RuntimeError(
            f"Auth is enabled but missing settings: {', '.join(missing)}"
        )


async def _fetch_token(session: aiohttp.ClientSession) -> str:
    _require_auth_config()
    token_url = (
        f"{settings.AUTH_SERVER_URL.rstrip('/')}/realms/"
        f"{settings.AUTH_REALM}/protocol/openid-connect/token"
    )
    data = {
        "grant_type": "client_credentials",
        "client_id": settings.AUTH_CLIENT_ID,
        "client_secret": settings.AUTH_CLIENT_SECRET,
    }
    async with session.post(token_url, data=data) as response:
        if response.status != 200:
            error_text = await response.text()
            raise RuntimeError(
                f"Auth token request failed ({response.status}): {error_text}"
            )
        payload = await response.json()

    token = payload.get("access_token")
    if not token:
        raise RuntimeError("Auth token response missing access_token")

    expires_in = payload.get("expires_in", 60)
    try:
        expires_in = int(expires_in)
    except (TypeError, ValueError):
        expires_in = 60

    global _cached_token, _cached_token_expiry
    _cached_token = token
    _cached_token_expiry = time.time() + max(expires_in - 30, 0)
    return token


async def get_bearer_token(session: aiohttp.ClientSession) -> Optional[str]:
    if not _auth_is_enabled():
        return None

    if _token_is_valid():
        return _cached_token

    try:
        return await _fetch_token(session)
    except Exception as exc:
        logging.error(f"Failed to fetch auth token: {exc}")
        raise


def _resolve_service(fiware_service: Optional[str]) -> str:
    return fiware_service or settings.FIWARE_SERVICE


async def build_orion_headers(
    session: aiohttp.ClientSession,
    fiware_service: Optional[str] = None,
) -> Dict[str, str]:
    headers = {
        "Fiware-Service": _resolve_service(fiware_service),
        "Fiware-ServicePath": settings.FIWARE_SERVICEPATH,
    }
    token = await get_bearer_token(session)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

