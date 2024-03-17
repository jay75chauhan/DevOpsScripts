import os

def directory_synchronization(source_dir, destination_dir):
    os.system(f"rsync -avz {source_dir} {destination_dir}")
    print("Directories synchronized successfully.")
