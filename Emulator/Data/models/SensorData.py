

class SensorData:
    def __init__(self, sensor_id: str, sensor_timestamp: str, sensor_value: float):
        self.sensor_id = sensor_id
        self.sensor_timestamp = sensor_timestamp
        self.sensor_value = sensor_value

    def to_dict(self):
        return {
            "sensor_id": self.sensor_id,
            "sensor_timestamp": self.sensor_timestamp,
            "sensor_value": self.sensor_value
        }