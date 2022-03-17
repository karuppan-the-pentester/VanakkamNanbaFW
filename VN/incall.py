import colored
from VN import *


class Incall:

    def icall():
        while True:
            ins = str(input("\033[4mvnf1>\033[0m "))
            if ins == "clear":
                os.system('clear')
            if ins == "":
                pass
            else:
                print(red+"[-]"+reset+" Unknown command: "+ins)
