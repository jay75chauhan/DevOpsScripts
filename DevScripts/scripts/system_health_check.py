import os

def system_health_check(output_file):
    with open(output_file, 'w') as f:
        f.write("System Health Check:\n")
        f.write("---------------------\n")
        f.write(f"Uptime: {os.popen('uptime').read().strip()}\n")
        f.write(f"Load Average: {os.popen('cat /proc/loadavg').read().strip()}\n")
        f.write(f"Memory Usage: {os.popen('free -m').read().strip()}\n")
    print(f"System health check results saved to {output_file}.")
