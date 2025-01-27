# Weather Data Collection System

![Screenshot (137)](https://github.com/user-attachments/assets/b4ab58bb-8034-4250-8bca-4ee9ff2dcedd)

# Project Overview
This project is a Weather Data Collection System designed to demonstrate core DevOps principles by integrating the following:

* External API Integration: Fetches real-time weather data from the OpenWeather API.
  
* Cloud Storage: Stores data securely in AWS S3.
  
* Infrastructure as Code (IaC): Simplifies infrastructure management.
  
* Version Control: Ensures code reliability and collaboration using Git.
  
* Python Development: Implements functionality in Python.
  
* Error Handling: Provides robust exception handling to ensure smooth operations.
  
* Environment Management: Uses environment variables to securely manage sensitive data.

# Features
* Fetches real-time weather data for multiple cities.
* Automatically stores weather data in AWS S3.
* Supports tracking of multiple cities.
* Timestamps all data for historical tracking and analysis.

  ## Technical Architecture

- **Language**: Python 3.x  
- **Cloud Provider**: AWS (S3)  
- **External API**: OpenWeather API  

### Dependencies:
- **boto3**: AWS SDK for Python, used to interact with AWS services (e.g., S3).  
- **python-dotenv**: For managing environment variables securely.  
- **requests**: For making HTTP requests to the OpenWeather API.  

