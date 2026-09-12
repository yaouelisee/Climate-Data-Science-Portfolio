from src.loader import load_weather_data
from src.processing import process_weather_data

def main():

    # Load weather observation 
    weather_data = load_weather_data("data/input/weather_data.csv")

    if __name__=="__main__":
        main()
    