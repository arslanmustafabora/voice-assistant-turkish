from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import faceDetect
import graphicalUserInterface
import os

if __name__ == '__main__':

    ID,PASS = "",""

    URL = "https://webmail.etu.edu.tr/roundcube/?_task=mail&_mbox=INBOX"

    programs = os.listdir()

    if 'information.txt' in programs:
        file = open('information.txt','r')
        ID = file.readline()
        PASS = file.readline()
        file.close()

    else:
        ID,PASS = graphicalUserInterface.login()
        file = open('information.txt','a')
        file.write(ID+"\n")
        file.write(PASS)
        file.close()


    found = faceDetect.detect()

    if found == 1:

        opt = Options()
        opt.add_argument("headless")
        br = webdriver.Chrome(options=opt)
        br.get(URL)
        userID = br.find_element_by_xpath("//*[@id='rcmloginuser']")
        password = br.find_element_by_xpath("//*[@id='rcmloginpwd']")
        button = br.find_element_by_xpath("//*[@id='rcmloginsubmit']")
        userID.send_keys(ID)
        password.send_keys(PASS)
        button.click()
        br.maximize_window()
        subjects = br.find_elements_by_class_name("message")
        graphicalUserInterface.screen(subjects)
        br.quit()

