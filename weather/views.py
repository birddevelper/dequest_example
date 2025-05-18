from django.shortcuts import render
from django.http import JsonResponse
from .weather_service import WeatherClient
import json
from django.core import serializers

def sync_weather(request):
        weather_dto = WeatherClient.get_weather_sync(
            latitude=35.6895,
            longitude=139.6917,
            forecast_days=2
        )
        return JsonResponse({
            'message': 'Weather data retrieved successfully',
            'weather': weather_dto.to_json()
        })



def async_weather(request):
        WeatherClient.get_weather_async(
            latitude=35.6895,
            longitude=139.6917,
            forecast_days=2
        )
        return JsonResponse({
            'message': 'Request sent asynchronously. Check the console for the response.',
        })