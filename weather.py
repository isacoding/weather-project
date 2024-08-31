import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # pass
    
    date_obj = datetime.fromisoformat(iso_string)
    return date_obj.strftime("%A %d %B %Y")



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # pass
    
    celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9
   
    return round(celsius, 1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # pass
    weather_data = [float(data) for data in weather_data]
    total = sum(weather_data)
    count = len(weather_data)
    return total / count


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # pass

    data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                row[1] = int(row[1])
                row[2] = int(row[2])
                data.append(row)
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # pass
    
    if not weather_data:
        return ()
    
    min_value = float(weather_data[0])
    min_index = 0
    
    for i in range(1, len(weather_data)):
        current_value = float(weather_data[i])
        if current_value <= min_value:
            min_value = current_value
            min_index = i
            
    return min_value, min_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # pass
    
    if not weather_data:
        return ()
    
    max_value = float(weather_data[0])
    max_index = 0
    
    for i in range(1, len(weather_data)):
        current_value = float(weather_data[i])
        if current_value >= max_value:
            max_value = current_value
            max_index = i
    
    return max_value, max_index



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No data available"

    # Extract dates, min temps, and max temps
    # dates = [datetime.fromisoformat(day[0]) for day in weather_data]
    # min_temps = [convert_f_to_c(day[1]) for day in weather_data]
    # max_temps = [convert_f_to_c(day[2]) for day in weather_data]
    min_temps = [convert_f_to_c(day[1]) for day in weather_data]
    # temp_tuple = find_min(min_temps)
    # min_temp = temp_tuple[0]
    # min_position = temp_tuple[1]
    min_temp, min_position = find_min(min_temps)
    
    max_temps = [convert_f_to_c(day[2]) for day in weather_data]
    max_temp, max_position = find_max(max_temps)
    

    # calculate summary statistics
    # overall_min = min(min_temps)
    # overall_max = max(max_temps)
    avg_min = calculate_mean(min_temps)
    avg_max = calculate_mean(max_temps)
    

    # find the dates of the overall min and max temperatures
    min_date = convert_date(weather_data[min_position][0])
    max_date = convert_date(weather_data[max_position][0])

    # Format the summary
    summary = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {min_date}.\n"
        f"  The highest temperature will be {format_temperature(max_temp)}, and will occur on {max_date}.\n"
        f"  The average low this week is {format_temperature(round(avg_min, 1))}.\n"
        f"  The average high this week is {format_temperature(round(avg_max,1))}.\n"
    )

    return summary



    
def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = ""

    for day in weather_data:
        date = convert_date(day[0])
        min_temp = format_temperature(convert_f_to_c(day[1]))
        max_temp = format_temperature(convert_f_to_c(day[2]))

        daily_summary += (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_temp}\n"
            f"  Maximum Temperature: {max_temp}\n\n"
        )

    return daily_summary

