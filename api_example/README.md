# Weather Forecast API

Проект для получения прогноза погоды в Москве на 14 дней с использованием API Open-Meteo.

## Описание

Этот проект использует [Open-Meteo API](https://open-meteo.com/) для получения метеорологических данных:
- Минимальная и максимальная температура (°C)
- Скорость ветра (км/ч)
- Вероятность выпадения осадков (%)

## Ссылка на API
https://api.open-meteo.com/v1/forecast

## Скрипт
import pandas as pd
import openmeteo_requests
from datetime import datetime

#обращаемся к сервису
openmeteo = openmeteo_requests.Client()
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 59.9386,
	"longitude": 30.3141,
	"daily": ["temperature_2m_max", "temperature_2m_min", "wind_speed_10m_max", "precipitation_probability_max"],
	"timezone": "Europe/Moscow",
	"forecast_days": 14,
	"wind_speed_unit": "ms"
}
responses = openmeteo.weather_api(url, params=params)

#информация о месте
response = responses[0]
print(f"Координаты: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Зона времени: {response.Timezone()}{response.TimezoneAbbreviation()}")

#сбор ежедневных данных о погоде
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(2).ValuesAsNumpy()
daily_precipitation_probability_max = daily.Variables(3).ValuesAsNumpy()

#генерируем колонку с датами
daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}

#собираем данные в массивы
daily_data["Макс. температура, C"] = daily_temperature_2m_max
daily_data["Мин. температура, C"] = daily_temperature_2m_min
daily_data["Макс. скорость ветра, C"] = daily_wind_speed_10m_max
daily_data["Макс. вероятность выпадения осадков, %"] = daily_precipitation_probability_max

#собираем даннные в один датафрейм
daily_dataframe = pd.DataFrame(data = daily_data)
print("\nDaily data\n", daily_dataframe)

## Скриншот вывода
<img width="1386" height="433" alt="image" src="https://github.com/user-attachments/assets/0be5e10d-3542-4326-9784-d03ac7110d83" />
