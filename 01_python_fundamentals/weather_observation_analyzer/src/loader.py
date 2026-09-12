"create a function that loads the data from the CSV file"
def load_weather_data(filename):
    data = []

    with open (filename,"r") as file :
        next(file)

        for line in file :
            data.append(line.strip())

    return data 