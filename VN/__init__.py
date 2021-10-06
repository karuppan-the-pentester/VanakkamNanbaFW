import colored
import time


class Message:
    def Help_Message():
        "This function shows you Help Message"
        time.sleep(2)
        print('''
Usage: msfconsole [options]

Database options:
    -C , --create-db     Create a database for User[Automatically deleted the old Database]

        ''')

    def Verrsion_Message():
        "This Function shows you Current version of the Framework"


class Function:
    def Create_Db():
        "This function creates a database for the user and save the exploit results \n[Still under developing]"
