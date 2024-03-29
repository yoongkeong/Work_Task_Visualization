import os
from openpyxl import load_workbook
from datetime import datetime
import pandas as pd
import sys

def duration_to_seconds(duration_str):
    # Parse duration in HH:MM:SS format and convert it to seconds
    duration_parts = duration_str.split(':')
    
    hours = int(duration_parts[0])
    minutes = int(duration_parts[1])
    
    # Extract seconds and handle milliseconds
    seconds_millis = duration_parts[2].split('.')
    seconds = int(seconds_millis[0])
    
    if len(seconds_millis) > 1:
        milliseconds = round(float("0." + seconds_millis[1]))  # Convert and round milliseconds
    else:
        milliseconds = 0

    total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds  # Include milliseconds
    return total_seconds

def format_duration(duration_str):
    # Parse duration in HH:MM:SS format and format it as '0:00:00'
    total_seconds = duration_to_seconds(duration_str)
    formatted_duration = f"{int(total_seconds // 3600):02}:{int((total_seconds % 3600) // 60):02}:{int(total_seconds % 60):02}"
    return formatted_duration

def append_task_data(task_label, task_name, start_time_str, end_time_str, duration_str):
    # Define the Excel file path (create it in the current directory)
    excel_file_path = os.path.join(os.getcwd(), 'tasksDB.xlsx')

    # Convert start and end times to datetime objects
    start_time = datetime.strptime(start_time_str, '%Y:%m:%d:%H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y:%m:%d:%H:%M:%S')

    # Format the duration
    formatted_duration = format_duration(duration_str)

    # Create a new row of data as a dictionary
    new_row = {
        'Task Label': task_label,
        'Task Name': task_name,
        'Start DateTime': start_time,
        'End DateTime': end_time,
        'Duration (seconds)': formatted_duration
    }

    # Load the existing Excel file into a pandas DataFrame (if it exists)
    if os.path.exists(excel_file_path):
        df = pd.read_excel(excel_file_path)
    else:
        # Create a new DataFrame if the Excel file doesn't exist
        df = pd.DataFrame(columns=['Task Label', 'Task Name', 'Start DateTime', 'End DateTime', 'Duration (seconds)'])

    # Append the new row to the DataFrame
    df = pd.concat([df, pd.DataFrame([new_row])])

    # Save the updated DataFrame to the Excel file
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
