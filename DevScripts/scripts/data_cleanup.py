import os

def data_cleanup(directory):
    os.system(f"find {directory} -type f -mtime +7 -exec rm {{}} \;")
    print("Old files removed.")
