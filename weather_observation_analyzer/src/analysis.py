class WeatherAnalyzer:

    def __init__(self, observations):
        self.observations = observations

    def temperature_stats(self):
        temperature = [
            observation.temperature
            for observation in self.observations
        ]

        max_temperature = max(temperature)
        min_temperature = min(temperature)
        temperature_ave = sum(temperature) / len(temperature)

        return max_temperature, min_temperature, temperature_ave

    def humidity_stats(self):
        humidity = [
            observation.humidity
            for observation in self.observations
        ]

        max_humidity = max(humidity)
        min_humidity = min(humidity)
        humidity_ave = sum(humidity) / len(humidity)

        return max_humidity, min_humidity, humidity_ave

    def rainfall_stats(self):
        rainfall = [
            observation.rainfall
            for observation in self.observations
        ]

        max_rain = max(rainfall)
        min_rain = min(rainfall)
        rain_ave = sum(rainfall) / len(rainfall)

        return max_rain, min_rain, rain_ave

    def wind_stats(self):
        wind_speed = [
            observation.wind_speed
            for observation in self.observations
        ]

        max_wind_speed = max(wind_speed)
        min_wind_speed = min(wind_speed)
        wind_speed_ave = sum(wind_speed) / len(wind_speed)

        return max_wind_speed, min_wind_speed, wind_speed_ave

    def pressure_stats(self):
        pressure = [
            observation.pressure
            for observation in self.observations
        ]

        max_pressure = max(pressure)
        min_pressure = min(pressure)
        pressure_ave = sum(pressure) / len(pressure)

        return max_pressure, min_pressure, pressure_ave

    def station_analysis(self):
        stations = {}

        for observation in self.observations:
            station = observation.station

            if station not in stations:
                stations[station] = []

            stations[station].append(observation)

        return stations

    def summary(self):
        return {
            "temperature": self.temperature_stats(),
            "humidity": self.humidity_stats(),
            "rainfall": self.rainfall_stats(),
            "wind": self.wind_stats(),
            "pressure": self.pressure_stats(),
            "stations": self.station_analysis()
        }
    