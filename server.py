from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve



app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather')
def weather():
    city = request.args.get("city")
    if not bool(city.strip()):
        city = "New York"
        print("No city name provided. Defaulting to New York.")

    weather_data = get_weather(city)
    if not weather_data:
        return render_template(
            "weather.html",
            title="Error",
            status="City not found or API error.",
            temp="N/A",
            feels_like="N/A",
            
        )

    
    if "main" not in weather_data or "weather" not in weather_data:
        return render_template(
            "weather.html",
            title="Error",
            status="City not found or API error.",
            temp="N/A",
            feels_like="N/A",
        )
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f'{weather_data["main"]["temp"]:.1f}',
        feels_like=f'{weather_data["main"]["feels_like"]:.1f}',
    )

if __name__ == "__main__":
    serve(app,host="0.0.0.0", port=8000)
