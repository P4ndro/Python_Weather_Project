# Weather Flask App

A simple Flask-based web application that fetches and displays current weather data for a given city, using the OpenWeatherMap API and served with Waitress.

## Features

- Enter any city name and retrieve:
  - Current temperature (°C)
  - “Feels like” temperature (°C)
  - Weather description (e.g. “Light rain”)
- Defaults to **New York** if no city is provided or lookup fails.
- Clean, minimal frontend with reusable templates.
- Production-ready WSGI server via **Waitress**.

## Demo

1. Start the app (see [Usage](#usage)).  
2. Open your browser at `http://localhost:8000/`.  
3. Enter a city (e.g. “London”) and submit.  
4. View current weather data.

## Getting Started

### Prerequisites

- Python 3.9+  
- An [OpenWeatherMap API Key](https://openweathermap.org/api)  
- (Optional) Git

### Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/P4ndro/weather-flask-app.git
   cd weather-flask-app

   python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

pip install -r requirements.txt


weather-flask-app/
├── .env
├── app.py
├── weather.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── weather.html
└── static/
    └── css/
        └── style.css




blinker==1.9.0
certifi==2025.4.26
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
Flask==3.1.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
python-dotenv==1.1.0
requests==2.32.3
urllib3==2.4.0
Werkzeug==3.1.3
waitress==2.1.2        # (implicit dependency via pip install waitress)




