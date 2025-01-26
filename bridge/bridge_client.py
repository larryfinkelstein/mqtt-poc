import paho.mqtt.client as mqtt

LOCAL_BROKER = "localhost"
LOCAL_PORT = 1883
CENTRAL_BROKER = "centralized-mqtt-broker"
CENTRAL_PORT = 1884


# Callback when a message is received from the local broker
def on_local_message(client, userdata, msg):
    print(f"Local message received: {msg.topic} {msg.payload}")
    central_client.publish(msg.topic, msg.payload)


# Callback when a message is received from the central broker
def on_central_message(client, userdata, msg):
    print(f"Central message received: {msg.topic} {msg.payload}")
    local_client.publish(msg.topic, msg.payload)


# Local MQTT client
local_client = mqtt.Client()
local_client.on_message = on_local_message
local_client.connect(LOCAL_BROKER, LOCAL_PORT, 60)
local_client.subscribe("#")

# Central MQTT client
central_client = mqtt.Client()
central_client.on_message = on_central_message
central_client.connect(CENTRAL_BROKER, CENTRAL_PORT, 60)
central_client.subscribe("#")

# Start the loop for both clients
local_client.loop_start()
central_client.loop_start()

# Keep the script running
while True:
    pass