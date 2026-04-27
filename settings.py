from typing import Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    ORION_URL: str = "http://orion:1026"
    MQTT_HOST: str = "test.mosquitto.org"
    MQTT_PORT: int = 1883
    MQTT_USER: Union[str, None] = None
    MQTT_PASSWORD: Union[str, None] = None
    MQTT_TLS: bool = False
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "iot_devices"
    REDIS_URL: str = "redis://localhost:6379"
    FIWARE_SERVICE: str = "gateway_test"
    FIWARE_SERVICEPATH: str = "/"
    # Optional auth settings for Orion access
    AUTH_ENABLED: bool = False
    AUTH_CLIENT_ID: Union[str, None] = None
    AUTH_CLIENT_SECRET: Union[str, None] = None
    AUTH_SERVER_URL: Union[str, None] = None
    AUTH_REALM: Union[str, None] = None
    # Get log level from environment variable, default to INFO if not set
    LOG_LEVEL: str = 'INFO'  # 'critical', 'error', 'warning', 'info', 'debug'


# Create an instance of the settings
settings = Settings()
