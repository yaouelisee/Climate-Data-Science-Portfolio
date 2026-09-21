class WeatherAnalyzer :
    def __init__(self,observations):
        self.observations = observations

    def temperature_stats(self):
        temperature = [self.observations[i][2] for i in range(len(self.observations))]
        max_temp = max(temperature)
        min_temp = min(temperature)
        temp_ave = sum(temperature)/len(temperature)
        return max_temp, min_temp, temp_ave
        
    def humididty_stats(self):
        humidity = [self.observations[i][3] for i in range(len(self.observations))]
        max_hum = max(humidity)
        min_hum = min(humidity)
        hum_ave = sum(humidity)/len(humidity)
        return max_hum, min_hum, hum_ave
        
    def rainfall_stats(self):
        rainfall =[self.rainfall[i][4] for i in range(len(self.observations))]
        max_rain = max(rainfall)
        min_rain = min(rainfall)
        rain_ave = sum(rainfall)/len(rainfall)
        return max_rain, min_rain , rain_ave 
    
    def wind_stats(self):
        wind_speed = [self.observations[i][5] for i in range(len(self.observations))]
        max_wind_speed = max(wind_speed)
        min_wind_speed = min(wind_speed)
        wind_speed_ave = sum(wind_speed)/wind_speed
        return max_wind_speed, min_wind_speed,wind_speed_ave
    
    def pressure_stats(self):
        pressure = [self.observations[i][6]for i in range(len(self.observations))]
        max_pressure = max(pressure)
        min_pressure = min(pressure)
        pressure_ave = sum(pressure)/len(pressure)
        return max_pressure, min_pressure, pressure_ave
    
    def station_analysis(self):
        stations = {}
        for observation in self.observations :
            station = observation.station 
            if station not in stations : 
                stations[station]=[]
                stations[station].append(observation)
        return stations
        
    def summary(self):
        return { "temperature": self.temperature_stats(),
                 "humidity": self.humididty_stats(),
                 "rainfall": self.rainfall_stats(),
                 "wind" : self.wind_stats(),
                 "pressure": self.pressure_stats(),
                 "stations": self.station_analysis()}
    
    

