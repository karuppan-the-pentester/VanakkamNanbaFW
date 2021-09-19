import sys
import time
lowerstr = "buffering"
upperstr = lowerstr.upper()
for x in range(len(lowerstr)):
    s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
    sys.stdout.write(s)
    sys.stdout.flush()
    time.sleep(0.1)
