import colored
import time

orange = colored.fg("dark_orange")
green1 = colored.fg("spring_green_2a")
reset = colored.attr("reset")


class Message:
    def Help_Message():
        "This function shows you Help Message"
        time.sleep(2)
        print('''
Usage: python3 Vanakkam_NanbaFW.py [options]

Database options:
    -C , --create-db     Create a database for User to store the attack data [Automatically deleted the old Database]

Framework options:
    -v , --version       Show version

Console options:
    -q, --quick          Do not print the banner on startup
    -h, --help           Show this message
        ''')

    def Verrsion_Message():
        "This Function shows you Current version of the Framework"


class Function:
    def Create_Db():
        "This function creates a database for the user and save the exploit results \n[Still under developing]"
