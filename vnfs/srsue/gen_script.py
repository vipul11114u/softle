import sys
import subprocess

hss_file_loc = '../srsepc/hss.conf'
user_db_file_loc = '../srsepc/user_db.csv'
# hss_file_loc = 'hss.conf'
# user_db_file_loc = 'user_db.csv'

open(hss_file_loc, 'w').close()
open(user_db_file_loc, 'w').close()

total_files = int(sys.argv[2])
# print total_files
global_num = 1
in_file_name = ''
hss_arg6_unknwon = '10000000128f'
while global_num <= total_files:
    # print global_num, "->" ,total_files
    if(len(in_file_name) == 0):
        in_file_name = sys.argv[1]
    else:
        in_file_name = out_file_name
    # print 'infile', in_file_name
    with open(in_file_name, "rt") as fin:
        out_file_name = sys.argv[1][0:7] + str(global_num) + '.conf'
        # print out_file_name
        #with open(sys.argv[2], "wt") as fout:
        hss_arg1_name = 'ue'+str(global_num)
        hss_arg2_imsi = ''
        hss_arg3_k = ''
        hss_arg4_op = ''
        hss_arg5_port = ''
        with open(out_file_name, "wt") as fout:
            for line in fin:
                if 'num =' in line:
                    line = line.strip()
                    port = line[-4:]
                    new_port = (int(port) + 1) % 9999
                    hss_arg5_port = str(new_port)
                    line = line.replace(port, str(new_port)) + '\n'
                    line = '0' * (4 - len(line)) + line
                if 'op   =' in line:
                    line = line.strip()
                    op = line[-32:]
                    val = int(op, base=16)
                    hss_arg4_op = str(hex(val + 1))[2:-1]
                    line = line.replace(op, str(hex(val + 1))[2:-1]) + '\n'
                    line = '0' * (32 - len(line)) + line
                if 'k    =' in line:
                    line = line.strip()
                    k = line[-32:]
                    val = int(k, base=16)
                    hss_arg3_k = str(hex(val + 1))[2:-1]
                    line = line.replace(k, str(hex(val + 1))[2:-1]) + '\n'
                    line = '0' * (32 - len(line)) + line
                if 'imsi =' in line:
                    line = line.strip()
                    ismi = line[-15:]
                    num = int(ismi)
                    num = (num + 1) % 999999999999999
                    # val = format(num, '%014d')
                    hss_arg2_imsi = str(num)
                    val = str(num)
                    # print val
                    line = line.replace(ismi, val) + '\n'
                    line = '0' * (15 - len(line)) + line
                fout.write(line)
    fout.close()
    fin.close()
    hss_arg6_unknwon_temp = int(hss_arg6_unknwon, base=16)
    hss_arg6_unknwon_temp+=1
    hss_arg6_unknwon = str(hex(hss_arg6_unknwon_temp))[2:]
    print hss_arg6_unknwon
    hss_list = [hss_arg1_name,hss_arg2_imsi,hss_arg3_k,hss_arg4_op,hss_arg5_port,hss_arg6_unknwon]
    string_to_add = ','.join(hss_list)+'\n'
    print string_to_add
    with open(hss_file_loc, "a") as hss_fout:
        hss_fout.write(string_to_add)
    with open(user_db_file_loc, "a") as user_fout:
        user_fout.write(string_to_add)

    #args = ("srsue", out_file_name)
    #popen = subprocess.Popen(args)
    #popen.wait()
    global_num+=1
