from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

topic = 'temperature'

temperature_data = [22.4, 23.1, 21.8, 22.9, 23.5, 24.0, 22.7, 23.3, 22.1, 23.8]

while True:
    for i in range(10):
        message = {'id': i,
                'temperature': random.choice(temperature_data)
                }

        producer.send(topic, value=message)
        print(f'Sent: {message}')
        time.sleep(1)

    producer.flush()

    time.sleep(5)  # Wait for 5 seconds before sending the next batch of messages