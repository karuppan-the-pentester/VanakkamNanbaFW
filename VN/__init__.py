import colored
import time
import requests
from bs4 import BeautifulSoup
from VN.Auxillary import *

orange = colored.fg("dark_orange")
green1 = colored.fg("spring_green_2a")
red = colored.fg("red")
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
        checking_url = "https://github.com/karuppan-the-pentester/VanakkamNanbaFW/blob/master/version.vnf"
        response = requests.get(checking_url).content
        soup = BeautifulSoup(response, "html.parser")
        version = soup.find("td", {"id": "LC1"})
        print(green1+"Framework Version: "+reset+str(version.text))


class Function:
    def Create_Db():
        "This function creates a database for the user and save the exploit results \n[Still under developing]"

    def CheckingUpdate():
        "This Function is used to check any update in the frame work based on the version of the Framework"
