import s3fs
import pandas as pd
from kafka import KafkaProducer
import json

# AWS S3 and Kafka configuration
s3_bucket = 'stock-data5051'
s3_key = 'ADANIPORTS.csv'
kafka_bootstrap_servers = ['localhost:9092']
kafka_topic = 'stock-topic'  # Replace with your actual Kafka topic

try:
    # Initialize S3 filesystem
    fs = s3fs.S3FileSystem()

    # Initialize Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=kafka_bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Read CSV file from S3
    with fs.open(f's3://{s3_bucket}/{s3_key}', 'r') as f:
        df = pd.read_csv(f)

    # Iterate over rows and send each row to Kafka
    for index, row in df.iterrows():
        # Convert row to dictionary
        data = row.to_dict()
        # Send data to Kafka
        producer.send(kafka_topic, value=data)
        # Optional: Flush to ensure data is sent
        producer.flush()

    print("Data sent to Kafka successfully.")
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the producer
    producer.close()