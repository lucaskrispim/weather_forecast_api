Weather Forecast API

This Django-based API provides weather forecast data using the OpenWeatherMap API.
Setup
Prerequisites
  Python 3.x installed on your system.

Navigate to the project directory:

cd weather


Create and activate a virtual environment (optional but recommended):

  python -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate

Install dependencies:

  pip install -r requirements.txt

Configuration

  To use the project, you'll need to set up a .env file at the root of the project directory with the required API key.
    Create a .env file in the project root.
    Add your OpenWeatherMap API key to the .env file: API_KEY=your_api_key_here
    Replace your_api_key_here with your actual OpenWeatherMap API key.
    Save the changes.

Note: The .env file containing the API key should be in the same directory as the settings.py file of the project.

Usage
Making a POST Request

To retrieve weather forecast data, send a POST request to the /temperatures/ endpoint.
Request Format

Example using cURL:
  curl -X POST http://127.0.0.1:8000/temperatures/ \
  -H "Content-Type: application/json" \
  -d '{
        "lat": -21.7519891,
        "lon": -43.3469213
      }'

Request Body (Required Fields)

    lat (float): Latitude of the location.
    lon (float): Longitude of the location.

Response

The API returns weather forecast data for the specified location.
  Response example:
    {
	"content": [
		{
			"dia": "09/12/2023",
			"temperatura_celsius": 23.8
		},
		{
			"dia": "10/12/2023",
			"temperatura_celsius": 23.92
		},
		{
			"dia": "11/12/2023",
			"temperatura_celsius": 27.62
		},
		{
			"dia": "12/12/2023",
			"temperatura_celsius": 28.73
		},
		{
			"dia": "13/12/2023",
			"temperatura_celsius": 29.4
		},
		{
			"dia": "14/12/2023",
			"temperatura_celsius": 34.51
		},
		{
			"dia": "15/12/2023",
			"temperatura_celsius": 36.74
		},
		{
			"dia": "16/12/2023",
			"temperatura_celsius": 35.39
		}
	]
}
  
