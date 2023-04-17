from pydantic import BaseModel, Field
from filip.models.ngsi_v2.iot import DeviceAttribute
from typing import Optional, List


class Topic(BaseModel):
    """
    A specific MQTT topic to be converted into FIWARE topic
    """
    attributes: List[DeviceAttribute] = Field(
        description="The list of all received attributes under this MQTT topic",
        default=[]
    )

    topic_name: str = Field(
        description="The MQTT topic of this converter"
    )


