import os
from openpyxl import Workbook, load_workbook
from datetime import datetime, timedelta
import pandas as pd
import sys

def duration_to_seconds(duration_str):
    # Parse duration in HH:MM:SS format and convert it to seconds
    duration_parts = duration_str.split(':')
    
    hours = int(duration_parts[0])
    minutes = int(duration_parts[1])
    
    # Extract seconds and handle decimal parts
    seconds_with_millis = duration_parts[2].split('.')
    seconds = int(seconds_with_millis[0])
    
    # Handle optional milliseconds
    if len(seconds_with_millis) > 1:
        milliseconds = int(seconds_with_millis[1])
    else:
        milliseconds = 0

    total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000  # Convert milliseconds to seconds
    return total_seconds

def append_task_data(task_label, task_name, start_time_str, end_time_str, duration_str):
    # Define the Excel file path (create it in the current directory)
    excel_file_path = os.path.join(os.getcwd(), 'tasks.xlsx')

    # Convert start and end times to datetime objects
    start_time = datetime.strptime(start_time_str, '%Y:%m:%d:%H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y:%m:%d:%H:%M:%S')

    # Convert duration to seconds
    duration_seconds = duration_to_seconds(duration_str)

    # Create a Pandas DataFrame with the task data
    data = {
        'Task Label': [task_label],
        'Task Name': [task_name],
        'Start DateTime': [start_time],
        'End DateTime': [end_time],
        'Duration (seconds)': [duration_seconds]
    }

    df = pd.DataFrame(data)

    # Create a new Excel file with a visible worksheet
    with pd.ExcelWriter(excel_file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Task Data', index=False)

    print("Task data appended to Excel file.")

if __name__ == "__main__":
    # Receive task data as command-line arguments from timer.py
    task_label = sys.argv[1]
    task_name = sys.argv[2]
    start_time_str = sys.argv[3]
    end_time_str = sys.argv[4]
    duration_str = sys.argv[5]

    # Call the append_task_data function with the received values
    append_task_data(task_label, task_name, start_time_str, end_time_str, duration_str)
