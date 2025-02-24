import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        self.s3 = boto3.client('s3')


    def create_bucket_if_not_exists(self):
        try:
            self.s3.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} already exists")
            return
        
        except:
            print(f"Creating bucket {self.bucket_name}")
        
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"The bucket {self.bucket_name} created successfully.")
        
        except Exception as e:
            print(f"Error creating the bucket : {e}")
    

    def fetch_weather(self,city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q' : city,
            'appid' : self.api_key,
            'units' : 'imperial'
        }

        try:
            response = requests.get(base_url,params=params)
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data : {e}")
            return None
        
    def save_to_s3(self,weather_data,city):
        if not weather_data:
            return False
        
        timestamp = datetime.now().strftime('%Y%m%d--%H%M%S')
        file_name = f"weather-data/{city}--{timestamp}.json"

        try:
            weather_data['timestamp'] = timestamp
            self.s3.put_object(
                Bucket = self.bucket_name,
                Key = file_name,
                Body = json.dumps(weather_data),
                ContentType = 'application/json'
            )
            print(f'Successfully saved data for {city} to S3')
            return True
        
        except Exception as e:
            print(f"Error saving to S3 : {e}")
            return False
        
def main():
    dashboard = WeatherDashboard()

    dashboard.create_bucket_if_not_exists()

    cities = ["New Delhi","Kurnool","Sankri","Kolkata"]

    for city in cities:
        print(f"\nFetching weather for {city}")
        weather_data = dashboard.fetch_weather(city)
        if weather_data:
            success = dashboard.save_to_s3(weather_data,city)

            if success:
                print(f"Weather data for {city} saved to S3!")
            else:
                print("Error saving to S3")
        else:
            print(f"Failed to fetch weather data for {city}")


if __name__ == "__main__":
    main()
