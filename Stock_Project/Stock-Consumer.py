from kafka import KafkaConsumer
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Kafka Consumer Configuration
kafka_bootstrap_servers = ['localhost:9092']
kafka_topic = 'stock-topic'  # Use the same topic as the producer

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    consumer_timeout_ms=10000  # Adjust based on your use case
)

# Initialize a list to hold data points
data_points = []

# Function to update the plot
def update(frame):
    global data_points
    # Consume a message from Kafka
    for message in consumer:
        data = message.value
        data_points.append(data)
        
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(data_points)
        
        # Clear the previous plot
        plt.cla()
        
        # Plot the data (adjust columns as per your CSV structure)
        plt.plot(df.Date, df['Close'], marker='o')
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.title('Real-Time Data Visualization')
        
        # Break after consuming one message to update the plot
        break

# Set up Matplotlib plot
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000)  # Update every 1000 ms (1 second)

# Show the plot
plt.show()

# Close the Kafka consumer when done
consumer.close()