from Emulator.Data.EmulatorGenerator import EmulatorGenerator
from Emulator.Data.MQTT.MqttClient import MqttClient


if __name__ == "__main__":
    mqtt_client = MqttClient(broker_address="broker.emqx.io", client_id="emulator", broker_port=1883)
    emulator = EmulatorGenerator(mqtt_client)
    emulator.start()
