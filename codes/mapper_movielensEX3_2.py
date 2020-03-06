

import sys

for line in sys.stdin:
	Data = line.strip().split("::")
	if(len(Data)>=3): # check for empty line or false data
		print('%s=%s' % (Data[0],Data[2]))

