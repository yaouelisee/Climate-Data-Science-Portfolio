class WeatherStation: 
    def __init__(self,date,station,temperature,humidity,rainfall,wind_speed,pressure):
        self.date = date
        self.station = station
        self.temperature = temperature 
        self.humidity = humidity 
        self.rainfall = rainfall
        self.wind_speed = wind_speed
        self.pressure = pressure 

def process_weather_data(data):
    clean_data = []

    for line in data :

        # Ignore empty lines 
        if not line.strip():
            continue
        # Check the number of columns 
        if len(values) != 7:
            print("Invalid row :{line}")
            continue 

        values = line.split(',')

        date = values[0].strip()
        station =  values[1].strip()

        try:
            temperature = float(values[2])
            humidity = float(values [3])
            rainfall = float(values[4])
            wind_speed = float(values[5])
            pressure = float(values[6])

        except ValueError :
            print(f"Invalid numerical data :{line}")
            continue 


        observations = WeatherStation (date,station,temperature,humidity,rainfall,wind_speed,pressure)

        clean_data.append(observations)

    return clean_data