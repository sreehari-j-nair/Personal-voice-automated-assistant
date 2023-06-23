from selenium import webdriver
import time
import pyttsx3
import speech_recognition as sr
from details_configuration import insta_pass,insta_user_name

def instagram():
    r=sr.Recognizer()
    
    engine=pyttsx3.init()

    engine.say("Checking your instagram account")
    engine.runAndWait()

    browser = webdriver.Chrome(executable_path="C:\\Users\\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver\\chromedriver.exe")
    
    engine.say("logging into the instagram site")
    engine.runAndWait()

    browser.get("https://www.instagram.com")
    browser.maximize_window()

    time.sleep(2)

    engine.say("Logging into your account")
    engine.runAndWait()

    input = browser.find_element_by_name("username")
    input.send_keys(insta_user_name)

    input_password=browser.find_element_by_name("password")
    input_password.send_keys(insta_pass)

    search = browser.find_element_by_css_selector('button[type="submit"]')
    search.click()

    time.sleep(4)

    engine.say("Clearing all pop ups")
    engine.runAndWait()

    nonotify = browser.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    nonotify.click()

    time.sleep(1)

    nonotify1 = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    nonotify1.click()

    notification = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > div > div > div')

    if notification == None:
        engine.say("No new messages sir")
        engine.runAndWait()
    else:
        msgs = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > div > div > div')
        messages = msgs.text
        engine.say(f"sir you have got {messages} unreaden messages")
        engine.runAndWait()
        while True:
            try:
                with sr.Microphone() as source:
                    cmdaudio = r.listen(source)
                    cmdtext=r.recognize_google(cmdaudio)
                    cmdvoc=format(cmdtext)
                    cmdvoc.lower()
                    if "check" and "messages" in cmdvoc:
                        messagebutton = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(2) > a > svg > path')
                        engine.say("moving to message interface")
                        engine.runAndWait()
                        messagebutton.click()

                    elif "back" and "main" in cmdvoc:
                        homebutton = browser.find_element_by_css_selector('#react-root > section > div > div._lz6s.Hz2lF > div > div.ctQZg > div > div:nth-child(1) > div > a > svg')
                        engine.say("Moving back to home page")
                        engine.runAndWait()
                        homebutton.click()

                    elif "log" and "out" in cmdvoc:
                        profilebutton = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > span > img')
                        profilebutton.click()
                        logoutbutton = browser.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div:nth-child(5) > div.poA5q > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > div:nth-child(6) > div')
                        engine.say("Logging out from the account")
                        engine.runAndWait()
                        logoutbutton.click()
                        break
                    else:
                        engine.say("command not in list sir")
                        engine.runAndWait()
            except :
                continue
    
    browser.close()
