from dataclasses import dataclass,  asdict
import json


@dataclass
class WeatherDTO:
    latitude: float
    longitude: float
    timezone: str
    timezone_abbreviation: str
    daily: dict

    def to_json(self):
        return asdict(self)
    
    def __str__(self):
        return json.dumps(self.to_json(), indent=4)