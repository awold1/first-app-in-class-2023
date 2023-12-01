from app.weather_report import display_forecast

def test_display_forecast():

    assert display_forecast("06510") == 200

