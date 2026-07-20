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
    "create a function that finds the hottest day during the observations "

    # variable that stores the hottest day initially at 0
    hottest = records[0]

    # get throuth each observations 
    for day in records :

    # if the current day's temperature is superior to the hottest 
        if day["max_temp"] > hottest["max_temp"]

    # the hottest day is the current day's temperature 
        hottest= day["temps_max"]

    # return the hottest day to the program 
        return hottest 
    

def find_coldest_day(records):

" create a funtion that"
       
        

        
    

        

        
    
    







