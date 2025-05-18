from django.shortcuts import render
from django.http import JsonResponse
from .weather_client import WeatherClient
import json
from django.core import serializers

def index(request):
        weather_dto = WeatherClient.get_weather(
            latitude=35.6895,
            longitude=139.6917,
            forecast_days=2
        )
        return JsonResponse({
            'message': 'Hello, world! This is the weather app.',
            'weather': weather_dto.to_json()
        })