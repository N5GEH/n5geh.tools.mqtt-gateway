from typing import Optional, Union
from dotenv import find_dotenv
from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=find_dotenv(".env"),
                                      env_file_encoding="utf-8",
                                      case_sensitive=False,
                                      use_enum_values=True)
    GATEWAY_URL: AnyHttpUrl = Field(default="http://localhost:8000",
                             alias="GATEWAY_URL")
    ORION_URL: AnyHttpUrl = Field(default="http://localhost:1026",
                                  alias="ORION_URL")
    MQTT_HOST: str = Field(default="localhost",
                           alias="MQTT_HOST")
    MQTT_PORT: int = Field(default="1883",
                           alias="MQTT_PORT")
    FIWARE_SERVICE: str = Field(default="gateway_test",
                                alias="FIWARE_SERVICE")
    FIWARE_SERVICEPATH: str = Field(default="/",
                                    alias="FIWARE_SERVICEPATH")
    # Optional auth settings for protected Orion endpoints
    AUTH_ENABLED: bool = Field(default=False,)
    AUTH_CLIENT_ID: Optional[Union[str, None]] = Field(default=None,)
    AUTH_CLIENT_SECRET: Optional[Union[str, None]] = Field(default=None)
    AUTH_SERVER_URL: Optional[Union[AnyHttpUrl, None]] = Field(default=None)
    AUTH_REALM: Optional[Union[str, None]] = Field(default=None)


# create settings object
settings = TestSettings()
print(f"Running tests with the following settings: \n "
      f"{settings.model_dump_json(indent=2)}")
