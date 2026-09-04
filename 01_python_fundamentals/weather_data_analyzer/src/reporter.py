def generate_report(records,total,hottest_days,coldest_day,
    rainiest_day,windest_day,average_maximum_temperature,average_minimum_temperature,
    average_rainfall,average_humidity,average_wind_speed,count_rainy_days,count_dry_days,
    day_with_highest_humidity,largest_range_day ):
    """
    print a clean aligned weather report to the terminal.
    Each parameter is a result already computed by analyzer.py-
    this function's only job is to display them well.

    """
    # "=" * 45 repeats the "=" character 45 times to build a seperator line
    print("="*45)
    #.center(45) pads the title with spaces so it's centered 
    # within a 45-character width, matching the seperator lines above/below
    print("WEATHER DATA ANALYSER REPORT".center(45))
    print("="*45)

    # records[0] is the first day in the list , records[-1]is the last day 
    #(-1 means "last elment" in python, no matter the list's length )
    print(f"Period:{records[0]['date']} to {records[-1]['date']}")
    print(f"Total days recorded :{total}")
    print("="*45)

    # :.2f formats a number to exactly 2 decimal places (e.g. 32.02)
    print(f"\nThe hottest day is  : {hottest_days['date']}"  )
    print(f"The maximum temperature is :{hottest_days['max_temp']}C")

    print(f"\n the coldest day is :{coldest_day['date']}")
    print(f"The minimum temperature is :{coldest_day['min_temp']}C")

    print(f"\n The rainiest day is :{rainiest_day['date']}")
    print(f"The highest rainfall is : {rainiest_day['rainfall']}mm")

    print(f"\nThe windest day is : {windest_day['date']}")
    print(f"The highest wind speed is : {windest_day['wind_speed']}km/h")

# Display every average of analyser.py 
    print(f"\nThe average maximum temperature is :{average_maximum_temperature:.2f}C")

    print(f"The average minimum temperature is :{average_minimum_temperature:.2f}C")

    print(f"The average rainfall is :{average_rainfall:.2f}mm")

    print(f"The average humidity is :{average_humidity:.2f} %")
    
    print(f"The average wind speed is :{average_wind_speed:.2f}km/h")

# Display the number of rainy days and the number of dry days 
    print(f"Number of rainy days :{count_rainy_days}")
    
    print(f"Number of dry days :{count_dry_days}")

# Display the day with the highest humidity 
    print(f"\nThe day with the highest humidity is :{day_with_highest_humidity}")

# Display the daily temperature range 
    print(f"The daily temperature range is :{largest_range_day}C")


    





