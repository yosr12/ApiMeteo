
Weather Data Retrieval with AWS Cloud and Serverless FastAPI

This project demonstrates two implementations for retrieving weather data from the Open-Meteo API and saving the responses. One implementation is designed for AWS Lambda, while the other is a Serverless FastAPI application. Both implementations are serverless and can be hosted on AWS Cloud resources.


AWS Lambda Implementation

#Description
The AWS Lambda implementation uses Python to retrieve weather data from the Open-Meteo API and store it in an AWS S3 bucket. It leverages the aws_lambda_powertools library for simplified logging.

Implementation Steps
Initialize Environment: Configure the necessary environment for AWS Lambda, including AWS S3 access.

Get Weather Data: Utilize the Open-Meteo API to fetch weather data based on specified latitude and longitude coordinates. The code retrieves data for a 3-day period, starting from 2 days before the current date.

Data Processing: Parse the API response, convert it into a Pandas DataFrame, and store it as a CSV file.

Upload to S3: Upload the CSV data to an AWS S3 bucket, making it accessible for later use.

Usage
Deploy the AWS Lambda function on AWS and configure event triggers if necessary.

Run the Lambda function, which will fetch and store weather data in the specified S3 bucket.

Access the weather data stored in the S3 bucket.

Serverless FastAPI Implementation.
Description
The Serverless FastAPI implementation uses FastAPI, a modern Python web framework, to create a serverless API for retrieving weather data from the Open-Meteo API. It provides an HTTP GET endpoint for accessing weather information.

Implementation Steps
Initialize FastAPI: Create a FastAPI instance to serve as the serverless web application.

API Endpoint: Define a GET endpoint /weather_data to retrieve weather data.

Get Weather Data: Use Python and the Open-Meteo API to fetch weather data based on specified latitude and longitude coordinates, similar to the Lambda implementation.

Data Processing: Parse the API response, convert it into a Pandas DataFrame (optional), and log the result.

Response: Return the weather data as a JSON response.

Usage
Deploy the FastAPI application to a serverless platform or host it as needed.

Access the /weather_data endpoint using an HTTP GET request.

Receive weather data as a JSON response.

Dependencies
Both implementations rely on the following Python dependencies:

pandas for data manipulation and CSV processing.
requests for making HTTP requests to the Open-Meteo API.
boto3 for AWS S3 integration in the Lambda implementation.
aws_lambda_powertools for simplified logging in the Lambda implementation.
fastapi and uvicorn for creating and running the FastAPI application.
Getting Started
Clone this repository to your local environment.

Install the required Python packages using pip install -r requirements.txt.

Deploy the AWS Lambda function and/or FastAPI application as needed.

Access weather data by invoking the Lambda function or making HTTP GET requests to the FastAPI endpoint.







