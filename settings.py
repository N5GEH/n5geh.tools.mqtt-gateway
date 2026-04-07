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
    # Optional auth settings for Orion access
    AUTH_ENABLED: bool = False
    AUTH_TENANT: str = None
    AUTH_CLIENT_ID: str = None
    AUTH_CLIENT_SECRET: str = None
    AUTH_SERVER_URL: str = None
    AUTH_REALM: str = None
    # Get log level from environment variable, default to INFO if not set
    LOG_LEVEL: str = 'INFO'  # 'critical', 'error', 'warning', 'info', 'debug'

    class Config:
        env_file = ".env"


# Create an instance of the settings
settings = Settings()
