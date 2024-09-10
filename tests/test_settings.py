import logging
from dotenv import find_dotenv
from pydantic import AnyUrl, AnyHttpUrl, Field, root_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestSettings(BaseSettings):
    """

    """
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
    model_config = SettingsConfigDict(env_file=find_dotenv(".env"), env_file_encoding="utf-8", case_sensitive=False, use_enum_values=True, allow_reuse=True)


# create settings object
settings = TestSettings()
print(f"Running tests with the following settings: \n "
      f"{settings.json(indent=2)}")

