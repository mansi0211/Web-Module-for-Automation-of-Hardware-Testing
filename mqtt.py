from paho.mqtt import client as mqtt_client

broker = '13.234.33.107'
port = 1883
topic = "mobilogix/#"
topic_sub = "mobilogix/#"
# generate client ID with pub prefix randomly
client_id = '133787288368388'
username = 'device-6'
password = 'autogrid'
deviceId = "860181068953519"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)


    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, status):
    msg = '$860181068953519,0.55,3.34,200523,153510.00,1,18.495342,N,74.131390,E,0.000,88.66,0.02,x,x,L,297,*'
    result = client.publish(msg,topic)
    msg_status = result[0]
    if msg_status ==0:
        print(f"message : {msg} sent to topic {topic}")
    else:
        print(f"Failed to send message to topic {topic}")



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Recieved '{msg.payload.decode()}' from '{msg.topic}' topic")
        
        
        

myArray = np.array(msg.payload.decode())
print(myArray[1])
        
    client.subscribe(topic_sub)
    client.on_message = on_message

def main():
    client = connect_mqtt()
    subscribe(client)

    client.loop_forever()

if __name__ == '__main__':
    main()
