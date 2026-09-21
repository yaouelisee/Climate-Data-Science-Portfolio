from src.loader import load_weather_data
from src.processing import process_weather_data
from src.analysis import WeatherAnalyzer

def main():

    # Load weather observation 
    observations = load_weather_data("data/input/weather_data.csv")

    # Create the analyzer 
    analyzer = WeatherAnalyzer(observations)

    # Run analyses 
    print("===WEATHER DATA ANALYSIS===/n")

    print("Temperature:")

    print(analyzer.temperature_stats())

    print("\nRainfall:")

    print(analyzer.rainfall_stats())

    print("\nHumidity:")

    print(analyzer.humididty_stats())

    print("\nStation analysis:")

    print(analyzer.station_analysis())

    if __name__=="__main__":
        main()
    