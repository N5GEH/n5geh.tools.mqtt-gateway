from pydantic import BaseSettings


class Settings(BaseSettings):
    ORION_URL: str = "http://orion:1026"
    MQTT_HOST: str = "test.mosquitto.org"
    MQTT_PORT: int = 1883
    MQTT_USER: str = None
    MQTT_PASSWORD: str = None
    MQTT_TLS: bool = False
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "admin"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "iot_devices"
    REDIS_URL: str = "redis://localhost:6379"
    FIWARE_SERVICE: str = "gateway_test"
    FIWARE_SERVICEPATH: str = "/"
    # Get log level from environment variable, default to INFO if not set
    LOG_LEVEL: str = 'INFO'

    class Config:
        env_file = ".env"


# Create an instance of the settings
settings = Settings()
