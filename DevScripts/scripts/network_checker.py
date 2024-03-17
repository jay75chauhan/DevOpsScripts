import os

def network_checker(host):
    response = os.system(f"ping -c 1 {host} &>/dev/null")
    if response == 0:
        print("Network is up.")
    else:
        print("Network is down.")
