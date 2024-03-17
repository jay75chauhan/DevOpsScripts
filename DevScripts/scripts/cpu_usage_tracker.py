import os
import datetime

def cpu_usage_tracker(output_file):
    with open(output_file, 'a') as f:
        cpu_usage = os.popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2}' | cut -d. -f1").read().strip()
        f.write(f"{datetime.datetime.now()} {cpu_usage}%\n")
    print("CPU usage logged.")
