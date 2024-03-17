import os

def network_interface_info(network_interface):
    os.system(f"ifconfig {network_interface}")
    print("Network interface information displayed.")
