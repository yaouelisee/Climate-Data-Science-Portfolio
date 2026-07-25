    




def calculate_average_maximum_temperature(records):
    "create a function that calculates the average maximum temperature "

# variable that stores the total temperature 
    total = 0

# get through each observation 
    for day in records :


        total+=day["temperature"]
        
        return total 
    
    records = [day=={ "date[0]": 1 , "temp[0]":int("32"), "rainfall[0]":33 ,
                     "date[1]":2 ,"temp[1]": 42,"rainfall[1]": 22}
              ]
        
    calculate_average_maximum_temperature(records)
    print(total)
    
  




