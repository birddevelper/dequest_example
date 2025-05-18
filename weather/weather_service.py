from dequest import async_client, sync_client, QueryParameter, HttpMethod

from weather.dtos import WeatherDTO


async def async_weather_callback(dto):
    # Handle the response here
    # For example, you can emit a signal or log the data
    # For demonstration, let's just print the data  to the console
    print("Async weather data:", dto.timezone, dto.daily["rain_sum"])


class WeatherClient:

    @classmethod
    @sync_client(
        dto_class=WeatherDTO,
        url="https://fakestoreapi.com/products/{product_id}",
        method=HttpMethod.GET,
    )
    def get_weather_sync(
        cls,
        latitude: QueryParameter,
        longitude: QueryParameter,
        forecast_days: QueryParameter,
    ):
        """
        Get weather data synchronously.
        This function retrieves weather data from the API and returns it as a WeatherDTO object.
        """

    @classmethod
    @async_client(
        dto_class=WeatherDTO,
        url="https://api.open-meteo.com/v1/forecast",
        method=HttpMethod.GET,
        callback=async_weather_callback,
    )
    def get_weather_async(
        cls,
        latitude: QueryParameter,
        longitude: QueryParameter,
        forecast_days: QueryParameter,
        daily: QueryParameter = "rain_sum",
    ):
        """
        Get weather data asynchronously.
        This function retrieves weather data from the API and returns it as a WeatherDTO object.
        """
