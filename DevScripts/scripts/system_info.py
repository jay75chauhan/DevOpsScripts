import os

def system_info(output_file):
    with open(output_file, 'w') as f:
        f.write("System Information:\n")
        f.write("-------------------\n")
        f.write(f"Hostname: {os.uname().nodename}\n")
        f.write(f"OS: {os.uname().sysname} {os.uname().release}\n")
        f.write(f"Memory: {os.popen('free -h').read().strip()}\n")
        f.write(f"Disk Space: {os.popen('df -h').read().strip()}\n")
    print(f"System info saved to {output_file}.")
