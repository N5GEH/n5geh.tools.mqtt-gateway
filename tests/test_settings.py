import logging
from dotenv import find_dotenv
from pydantic import AnyUrl, AnyHttpUrl, BaseSettings, Field, root_validator


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

    class Config:
        """
        Pydantic configuration
        """
        env_file = find_dotenv(".env")
        env_file_encoding = "utf-8"
        case_sensitive = False
        use_enum_values = True
        allow_reuse = True


# create settings object
settings = TestSettings()
print(f"Running tests with the following settings: \n "
      f"{settings.json(indent=2)}")

