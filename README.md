#  Weather Streaming with Kafka and Streamlit

This project streams real-time weather data for **Cairo** using **Kafka** and displays it through a **Streamlit** web interface.

##  How It Works

- `producer1.py`: Fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/) and sends it to a Kafka topic.
- `consumer1.py`: Consumes the data from the Kafka topic and optionally stores it or forwards it.
- `weather_app.py`: Displays the received weather data ( temperature, humidity, description) using Streamlit.

##  Weather Target
City: **Cairo, Egypt**

## Technologies
- Python
- Kafka (`kafka-python`)
- Streamlit
- OpenWeatherMap API
- Requests

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-streamlit-kafka.git
cd weather-streamlit-kafka
```

### 2. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Kafka Server

Make sure you have Apache Kafka and Zookeeper running locally or on your server.

### 4. Start the Producer

```bash
python producer1.py
```

### 5. Start the Consumer

```bash
python consumer1.py
```

### 6. Launch the Streamlit App

```bash
streamlit run weather_app.py
```

##  Notes
- Replace `"your_api_key_here"` in `producer.py` with your actual OpenWeatherMap API key.
- The producer fetches weather data every 30 seconds using time.sleep(30).
- The Streamlit app automatically refreshes every 5 seconds using st.experimental_rerun() with time.sleep(5) or a refresh timer.
- Ensure Kafka is running and the topic (e.g., `weather_topic`) is created.
## 📸 Streamlit App Preview
![image](https://github.com/user-attachments/assets/145f3af6-f7df-4ccf-b792-71e66f642990)




```

## 🧾 License

This project is for educational purposes and is open-source.
