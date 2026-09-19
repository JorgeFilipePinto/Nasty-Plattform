import logging

from Emulator.Data.EmulatorGenerator import EmulatorGenerator
from Emulator.Data.MQTT.MqttClient import MqttClient

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("Emulator")

if __name__ == "__main__":
    logger.info("Starting emulator...")
    mqtt_client = MqttClient(broker_address="broker.emqx.io", client_id="emulator", broker_port=1883)
    emulator = EmulatorGenerator(mqtt_client)
    emulator.start()
