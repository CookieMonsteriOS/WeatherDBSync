# Weather DB Sync

The Weather DB Sync project is a Flask-based API that integrates with the OpenWeather API to retrieve and store weather data for different locations. It also provides an endpoint to calculate the average weather for a specific location within a given date range.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone 
    ```

2. Navigate to the project directory:

    ```bash
    cd weather-db-sync
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

### Endpoints

#### 1. /weather

- **Method:** GET
- **Description:** Retrieves and stores weather data for a specified location.
- **Parameters:**
    - `lat` (float): Latitude of the location.
    - `lon` (float): Longitude of the location.
    - `city` (string): Name of the city.
- **Response:** JSON object containing the weather data.

#### 2. /weather/average/<int:location_id>

- **Method:** GET
- **Description:** Calculates the average weather for a specific location within a given date range.
- **Parameters:**
    - `location_id` (int): ID of the location.
    - `start_date` (string): Start date of the date range (format: YYYY-MM-DD HH:MM:SS).
    - `end_date` (string): End date of the date range (format: YYYY-MM-DD HH:MM:SS).
- **Response:** JSON object containing the average weather temp and humidity, and other metrics for the location.
- ```sh
curl -X GET "http://127.0.0.1:5000/weather/average/1?start_date=2024-04-15%2017:11:41&end_date=2024-04-15%2017:27:51"

**Note:** Historical weather data is not available due to limitations with the OpenWeather API. The /weather/average endpoint calculates the average weather based on the available data.

## Contributing

Contributions to the Weather DB Sync project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
