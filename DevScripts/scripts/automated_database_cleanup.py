import os

def automated_database_cleanup(database_name, days_to_keep):
    os.system(f"find /path/to/database/backups -name '{database_name}*.sql' -mtime +{days_to_keep} -exec rm {{}} \;")
    print("Old database backups cleaned up.")
