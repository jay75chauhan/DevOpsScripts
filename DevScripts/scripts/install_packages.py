import os

def install_packages(packages):
    for package in packages:
        os.system(f"sudo apt-get install {package} -y")
    print("Packages installed successfully.")
