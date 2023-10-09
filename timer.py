import time
import tkinter as tk
from datetime import datetime, timedelta
import subprocess

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.task_name = None
        self.task_label = None
        self.duration = None

    def start(self):
        """Start the timer."""
        self.start_time = datetime.now()
        self.task_name = task_name_entry.get()
        self.task_label = task_label_entry.get()
        self.duration = None

    def stop(self):
        """Stop the timer and calculate the elapsed time."""
        if self.start_time is not None:
            self.end_time = datetime.now()
            elapsed_time = self.end_time - self.start_time
            self.duration = elapsed_time
            self.start_time = None
            return self.duration
        else:
            return timedelta(seconds=0)

def start_timer():
    timer.start()
    timer.start_time = datetime.now()  # Record the start time
    update_timer()

def update_timer():
    if timer.start_time is not None:
        elapsed_time = datetime.now() - timer.start_time
        minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
        timer_label.config(text=f"{int(minutes)}:{int(seconds):02}")
        timer_label.after(1000, update_timer)  # Update every second

def stop_timer():
    task_name = timer.task_name
    task_label = timer.task_label
    start_time = timer.start_time.strftime('%Y:%m:%d:%H:%M:%S') if timer.start_time else "N/A"
    
    duration = timer.stop()
    end_time = timer.end_time.strftime('%Y:%m:%d:%H:%M:%S') if timer.end_time else "N/A"

    if timer.duration:
        duration_str = str(timer.duration)
    else:
        duration_str = "N/A"

    print(f"Task Label: {task_label}")
    print(f"Task Name: {task_name}")
    print(f"Start DateTime: {start_time}")
    print(f"End DateTime: {end_time}")
    print(f"Duration: {duration_str}")
    subprocess.Popen(['python', 'C:\proj_perso\Timer task visualization\excel_appender.py', task_label, task_name, start_time, end_time, duration_str])
    # root.destroy()


if __name__ == "__main__":
    # Create a simple tkinter window for user interaction
    root = tk.Tk()
    root.title("Timer App")

    task_label_label = tk.Label(root, text="Enter Task Label:")
    task_label_label.pack()

    task_label_entry = tk.Entry(root)
    task_label_entry.pack()

    task_name_label = tk.Label(root, text="Enter Task Name:")
    task_name_label.pack()

    task_name_entry = tk.Entry(root)
    task_name_entry.pack()

    timer_label = tk.Label(root, text="0:00", font=("Helvetica", 48))
    timer_label.pack()

    start_button = tk.Button(root, text="Start Timer", command=start_timer)
    start_button.pack()

    stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
    stop_button.pack()

    # Create the timer instance
    timer = Timer()

    root.mainloop()
