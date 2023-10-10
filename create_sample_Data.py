import random
from datetime import datetime, timedelta
import pandas as pd

# Sample data for Task Labels and Task Names
task_labels = ["Planning Phase","Design Phase", "Development Phase","Testing Phase","Deployment Phase","Monitoring Phase"]
task_names = ["Project Kick-off", "Requirement gathering", "Design","Development","Testing","Deployment","Documentation","Project Review"]

# Initialize an empty list to store the data rows
data_rows = []

# Start date for data generation
start_date = datetime(2023, 10, 9, 8, 0, 0)  # October 9, 2023, 08:00:00

# Generate 100 rows of random data
for _ in range(100):
    # Randomly select Task Label and Task Name
    task_label = random.choice(task_labels)
    task_name = random.choice(task_names)

    # Generate a random duration between 1 second and 60 minutes
    duration_seconds = random.randint(1, 60 * 60)

    # Calculate end time based on duration
    end_time = start_date + timedelta(seconds=duration_seconds)

    # Format the data as strings
    start_time_str = start_date.strftime('%Y-%m-%d %H:%M:%S')
    end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S')
    duration_str = str(timedelta(seconds=duration_seconds))

    # Append the data row to the list
    data_rows.append([task_label, task_name, start_time_str, end_time_str, duration_str])

    # Update start_date for the next row (ensure no backward Task Name sequence)
    task_name_index = task_names.index(task_name)
    task_name_index = (task_name_index + 1) % len(task_names)  # Cycle through task_names
    start_date = end_time + timedelta(seconds=random.randint(1, 60 * 60))

# # Print the first 24 rows of data as an example
# for row in data_rows[:1000]:
#     print(row)

# Convert data_rows to a Pandas DataFrame
df = pd.DataFrame(data_rows, columns=['Task Label', 'Task Name', 'Start DateTime', 'End DateTime', 'Duration'])

# Save the DataFrame to an Excel file
excel_file_path = 'tasks_sampleDB.xlsx'
df.to_excel(excel_file_path, index=False)

print(f'Data saved to {excel_file_path}')
