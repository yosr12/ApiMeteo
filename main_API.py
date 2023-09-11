import pandas as pd
import requests
from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create a FastAPI instance
app = FastAPI()

"""
This code is using the Server
"""
# To run the server, use the following command:
# uvicorn main:app

# Define a GET endpoint for retrieving weather data
@app.get("/weather_data")
def get_weather_data():
    # Open-Meteo API URL
    url = "https://api.open-meteo.com/v1/forecast"

    # Replace with the desired latitude and longitude coordinates
    latitude = 52.52
    longitude = 13.41

    # Calculate date range (2 days before today to 2 days ahead)
    today = datetime.now().date()
    start_date = today - timedelta(days=2)
    end_date = start_date + timedelta(days=2)

    # Define request parameters
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "relativehumidity_2m,temperature_2m,snowfall,snow_depth,cloudcover,direct_radiation,diffuse_radiation,rain"
    }

    # Send a GET request to the Open-Meteo API
    response = requests.get(url, params=params)

    # Check if the API response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response from the API
        weather_data = response.json()

        # Create a DataFrame from the "hourly" data
        df = pd.DataFrame(weather_data["hourly"])

        # Save the weather data as a CSV file (optional)
        df.to_csv('weather_data.csv', index=False)

        # Log a success message
        print("Weather data saved successfully.")

        # Return the weather data as a JSON response
        return JSONResponse(content=weather_data, status_code=200)
    else:
        # Log an error message if the API request fails
        print("Error occurred:", response.status_code)

        # Return an error response
        return JSONResponse(content={"message": f"Error occurred: {response.status_code}"}, status_code=response.status_code)

# Entry point for the FastAPI application
if __name__ == "__main__":

    # Call the FastAPI handler function
    handler(event, context)
