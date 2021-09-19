import sys
import time
lowerstr = "[*] Starting Vanakkam Nanba FrameWork.... "
upperstr = lowerstr.upper()
for x in range(len(lowerstr)):
    s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
    sys.stdout.write(s)
    sys.stdout.flush()
    time.sleep(0.1)
for x in range(len(lowerstr)):
    # s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
    # sys.stdout.write(s)
    # sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\r'+lowerstr[0:x] +
                     upperstr[x] + lowerstr[x+1:] + ' |'+'\r')
    # time.sleep(0.1)
    sys.stdout.write('\r'+lowerstr[0:x] +
                     upperstr[x] + lowerstr[x+1:] + ' /'+'\r')
    # time.sleep(0.1)
    sys.stdout.write('\r'+lowerstr[0:x] +
                     upperstr[x] + lowerstr[x+1:] + ' -'+'\r')
    # time.sleep(0.1)
    sys.stdout.write('\r'+lowerstr[0:x] +
                     upperstr[x] + lowerstr[x+1:] + ' \\'+'\r')
    # time.sleep(0.1)

done = 'false'
# here is the animation


def animate():
    for i in range(5):
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' |'+'\r')
        time.sleep(0.1)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' /'+'\r')
        time.sleep(0.1)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' -'+'\r')
        time.sleep(0.1)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' \\'+'\r')
        time.sleep(0.1)


animate()
# long process here
done = 'true'
