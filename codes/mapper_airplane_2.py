

import sys

for line in sys.stdin:
    dataToken = line.strip().split(",")
    if(len(dataToken)>7):

        
        (flight,delay) = (dataToken[3],dataToken[8])
        if(delay):
        #we know at 3 index airport_id and last index delayTime
            print("%s\t%s" % (flight,delay))
