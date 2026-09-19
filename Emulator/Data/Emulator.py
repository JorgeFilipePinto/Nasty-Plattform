import random
from time import time
from MQTT.MqttClient import MqttClient
from models.SensorData import SensorData
import json


class Emulator:
    def __init__(self, mqtt_client: MqttClient):
        self.mqtt_client = mqtt_client

    def start(self):
        _timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - random.randint(0, 10000)))
        message = SensorData(
            sensor_timestamp=_timestamp,
            sensor_id="sensor_123",
            sensor_value=random.uniform(20.0, 30.0)
        )

        json_format = json.dumps(message.to_dict())
        self.mqtt_client.publish("nasty", json_format)

