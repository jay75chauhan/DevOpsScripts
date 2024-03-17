import os

def remote_script_execution(remote_server, remote_script):
    os.system(f"ssh {remote_server} 'bash -s' < {remote_script}")
    print("Remote script executed.")
