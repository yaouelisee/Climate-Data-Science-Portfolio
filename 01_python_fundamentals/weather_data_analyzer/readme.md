# Weather Data Analysis System

A Python application that loads, analyzes, and reports weather observations stored in a text file.

This project was built using **only Python fundamentals**, without external libraries such as NumPy, Pandas, or Matplotlib. Its purpose is to demonstrate how core Python concepts can be applied to solve a realistic climate data analysis problem.

---

# Project Objectives

The main objectives of this project are to:

- Read weather observations from a text file.
- Convert raw data into Python dictionaries.
- Analyze weather conditions.
- Compute descriptive climate statistics.
- Generate a clear and organized weather report.
- Practice writing clean, modular, and reusable Python code.

---

# Features

The program can:

- Load weather data from a text file
- Count the total number of observations
- Find the hottest day
- Find the coldest day
- Find the rainiest day
- Find the windiest day
- Calculate the average maximum temperature
- Calculate the average minimum temperature
- Calculate the average rainfall
- Calculate the average humidity
- Calculate the average wind speed
- Count rainy days
- Count dry days
- Find the day with the highest humidity
- Compute the largest daily temperature range
- Display a complete weather analysis report

---

# Project Structure

```
weather_data_analyzer/

|
|-- data/
|   |-- weather_data.txt
|
|-- src/
|   |-- loader.py
|   |-- analyzer.py
|   |-- reporter.py
|
|-- main.py
|
|-- README.md
|
|-- requirements.txt
```

---

# How It Works

## 1. Load the Weather Data

The `loader.py` module opens the weather data file, reads each line, converts every observation into a dictionary, and stores all observations in a list.

Example:

```python
{
    "date": "2026-06-01",
    "max_temp": 32,
    "min_temp": 24,
    "rainfall": 8,
    "humidity": 79,
    "wind_speed": 14
}
```

---

## 2. Analyze the Data

The `analyzer.py` module performs all weather calculations.

It computes:

- averages
- extreme values
- rainy and dry days
- highest humidity
- largest daily temperature range

Each function has a single responsibility, making the code easy to understand and maintain.

---

## 3. Generate the Report

The `reporter.py` module receives the results computed by `analyzer.py` and displays them in a clean and readable weather report.

The reporter **does not perform calculations**. Its only responsibility is presenting the results.

---

# Example Output

```
=============================================
         WEATHER DATA ANALYZER REPORT
=============================================

Period: 2026-06-01 to 2026-06-30

Total days recorded: 30

The hottest day is: 2026-06-08
The maximum temperature is: 35 C

The coldest day is: 2026-06-15
The minimum temperature is: 20 C

The rainiest day is: 2026-06-10
Rainfall: 42 mm

The windiest day is: 2026-06-18
Wind speed: 25 km/h

Average maximum temperature: 31.87 C
Average minimum temperature: 23.40 C

Average rainfall: 8.35 mm
Average humidity: 76.20 %

Average wind speed: 13.80 km/h

Number of rainy days: 17
Number of dry days: 13

Day with the highest humidity: 2026-06-10

Largest daily temperature range: 13 C

=============================================
```

---

# Python Concepts Demonstrated

This project demonstrates the use of:

- Variables
- Data types
- Lists
- Dictionaries
- Loops
- Conditional statements
- Functions
- Modules
- Imports
- File handling
- String formatting
- Basic software architecture

---

# Technologies

- Python 3

No external libraries were used.

---

# Skills Developed

Through this project, I practiced:

- Data processing
- Climate data analysis
- Modular programming
- Code organization
- Problem solving
- Software design
- Python best practices

---

# Future Improvements

Possible future improvements include:

- CSV file support
- Data visualization with Matplotlib
- Data analysis using Pandas
- Monthly and yearly climate summaries
- Interactive command-line interface
- Unit testing
- Export reports to text or PDF

---

# Learning Outcome

This project strengthened my understanding of Python fundamentals while introducing the workflow of a real-world climate data analysis application.

It is the first project in my **Climate Data Science Portfolio**, which aims to combine programming, data science, and environmental analysis.

---

# Author

**Elisee YAOU**

Climate Data Science Portfolio
