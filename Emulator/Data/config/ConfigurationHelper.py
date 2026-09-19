import os

class ConfigurationHelper:
    def __init__(self):
        self.logger_level = os.getenv("LOGGER", "INFO")
        self.message_interval = int(os.getenv("MESSAGE_INTERVAL"))
        self.broker_address = os.getenv("BROKER_ADDRESS")
        self.client_id = os.getenv("CLIENT_ID")
        self.broker_port = int(os.getenv("BROKER_PORT"))
        self.topic = os.getenv("TOPIC")