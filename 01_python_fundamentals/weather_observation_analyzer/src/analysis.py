class WeatherAnalyzer :
    def __init__(self,observations):
        self.observations = observations

    def temperature_stats(self):
        temperatures = [self.observations[i][2] for i in range(len(self.observations))]
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        temp_ave = sum(temperatures)/len(temperatures)
        return max_temp, min_temp, temp_ave
        
    def humididty_stats(self):
        humidity = [self.observations[i][3] for i in range(len(self.observations))]
        max_hum = max(humidity)
        min_hum = min(humidity)
        hum_ave = sum(humidity)/len(humidity)
        return max_hum, min_hum, hum_ave
        
    def rainfall_stats(self):
        
        pass
    def wind_stats(self):
        pass
    def pressure_stats(self):
        pass
    def station_analysis(self):
        pass
    def summary(self):
        pass 

