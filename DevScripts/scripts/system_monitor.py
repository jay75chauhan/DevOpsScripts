import subprocess

def system_monitor(threshold):
    cpu_usage = int(subprocess.check_output(["top", "-bn1", "|", "grep", '"Cpu(s)"', "|", "awk", "'{print $2}'"]).decode().split('.')[0])
    if cpu_usage > threshold:
        print(f"High CPU usage detected: {cpu_usage}%")
        # Add alert/notification logic here
