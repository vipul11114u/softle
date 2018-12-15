import sys
import subprocess
import time

hss_file_loc = '../srsepc/hss.conf'
user_db_file_loc = '../srsepc/user_db.csv'

total_files = int(sys.argv[2])

global_num = 1
while global_num <= total_files:    
    out_file_name = sys.argv[1][0:7] + str(global_num) + '.conf'
    args = ("srsue", out_file_name)
    popen = subprocess.Popen(args)
    global_num += 1
    time.sleep(1)
