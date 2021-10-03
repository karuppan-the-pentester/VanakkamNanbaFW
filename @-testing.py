import getopt
import sys


def cmd_help():
    print("help")


argv = sys.argv[1:]
options = "hq:"
l_options = ["help", "quick"]
try:
    arguments, values = getopt.getopt(argv, options, l_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print("Displaying Help")
        elif currentArgument in ("-q", "--quick"):
            print("Quick")

except Exception as e:
    print(e)
