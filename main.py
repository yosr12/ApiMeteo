import pandas as pd
import requests
from datetime import datetime, timedelta
import json
import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import lambda_handler

logger = Logger(service="local_test")
def get_weather_data(event, context):
    url = "https://api.open-meteo.com/v1/forecast"
    latitude = 52.52  # given latitude example
    longitude = 13.41  # given Longitude example
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
        weather_data = response.json()
        df = pd.DataFrame(weather_data["hourly"])
        csv_data = df.to_csv(index=False)

        # Upload CSV data to S3
        s3 = boto3.client('s3')
        bucket_name = 'your-bucket-name'
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
    return get_weather_data(event, context)

if __name__ == "__main__":
    event = {}
    context = {}
    handler(event, context)
