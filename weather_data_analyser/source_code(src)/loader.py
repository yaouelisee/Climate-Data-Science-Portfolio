def load_weather_data(file_path):

    """create a funtion that reads the weather_data.txt file and converts it into a list of dictionnaries."""

    # This variable will store all weather observations 
    weather_records=[]
 
    # skip the header
    next(file)

    # This built-in opens the file as a read mode 
    with open (file_path,"r") as file:

        # Read the file one line at time 
        for line in file :

            # Remove spaces and the newline character at the end (/n)
            line = line.strip()

            # Split the line into seperate values using commas 
            parts = line.split(",")

            # Create a dictionnary representing one weather observation 
            day = {
                "date"=parts[0], max_temp =int(parts[1]), min_temp=int(parts[2]), rainfall=int(parts[3]), humidity=int(parts[4]), wind_speed=int(parts[5])}

            # Add the weather dictionnary into the empty list 
            weather_records.append(weather)

            # send the complete dataset back to the program 
            return weather_records
        



        
       
