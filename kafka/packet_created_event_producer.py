import uuid
from confluent_kafka import Producer
from kafka.message.packet_send import PacketSend

class PacketCreatedEventProducer:
    def __init__(self, bootstrap_servers='localhost:19092', client_id='python-producer'):
        self.conf = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': client_id
        }
        self.producer = Producer(**self.conf)
        self.topic = 'mytelemetry.udp.packet.created'

    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Error when sending message: {err}')
        else:
            print(f'Message sended to {msg.topic()} [{msg.partition()}]')

    def produce(self, detected_packet):
        packet = PacketSend(detected_packet)
        self.producer.produce(self.topic, key=str(uuid.uuid1()), value=packet.to_json(), callback=self.delivery_report)
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()

    def close(self):
        self.flush()
        self.producer = None

