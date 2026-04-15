import pytest
from unittest.mock import patch, MagicMock
from weather_service import get_weather

def test_get_weather_success():
    dummy_data = {"temp": 22, "condition": "Cloudy"}
    with patch("weather_service.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = dummy_data
        mock_get.return_value = mock_response

        result = get_weather("madrid")
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/madrid")
        assert result == dummy_data

def test_get_weather_url_called():
    with patch("weather_service.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"dummy": True}
        mock_get.return_value = mock_response

        get_weather("paris")
        mock_get.assert_called_once_with("https://api.weather.com/v3/weather/paris")

def test_get_weather_handles_exception():
    with patch("weather_service.requests.get", side_effect=Exception("Network error")):
        with pytest.raises(Exception):
            get_weather("tokyo")
