import os

def website_checker(website):
    response = os.system(f"curl --output /dev/null --silent --head --fail {website}")
    if response == 0:
        print("Website is up.")
    else:
        print("Website is down.")
