import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"  
porta = 1883
topico_sub = "esp32/mottu/distancia"
topico_pub = "esp32/mottu/led"

def on_connect(client, userdata, flags, rc):
    print(f"Conectado com código de retorno: {rc}")
    client.subscribe(topico_sub)

def on_message(client, userdata, msg):
    print(f"[{msg.topic}] {msg.payload.decode()}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, porta, 60)

client.loop_forever()
