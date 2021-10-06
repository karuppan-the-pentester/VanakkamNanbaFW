#!/usr/bin/python3

import os
import sys
import time
import getopt
from VN import *


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


       =[ vanakkam_nanba v1.0.0-dev                ]
+ -- --=[ 1 exploits - 1 auxiliary - 1 post        ]
+ -- --=[ 0 payloads - 0 encoders  - 0 nops        ]
+ -- --=[ 0 evasion                                ]
''', '''

''']
    print(banners[0])


argv = sys.argv[1:]
options = "hqgC0:"
l_options = ["help", "quick", "graphical", "create-db", "none"]
try:
    arguments, values = getopt.getopt(argv, options, l_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            Message.Help_Message()
        elif currentArgument in ("-q", "--quick"):
            time.sleep(3)
        elif currentArgument in ("-C", "--create-db"):
            Function.Create_Db()
    if len(sys.argv) == 1:
        ProgramStartingAnimation()
        banner()
except KeyboardInterrupt:
    print()
except Exception as e:
    print(e)
