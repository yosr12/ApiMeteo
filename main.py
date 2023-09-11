import pandas as pd
import requests
from datetime import datetime, timedelta
import json
import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import lambda_handler

# Initialize the AWS Lambda Powertools logger
logger = Logger(service="local_test")

def get_weather_data(event, context):
    """
    Retrieves weather data from the Open-Meteo API and stores it in an AWS S3 bucket.

    Args:
        event: AWS Lambda event data.
        context: AWS Lambda context.

    Returns:
        dict: A dictionary containing the HTTP response status and a message.
    """
    
    # Open-Meteo API URL
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Specify the latitude and longitude of the location for weather data retrieval
    latitude = 52.52  # Replace with the desired latitude
    longitude = 13.41  # Replace with the desired longitude
    
    # Calculate date range for weather forecast
    today = datetime.now().date()
    start_date = today - timedelta(days=2)
    end_date = start_date + timedelta(days=2)
    
    # Define API request parameters
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

    if response.status_code == 200:
        # Parse the API response as JSON
        weather_data = response.json()
        
        # Convert the JSON data to a Pandas DataFrame
        df = pd.DataFrame(weather_data["hourly"])
        
        csv_data = df.to_csv(index=False)

        #  CSV  to an S3 bucket
        s3 = boto3.client('s3')
        bucket_name = 'your_bucket_name'  # Replace with the name of your S3 bucket
        s3.put_object(Body=csv_data, Bucket=bucket_name, Key='weather_data.csv')

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Weather data saved successfully.'})
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps({'message': f'Error occurred: {response.status_code}'})
        }

@lambda_handler
def handler(event, context):
    """
    Lambda function handler.

"""
    return get_weather_data(event, context)

if __name__ == "__main__":
    # For local testing purposes, simulate an event and context
    event = {}
    context = {}
    handler(event, context)
