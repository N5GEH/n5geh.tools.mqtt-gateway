from typing import Union
from dotenv import find_dotenv
from pydantic import AliasChoices, AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict



class TestSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(".env"),
        env_file_encoding="utf-8",
        use_enum_values=True,
        extra = "ignore"
    )

    GATEWAY_URL: AnyHttpUrl = "http://localhost:8000"
    ORION_URL: AnyHttpUrl = "http://localhost:1026"
    MQTT_HOST: str = "localhost"
    MQTT_PORT: int = 1883
    FIWARE_SERVICE: str = "gateway_test"
    FIWARE_SERVICEPATH: str = Field(
        default="/",
        validation_alias=AliasChoices(
            "FIWARE_PATH",
            "FIWARE_SERVICEPATH",
            "FIWARE_SERVICE_PATH",
        ),
    )
    # Optional auth settings for protected Orion endpoints
    AUTH_ENABLED: bool = False
    AUTH_CLIENT_ID: Union[str, None] = None
    AUTH_CLIENT_SECRET: Union[str, None] = None
    AUTH_SERVER_URL: Union[str, None] = None
    AUTH_REALM: Union[str, None] = None


def _settings_json(value: BaseSettings) -> str:
    return value.model_dump_json(indent=2)


# create settings object
settings = TestSettings()
print(f"Running tests with the following settings: \n "
      f"{_settings_json(settings)}")
