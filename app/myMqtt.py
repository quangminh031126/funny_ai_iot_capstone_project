import os
import random
import time

from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client

load_dotenv()


host = os.getenv("MQTT_HOST")
port = int(os.getenv("MQTT_PORT"))
username = os.getenv("ADAFRUIT_USER")
password = os.getenv("ADAFRUIT_KEY")

topic_head = f"{username}/feeds/"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client_id = f"python-mqtt-{random.randint(0, 1000)}"

    client = mqtt_client.Client(
        client_id=client_id,
        callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2,
    )
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(host, port)
    return client


def test_publish(client):
    topic = f"{username}/feeds/bbc_led"
    msg_count = 1
    while True:
        time.sleep(1)
        msg = msg_count
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    test_publish(client)
    client.loop_stop()


if __name__ == "__main__":
    run()
