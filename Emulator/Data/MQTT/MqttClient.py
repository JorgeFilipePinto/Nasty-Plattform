import paho.mqtt.client as mqtt

class MqttClient:
    def __init__(self, broker_address, client_id, broker_port=1883):
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.client_id = client_id
        self.client = mqtt.Client(client_id)
        self.connect()
        self.subscribe("nasty")

    def connect(self):
        self.client.connect(self.broker_address, self.broker_port)

    def publish(self, topic, payload):
        self.client.publish(topic, payload)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def set_on_message_callback(self, callback):
        self.client.on_message = callback

    def loop_start(self):
        self.client.loop_start()

    def loop_stop(self):
        self.client.loop_stop()