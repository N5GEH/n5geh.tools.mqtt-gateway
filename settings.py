from pydantic import root_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    ORION_URL: str = "http://orion:1026"
    MQTT_HOST: str = "test.mosquitto.org"
    MQTT_PORT: int = 1883
    MQTT_USER: Optional[str] = None
    MQTT_PASSWORD: Optional[str] = None
    MQTT_TLS: Optional[bool] = False
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "iot_devices"
    REDIS_URL: str = "redis://localhost:6379"
    FIWARE_SERVICE: str = "gateway_test"
    FIWARE_SERVICEPATH: str = "/"
    # Get log level from environment variable, default to INFO if not set
    LOG_LEVEL: str = 'INFO'  # 'critical', 'error', 'warning', 'info', 'debug'
    model_config = SettingsConfigDict(env_file=".env")

    @root_validator(pre=True)
    def validate_mqtt_credentials(cls, values):
        if values.get("MQTT_TLS") and (
                not values.get("MQTT_USER") or not values.get("MQTT_PASSWORD")):
            raise ValueError(
                "MQTT_USER and MQTT_PASSWORD must be set if MQTT_TLS is enabled.")
        return values


# Create an instance of the settings
settings = Settings()
