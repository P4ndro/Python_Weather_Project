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


