import os

def remote_server_backup(source_dir, remote_server):
    os.system(f"rsync -avz {source_dir} {remote_server}")
    print("Files backed up to remote server.")
