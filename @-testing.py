import getopt
import sys


def cmd_help():
    print("help")


argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "h:")
    # print(getopt.getopt(argv, "h:"))
except:
    print("Error")

for opt, arg in opts:
    if opt in ['-h', '--help']:
        cmd_help()


print()
