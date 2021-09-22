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
    os.system('clear')


def banner():
    '''
    This Function provides You Banner
    '''
    banners = [
        '''
                 ,           ,
                /             \\
               ((__---,,,---__))
                  (_) O O (_)_________
                     \ _ /            |\\
                      o_o \   V N F   | \\
                           \   _____  |  *
                            |||   WW|||
                            |||     |||


       =[ vanakkam_nanba v1.0.0-dev                       ]
+ -- --=[ 1 exploits - 1 auxiliary - 1 post               ]
+ -- --=[ 0 payloads - 0 encoders  - 0 nops               ]
+ -- --=[ 0 evasion                                       ]
''', ]
    print(banners[0])


ProgramStartingAnimation()
banner()
