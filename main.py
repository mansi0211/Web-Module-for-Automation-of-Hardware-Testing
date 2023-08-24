import paho.mqtt.client as mqtt_client

broker = '13.234.33.107'
port = 1883
topic = "mobilogix/echo"
topic_sub = "mobilogix/#"
# generate client ID with pub prefix randomly
client_id = '133787288368388'
username = 'device-6'
password = 'autogrid'
deviceId = "860181068953519"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
        res = str(msg.payload.decode())
        print(res)
        res1 = res.split(",")
        res2 = tuple(map(str, res1))
        #print(res2)
        did = res2[0]
        deviceid = (did[1:])
        print("Device id is:"+deviceid)
        for i in range(3):
            if float(res2[i+1]) < 1.0:
                print("device at rest")
            else:
                if 0.0 < float(res2[i]) < 1.0:
                    print("incorrect values")
                else:
                    print("Current External Voltage:"+res2[1])
                if 3.0 < float(res2[i]) < 4.0:
                    print("Device's Internal Voltage is:"+res2[2])
                else:
                    print("Current Internal Voltage:"+res2[2])




    #  y = json.loads(msg.payload.decode())
    # temp = y["notification"]["parameters"]["temp"]
    # hum = y["notification"]["parameters"]["humi"]
    # print("temperature: ",temp,", humidity:",hum)

    client.subscribe(topic_sub)
    client.on_message = on_message


def main():
    client = connect_mqtt()
    subscribe(client)

    client.loop_forever()


if __name__ == '__main__':
    main()
