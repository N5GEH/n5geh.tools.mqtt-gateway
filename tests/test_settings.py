import logging
from typing import Optional
from dotenv import find_dotenv
from pydantic import AnyUrl, AnyHttpUrl, Field, BaseSettings



class TestSettings(BaseSettings):
    """

    """
    GATEWAY_URL: AnyHttpUrl = Field(default="http://localhost:8000",
                                    env=["GATEWAY_URL"])
    ORION_URL: AnyHttpUrl = Field(default="http://localhost:1026",
                                  env=["ORION_URL"])
    MQTT_HOST: str = Field(default="localhost",
                           env=["MQTT_HOST"])
    MQTT_PORT: int = Field(default="1883",
                           env=["MQTT_PORT"])
    FIWARE_SERVICE: str = Field(default="gateway_test",
                                env=["FIWARE_SERVICE"])
    FIWARE_SERVICEPATH: str = Field(default="/",
                                    env=["FIWARE_PATH",
                                         "FIWARE_SERVICEPATH",
                                         "FIWARE_SERVICE_PATH"])
    # Optional auth settings for protected Orion endpoints
    AUTH_ENABLED: bool = Field(default=False,
                               env=["AUTH_ENABLED"])
    AUTH_CLIENT_ID: Optional[str] = Field(default=None,
                                          env=["AUTH_CLIENT_ID"])
    AUTH_CLIENT_SECRET: Optional[str] = Field(default=None,
                                              env=["AUTH_CLIENT_SECRET"])
    AUTH_SERVER_URL: Optional[AnyHttpUrl] = Field(default=None,
                                                  env=["AUTH_SERVER_URL"])
    AUTH_REALM: Optional[str] = Field(default=None,
                                      env=["AUTH_REALM"])

    class Config:
        """
        Pydantic configuration
        """
        env_file = find_dotenv(".env")
        env_file_encoding = "utf-8"
        case_sensitive = False
        use_enum_values = True
        allow_reuse = True


def _settings_json(value: BaseSettings) -> str:
    if hasattr(value, "model_dump_json"):
        return value.model_dump_json(indent=2)
    return value.json(indent=2)


# create settings object
settings = TestSettings()
print(f"Running tests with the following settings: \n "
      f"{_settings_json(settings)}")
