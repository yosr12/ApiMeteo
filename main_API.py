import pandas as pd
import requests
from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()


# uvicorn main:app to run this code then open the postman to test the server

@app.get("/weather_data")
def get_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"
    latitude = 52.52  # Replace with the desired latitude
    longitude = 13.41  # Replace with the desired longitude
    today = datetime.now().date()
    start_date = today - timedelta(days=2)
    end_date = start_date + timedelta(days=2)
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "relativehumidity_2m,temperature_2m,snowfall,snow_depth,cloudcover,direct_radiation,diffuse_radiation,rain"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()        
        weather_data = response.json()
        df = pd.DataFrame(weather_data["hourly"])
        # Save DataFrame as CSV file
        df.to_csv('weather_data.csv', index=False)
        
        print("Weather data saved successfully.")
    else:
        print("Error occurred:", response.status_code)

