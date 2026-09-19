import logging
import random
import time
from Emulator.Data.MQTT.MqttClient import MqttClient
from Emulator.Data.models.SensorData import SensorData
import json

logger = logging.getLogger(__name__)


class EmulatorGenerator:
    def __init__(self, mqtt_client: MqttClient):
        self.mqtt_client = mqtt_client

    def start(self):
        logger.debug("EmulatorGenerator loop started")
        while True:
            self._create_and_publish_sensor_data()
            time.sleep(1)

    def _create_and_publish_sensor_data(self):
        _timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - random.randint(0, 10000)))
        message = SensorData(
            sensor_timestamp=_timestamp,
            sensor_id="sensor_123",
            sensor_value=random.uniform(20.0, 30.0)
        )

        json_format = json.dumps(message.to_dict())
        self.mqtt_client.publish("nasty", json_format)
        logger.debug("Published sensor data: %s", json_format)
