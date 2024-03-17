import os

def backup_rotation(backup_dir, max_backups):
    while len(os.listdir(backup_dir)) > max_backups:
        oldest_backup = min(os.listdir(backup_dir), key=lambda f: os.path.getctime(os.path.join(backup_dir, f)))
        os.remove(os.path.join(backup_dir, oldest_backup))
    print("Backup rotation completed.")
