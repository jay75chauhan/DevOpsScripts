import os

def service_restart(service_name):
    os.system(f"sudo systemctl restart {service_name}")
    print(f"Service {service_name} restarted.")
