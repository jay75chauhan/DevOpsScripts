import os

def web_server_log_analyzer(log_file):
    os.system(f"awk '{{print $1}}' {log_file} | sort | uniq -c | sort -nr")
    print("Web server log analyzed.")
