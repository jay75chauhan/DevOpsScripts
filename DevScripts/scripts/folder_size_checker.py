import os

def folder_size_checker(folder_path):
    folder_size = os.popen(f"du -sh {folder_path}").read().strip()
    print(f"Folder size: {folder_size}")
