

import sys

for line in sys.stdin:
    dataToken = line.strip().split(",")
    if(len(dataToken)>7):
       
        (flight,delay) = (dataToken[3],dataToken[6])
        if(delay):
        
            print("%s\t%s" % (flight,delay))
