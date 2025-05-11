import streamlit as st
from kafka import KafkaConsumer
import json
import time
from datetime import datetime

# Configuration - Update these if different in your setup
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'weather-topic'

def get_weather_data():
    """Fetch latest message from Kafka"""
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=[KAFKA_SERVER],
            auto_offset_reset='latest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            consumer_timeout_ms=2000
        )
        for msg in consumer:
            return msg.value
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
    return None

def main():
    st.title("Cairo Weather Monitor")
    
    # Initialize session state
    if 'last_data' not in st.session_state:
        st.session_state.last_data = None
    if 'last_update' not in st.session_state:
        st.session_state.last_update = "Never"

    # Fetch new data
    new_data = get_weather_data()
    if new_data:
        st.session_state.last_data = new_data
        st.session_state.last_update = datetime.now().strftime("%H:%M:%S")

    # Display data - MATCHING YOUR CONSUMER OUTPUT
    data = st.session_state.last_data
    if data:
        st.subheader(f" {data.get('name', 'Cairo')}")
        
        # Main metrics (matches your consumer printout)
        col1, col2 = st.columns(2)
        with col1:
            st.metric(" Temperature", f"{data['main']['temp']}°C")
            st.metric(" Humidity", f"{data['main']['humidity']}%")
        
        with col2:
            st.metric("Conditions", data['weather'][0]['description'].capitalize())
            st.metric(" Last Update", st.session_state.last_update)
        
        # Raw data for debugging
        with st.expander("View Raw Data"):
            st.json(data)
    else:
        st.warning("Waiting for data...")
        st.write("Make sure:")
        st.write("1. Kafka is running")
        st.write("2. Producer is sending data")
        st.write(f"3. Topic name is '{TOPIC_NAME}'")

    # Auto-refresh every 5 seconds
    time.sleep(5)
    st.experimental_rerun()

if __name__ == "__main__":
    main()