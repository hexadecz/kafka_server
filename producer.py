from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    message = input("Enter message to send: ")
    producer.send('test-topic', message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)
