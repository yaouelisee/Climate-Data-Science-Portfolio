from src.loader import load_weather_data
from src.processing import process_weather_data
from src.analysis import WeatherAnalyzer


def save_report(results, output_file):
    """Save analysis results to a text file."""

    with open(output_file, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("           WEATHER OBSERVATION ANALYSIS\n")
        file.write("=" * 60 + "\n\n")

        # Temperature
        max_temp, min_temp, avg_temp = results["temperature"]

        file.write("TEMPERATURE\n")
        file.write("-" * 60 + "\n")
        file.write(f"Maximum temperature : {max_temp:.2f}\n")
        file.write(f"Minimum temperature : {min_temp:.2f}\n")
        file.write(f"Average temperature : {avg_temp:.2f}\n\n")

        # Humidity
        max_humidity, min_humidity, avg_humidity = results["humidity"]

        file.write("HUMIDITY\n")
        file.write("-" * 60 + "\n")
        file.write(f"Maximum humidity : {max_humidity:.2f}\n")
        file.write(f"Minimum humidity : {min_humidity:.2f}\n")
        file.write(f"Average humidity : {avg_humidity:.2f}\n\n")

        # Rainfall
        max_rain, min_rain, avg_rain = results["rainfall"]

        file.write("RAINFALL\n")
        file.write("-" * 60 + "\n")
        file.write(f"Maximum rainfall : {max_rain:.2f}\n")
        file.write(f"Minimum rainfall : {min_rain:.2f}\n")
        file.write(f"Average rainfall : {avg_rain:.2f}\n\n")

        # Wind
        max_wind, min_wind, avg_wind = results["wind"]

        file.write("WIND SPEED\n")
        file.write("-" * 60 + "\n")
        file.write(f"Maximum wind speed : {max_wind:.2f}\n")
        file.write(f"Minimum wind speed : {min_wind:.2f}\n")
        file.write(f"Average wind speed : {avg_wind:.2f}\n\n")

        # Pressure
        max_pressure, min_pressure, avg_pressure = results["pressure"]

        file.write("PRESSURE\n")
        file.write("-" * 60 + "\n")
        file.write(f"Maximum pressure : {max_pressure:.2f}\n")
        file.write(f"Minimum pressure : {min_pressure:.2f}\n")
        file.write(f"Average pressure : {avg_pressure:.2f}\n\n")

        # Stations
        file.write("STATIONS\n")
        file.write("-" * 60 + "\n")

        for station, station_observations in results["stations"].items():
            file.write(
                f"{station} : {len(station_observations)} observation(s)\n"
            )

        file.write("\n")
        file.write("=" * 60 + "\n")
        file.write("Analysis completed successfully.\n")
        file.write("=" * 60 + "\n")


def main():

    # 1. Load data
    data = load_weather_data("data/input/weather_data.csv")

    # 2. Process data
    observations = process_weather_data(data)

    # 3. Analyze data
    analyzer = WeatherAnalyzer(observations)
    results = analyzer.summary()

    # 4. Display results in terminal
    print("\n" + "=" * 60)
    print("           WEATHER OBSERVATION ANALYSIS")
    print("=" * 60)

    print("\nTemperature:", results["temperature"])
    print("Humidity:", results["humidity"])
    print("Rainfall:", results["rainfall"])
    print("Wind:", results["wind"])
    print("Pressure:", results["pressure"])

    print("\nStations:")
    for station, station_observations in results["stations"].items():
        print(f"  {station}: {len(station_observations)} observation(s)")

    # 5. Save report
    output_file = "data/output/analysis_report.txt"

    save_report(results, output_file)

    print(f"\nReport saved to: {output_file}")


if __name__ == "__main__":
    main()