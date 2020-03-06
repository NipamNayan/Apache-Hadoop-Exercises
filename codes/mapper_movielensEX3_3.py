

import sys

for line in sys.stdin:
	Data = line.strip().split("::")
	sizeToken=len(Data)
	if(sizeToken==3): 
		print("%s=%s=%s=%s" % (Data[0],Data[1],Data[2],"2"))
	elif(sizeToken>3):
		print("%s=%s=%s%s" % (Data[1],Data[2],"1","0"))
