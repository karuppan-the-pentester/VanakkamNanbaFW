#!/usr/bin/python3

import os
import sys
import time


def ProgramStartingAnimation():
    '''
    This Function Provides You an animation Like Metasploit starting animation
    '''
    os.system('clear')
    lowerstr = "[*] Starting Vanakkam Nanba FrameWork.... "
    upperstr = lowerstr.upper()

    for x in range(len(lowerstr)-4):
        time.sleep(0.05)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' |'+'\r')
        time.sleep(0.05)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' /'+'\r')
        time.sleep(0.05)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' -'+'\r')
        time.sleep(0.05)
        sys.stdout.write('\r'+lowerstr[0:x] +
                         upperstr[x] + lowerstr[x+1:] + ' \\'+'\r')


ProgramStartingAnimation()
