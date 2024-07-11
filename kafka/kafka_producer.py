import uuid
from confluent_kafka import Producer

class KafkaProducer:
    def __init__(self, bootstrap_servers='localhost:19092', client_id='python-producer'):
        self.conf = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': client_id
        }
        self.producer = Producer(**self.conf)
        self.topic = 'mytelemetry.udp.message.created'

    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Error al enviar el mensaje: {err}')
        else:
            print(f'Mensaje enviado a {msg.topic()} [{msg.partition()}]')

    def produce(self, message):
        self.producer.produce(self.topic, key=str(uuid.uuid1()), value=message, callback=self.delivery_report)
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()

    def close(self):
        self.flush()
        self.producer = None

