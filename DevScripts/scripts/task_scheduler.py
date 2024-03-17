import os

def task_scheduler(scheduled_task, schedule_time):
    os.system(f"echo '{schedule_time} {scheduled_task}' | crontab -")
    print("Task scheduled successfully.")
