import logging
import paho.mqtt.client as mqtt

from Emulator.Data.config import ConfigurationHelper

logger = logging.getLogger(__name__)


class MqttClient:
    def __init__(self, config: ConfigurationHelper):
        self.broker_address = config.broker_address
        self.broker_port = config.broker_port
        self.client_id = config.client_id
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.client_id)
        self.connect()
        self.subscribe(config.topic)

    def connect(self):
        """
            Connect to the MQTT broker.
        """
        logger.info("Connecting to broker %s:%s", self.broker_address, self.broker_port)
        self.client.connect(self.broker_address, self.broker_port)

    def publish(self, topic, payload):
        """
            Publish a message to a topic on the MQTT broker.
        """
        self.client.publish(topic, payload)

    def subscribe(self, topic):
        """
            Subscribe to a topic on the MQTT broker.
        """
        logger.debug("Subscribing to topic %s", topic)
        self.client.subscribe(topic)

    def set_on_message_callback(self, callback):
        """
            Set the callback function to be called when a message is received.
        """
        self.client.on_message = callback

    def loop_start(self):
        """
            Start the MQTT client loop in a separate thread.
        """
        self.client.loop_start()

    def loop_stop(self):
        """
            Stop the MQTT client loop and disconnect from the broker.
        """
        self.client.loop_stop()
