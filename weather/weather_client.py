from dequest import sync_client, QueryParameter, HttpMethod

from weather.dtos import WeatherDTO


class WeatherClient:

    @classmethod
    @sync_client(
        dto_class=WeatherDTO,
        url="https://api.open-meteo.com/v1/forecast?daily=rain_sum,temperature_2m_max,temperature_2m_min",
        method= HttpMethod.GET,
    )
    def get_weather(
            cls, 
            latitude: QueryParameter,
            longitude: QueryParameter,
            forecast_days: QueryParameter
            ):
        pass