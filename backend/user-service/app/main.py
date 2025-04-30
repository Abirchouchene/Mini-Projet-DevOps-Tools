from app import create_app
from app.kafka_consumer import start_kafka_consumer

app = create_app()

if __name__ == "__main__":
    start_kafka_consumer()
    app.run(host="0.0.0.0", port=5000)
