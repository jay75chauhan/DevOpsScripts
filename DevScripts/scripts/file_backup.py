import os
import shutil
import datetime

def file_backup(backup_dir, source_dir):
    backup_filename = f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
    backup_path = os.path.join(backup_dir, backup_filename)
    shutil.make_archive(backup_path, 'gztar', source_dir)
    print(f"Backup created: {backup_path}")
