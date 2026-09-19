import logging

from Emulator.Data.EmulatorGenerator import EmulatorGenerator
from Emulator.Data.MQTT.MqttClient import MqttClient
from Emulator.Data.config import ConfigurationHelper

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("Emulator")
config = ConfigurationHelper()

if __name__ == "__main__":
    logger.info("Starting emulator...")
    mqtt_client = MqttClient(config)
    emulator = EmulatorGenerator(mqtt_client)
    emulator.start()
