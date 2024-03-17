import os

def disk_space_monitoring(threshold):
    disk_usage = int(os.popen("df -h | grep '/dev/sda1' | awk '{print $5}' | cut -d% -f1").read().strip())
    if disk_usage > threshold:
        print(f"High disk usage detected: {disk_usage}%")
        # Add alert/notification logic here
