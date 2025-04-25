from kafka import KafkaProducer
import json

KAFKA_SERVER = "kafka:9092"
KAFKA_TOPIC = "reservations"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_reservation_message(reservation):
    message = {
        "reservation_id": reservation.id,
        "user_id": reservation.user_id,
        "salle_id": reservation.salle_id,
        "status": reservation.status
    }
    producer.send(KAFKA_TOPIC, message)