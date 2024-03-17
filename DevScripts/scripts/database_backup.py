import os
import datetime

def database_backup(database_name, output_file):
    os.system(f"mysqldump -u username -ppassword {database_name} > {output_file}_{datetime.datetime.now().strftime('%Y%m%d')}.sql")
    print(f"Database backup created: {output_file}.sql")
