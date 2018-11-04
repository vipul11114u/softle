import sys

with open(sys.argv[1], "rt") as fin:
    with open(sys.argv[2], "wt") as fout:
        for line in fin:
			if 'num =' in line:
				port = line[-4:]
				new_port = (int(port) + 1) % 9999				
				line = line.replace(port, str(new_port)) + '\n'
				line = '0'*(4-len(line))+line
			if 'op   =' in line:
				op = line[-32:]
				val = int(op, base = 16)
				line = line.replace(op, str(hex(val+1))[2:-1]) + '\n'
				line = '0'*(32-len(line))+line
			if 'k    =' in line:
				k = line[-32:]
				val = int(k, base = 16)
				line = line.replace(k, str(hex(val+1))[2:-1]) + '\n'
				line = '0'*(32-len(line))+line
			if 'imsi =' in line:
				ismi = line[-15:]
				num = int(ismi)
				num = (num+1) % 999999999999999
				#val = format(num, '%014d')
				val = str(num)
				line = line.replace(ismi, val) + '\n'
				line = '0'*(15-len(line))+line
			fout.write(line)
