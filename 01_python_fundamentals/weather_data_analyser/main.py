from  src.loader import load_weather_data 

from src.analyser import ( count_number_of_observations,find_hottest_day,
find_coldest_day,find_rainiest_day,find_windest_day,calculate_maximum_temperature,
calculate_minimum_temperature,calculate_average_rainfall,calculate_average_humidity,
calculate_average_wind_speed,count_rainy_days,count_dry_days,find_day_with_highest_humidity,
compute_daily_temperature_range)

from src.reporter import generate_report 


def main():

    # Load data 
    records=load_weather_data("data/weather_data.txt ")


    # Analyze weather data 
    number_of_observations = count_number_of_observations(records)
    hottest_day = find_hottest_day(records)
    coldest_day = find_coldest_day(records)
    rainiest_day = find_rainiest_day(records)
    windest_day = find_windest_day(records)
    maximum_temperature = calculate_maximum_temperature(records)
    minimum_temperature = calculate_minimum_temperature(records)
    average_humidity = calculate_average_humidity(records)
    average_rainfall = calculate_average_rainfall(records)
    average_wind_speed = calculate_average_wind_speed(records)
    rainy_days = count_rainy_days(records)
    dry_days = count_dry_days(records)
    day_with_highest_humidity = find_day_with_highest_humidity(records)
    daily_temperature_range = compute_daily_temperature_range(records)


    # create report 
    generate_report(records, number_of_observations, hottest_day,
    coldest_day, rainiest_day, windest_day, maximum_temperature,
    minimum_temperature, average_humidity, average_rainfall,
    average_wind_speed, rainy_days, dry_days, day_with_highest_humidity,
    daily_temperature_range)

if __name__=="__main__":
    main()

    





