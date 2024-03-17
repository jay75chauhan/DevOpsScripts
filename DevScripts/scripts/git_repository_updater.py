import os

def git_repository_updater(git_repo):
    os.system(f"cd {git_repo} && git pull origin master")
    print("Git repository updated.")
