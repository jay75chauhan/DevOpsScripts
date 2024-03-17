def log_analyzer(logfile):
    with open(logfile, 'r') as f:
        error_log = [line for line in f if 'ERROR' in line]
    with open('error_log.txt', 'w') as f:
        f.writelines(error_log)
    print("Error log created.")
