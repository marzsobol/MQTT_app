import paho.mqtt.client as mqtt
import time
import random

# Don't forget to change the variables for the MQTT broker!
mqtt_username = "username"
mqtt_password = "catato"
mqtt_topic = "test"
mqtt_broker_ip = "xx.xx.xx.xx" #tozmienic:



class MQTTClient:
# These functions handle what happens when the MQTT client connects
# to the broker, and what happens then the topic receives a message
    def __init__(self):
        self.message_received = ""
        self.topic_received = "answer/group/1"
        self.client = mqtt.Client("numbersetting")
        # Set the username and password for the MQTT client
        self.client.username_pw_set(mqtt_username, mqtt_password)
        self.client.on_message = self.on_message
        print("Connection:")
        self.client.connect(mqtt_broker_ip, 1883) #mqtt_broker_id #port 1883

    def on_message(self, client, userdata, message):
        self.topic_received = message.topic
        self.message_received = str(message.payload.decode("utf-8"))


    def on_connect(self, userdata, flags, rc):
        print("Connected!", str(rc))
        self.client.subscribe(mqtt_topic)

    def mqtt_subscribe(self,topic):
        self.client.subscribe(topic) #subscribe one topic

    def mqtt_publish(self,topic, data):
        self.client.publish(topic, data) #publish on topic

    def mqtt_loop_forever(self):
        self.client.loop_forever()

    def mqtt_disconnect(self):
        self.client.disconnect()

