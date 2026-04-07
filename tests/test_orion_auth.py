import pytest
import requests

from test_settings import settings


def _missing_auth_settings():
    missing = []
    if not settings.AUTH_SERVER_URL:
        missing.append("AUTH_SERVER_URL")
    if not settings.AUTH_REALM:
        missing.append("AUTH_REALM")
    if not settings.AUTH_CLIENT_ID:
        missing.append("AUTH_CLIENT_ID")
    if not settings.AUTH_CLIENT_SECRET:
        missing.append("AUTH_CLIENT_SECRET")
    return missing


def _get_access_token():
    token_url = (
        f"{settings.AUTH_SERVER_URL.rstrip('/')}/realms/"
        f"{settings.AUTH_REALM}/protocol/openid-connect/token"
    )
    payload = {
        "grant_type": "client_credentials",
        "client_id": settings.AUTH_CLIENT_ID,
        "client_secret": settings.AUTH_CLIENT_SECRET,
    }
    response = requests.post(token_url, data=payload, timeout=15)
    response.raise_for_status()
    data = response.json()
    token = data.get("access_token")
    if not token:
        raise RuntimeError("No access_token in token response")
    return token


def test_orion_version_with_auth():
    if not settings.AUTH_ENABLED:
        pytest.skip("Auth disabled. Set AUTH_ENABLED=true to run this test.")

    missing = _missing_auth_settings()
    if missing:
        pytest.skip(f"Missing auth settings: {', '.join(missing)}")

    token = _get_access_token()
    service = settings.FIWARE_SERVICE
    headers = {
        "Authorization": f"Bearer {token}",
        "Fiware-Service": service,
        "Fiware-ServicePath": settings.FIWARE_SERVICEPATH,
        "Accept": "application/json",
    }
    response = requests.get(
        f"{settings.ORION_URL.rstrip('/')}/version",
        headers=headers,
        timeout=15,
    )
    assert response.status_code == 200, (
        f"Unexpected status {response.status_code}: {response.text}"
    )

