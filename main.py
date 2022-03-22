# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from flask import Flask
import pywhatkit
# import way2sms
from twilio.rest import Client
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def booking_Page(movie, theater, account_sid, auth_token):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    sleep(10)
    if len(driver.find_elements(By.XPATH, "(//div[@class='wzrk-button-container']//button)[1]"))>0:
        driver.find_element(By.XPATH, "(//div[@class='wzrk-button-container']//button)[1]").click()
    driver.find_element(By.XPATH, "//img[@alt='HYD']").click()
    sleep(5)
    driver.find_element(By.XPATH, "//img[@alt='" + movie + "']").click()
    sleep(2)


    driver.find_element(By.XPATH, "//div[@id='page-cta-container']").click()
    sleep(2)
    driver.find_element(By.XPATH, "(//div[@class='sc-vhz3gb-3 bvxsIo'])[3]").click()
    sleep(2)
    theatersTotal = driver.find_elements(By.XPATH,"//div[@class ='listing-info']")
    print(len(theatersTotal))
    if len(theatersTotal) > 55:
        message = "Theaters added"
        sms_Alert(account_sid, auth_token, message)
    a = 1
    countmsg = 1
    checkNum = 1
    while a==1:
        if len(driver.find_elements(By.XPATH, "//div[@class ='listing-info']//a[contains(text(), '" + theater + "')]")) > 0:
            message = theater + " available"
            sms_Alert(account_sid, auth_token, message)
            sleep(10)
            break
        if len(theatersTotal) > 55:
            message = "Theaters added"

            if(countmsg == 1):
                sms_Alert(account_sid, auth_token, message)
                countmsg = 2
                break
        else:
            sleep(150
                  )
            print(theater+" Not Available - round No:"
                  +str(checkNum))
            checkNum+=1
            driver.refresh()
            continue
    #   twilio:::: id 8886589919 password Pythonsmsindia1234
    driver.close()


def sms_Alert(account_sid, auth_token, message):
    # instantiating the Client
    client = Client(account_sid, auth_token)
    # sending message
    message = client.messages.create(body="'"+message+" For '" + movie + "'", from_="+18647635510"
                                     , to="+918886589919")
    print(message.sid)


# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    driver.implicitly_wait(10)
    driver.get('https://www.bookmyshow.com')
    driver.maximize_window()
    movie = "RRR"
    Theater = "Forum"
    account_sid = "ACc445c05af8aafefd18f7752dfa205998"
    auth_token = "df8e20b1baca95e7af2e79911a00221a"
    try:
        booking_Page(movie, Theater, account_sid, auth_token)
    except  Exception as e:
        driver.get_screenshot_as_file("screenshot.png")
        driver.close()
        print(e)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
