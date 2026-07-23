"""
This module contains functions used to analyze weather data .

Each functions receives a list of weather records and returns
aspecific climate indicator .
"""



def count_number_of_observations(records):
    " create a function that counts the number of observations "

    # The number of observations from the begining is 0
    total=0

    # read every line (observation) in records 
    for observation in records :

    # count the number of observations of the current day 
        total+=1

    # send the function back to the program  
    return total   


def find_hottest_day(records):
    "create a function that finds the hottest day of observations "

    # Assume the first observation is the hottest initially
    hottest_temp = records[0]['max_temp']
    hottest_day = records[0]

    # get throuth each observations 
    for day in records :

    # if the current day's temperature is superior to the hottest 
        if day["max_temp"] > hottest_temp:

    # the hottest day is the current day's temperature 
         hottest_temp= day["max_temp"]


         hottest_day = day

    # return the hottest day to the program 
    return hottest_day
    

def find_coldest_day(records):
     " create a funtion that finds the coldest day of observations "
    
    # Assume the first observation is the coldest initially
     coldest_temp = records[0]['min_temp']
     coldest_day = records[0]

    # get through each observation 
     for day in records : 
         
    # if for the current day , the minimal temperature is inferior to the coldest 
         if day["min_temp"] < coldest_temp:
             
    # the coldest temperature is this current day 
             coldest_temp = day["min_temp"]
             coldest_day = day 

    # return the coldest day to the program 
     return coldest_day
         

def find_rainiest_day(records):
    "create a fuction that finds the rainiest day . "

# variable that stores the rainiest 
    rainiest = records[0]['rainfall']
    rainiest_day = records[0]


# get through each observation 
    for day in records :

# if for the current day , the current precipitation is superior to the rainiest 
        if day["rainfall"] > rainiest:

# the rainiest day is this current precipitation 
            rainiest = day["rainfall"]
            rainiest_day = day 

# return the rainiest day 
    return rainiest_day
        

def find_windest_day(records):
    " create a function that finds the windest day "

# create a variable to store the windest 
    windest =  records[0]["wind_speed"]
    windest_day = records[0]

# get through each observations 
    for day in records :

# if for the current day , the wind velocity > windest["windspeed"]
        if day["wind_speed"] > windest :

# the windest day is this current day
            windest = day["wind_speed"]
            windest_day = day

# return the windest day 
    return windest_day
        

def calculate_average_maximum_temperature(records):
    "create a function that calculates the average maximum temperature "

# variable that stores the total temperature 
    total = 0

# get through each observation 
    for day in records :

# Add humidity values from every observation
        total+=day["max_temp"]
        
# variable that store the average 
        average_max_temp = total / len(records)

# Calculate the average maximum temperature
    return average_max_temp
    

def calculate_average_minimum_temperature(records):
    "create a function that calculates the average minimum temperature "

# variable that stores the total temperature 
    total = 0

# get through each observation 
    for day in records :


        total+=day["min_temp"]


        average_min_temp = total/len(records)


    return average_min_temp
    

def calculate_average_rainfall(records):
    "create a function that calculates the average rainfall "


    total= 0


    for day in records:


        total+=day["rainfall"]


        average_rainfall = total/len(records)


        return average_rainfall
    

    def calculate_average_humidity (records):



        total = 0



        for day in records :


            total+=day["humidity"]


            average_humidity = total / len(records)


        return average_humidity 
        

def calculate_average_wind_speed(records):


    total = 0


    for day in records :


        total+=day["wind_speed"]


        average_wind_speed = total/len(records)


    return average_wind_speed
    


def count_rainy_days (records):


    total=0

# Count observations were rainfall is gather than zero 
    for day in records:


        if day["rainfall"] > 0 :


            total+=1


    return total 


def count_dry_days(records):


    total = 0 

# Count days without precipitation
    for day in records :

 
        if day["rainfall"]==0:


            total+=1


    return total 
        

def find_day_with_highest_humidity(records):


# Start the day with the largest difference
    highest_humidity= records[0]['humidity']

    day_with_highest_humidity=records[0]



    for day in records :


        if day["humidity"]> highest_humidity :


            highest_humidity = day['humidity']


            day_with_highest_humidity=day


    return day_with_highest_humidity
        

def compute_daily_temperature_range(records):

# Store the day with the largest difference
    largest_range_day = records[0]

    largest_range = (records[0]["max_temp"]-records[0]["min_temp"])

    for day in records :
        
        current_range = (day["max_temp"]-day["min_temp"])

        if current_range > largest_range : 
            
            largest_range = current_range 

            largest_range_day = day 

    return largest_range_day


        




            




        


        
    







              
    


        









       
