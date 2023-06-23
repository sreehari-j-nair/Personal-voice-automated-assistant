from selenium import webdriver
import time
import pyttsx3
import speech_recognition as sr

r=sr.Recognizer()
    
engine=pyttsx3.init()

engine.say("Checking your facebook account")
engine.runAndWait()

browser = webdriver.Chrome(executable_path="C:\\Users\\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver\\chromedriver.exe")

engine.say("logging into facebook in the browser")
engine.runAndWait()

browser.get("https://www.facebook.com")
browser.maximize_window()

time.sleep(2)

engine.say("logging in to your account")
engine.runAndWait()

userinput=browser.find_element_by_css_selector('#email')
userinput.send_keys("9847291043")

passinput=browser.find_element_by_css_selector('#pass')
passinput.send_keys("sreeind")

loginbutton=browser.find_element_by_css_selector('#u_0_b')
loginbutton.click()

time.sleep(3)

updater=browser.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.dp1hu0rb.p01isnhg > div > div.rq0escxv.lpgh02oy.du4w35lb.o387gat7.qbu88020.pad24vr5.rirtxc74.dp1hu0rb.fer614ym.ni8dbmo4.stjgntxs.rek2kq2y.be9z9djy.bx45vsiw > div > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div > div > div.buofh1pr > div:nth-child(2) > ul > li:nth-child(2) > div > a > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.nnctdnn4.hpfvmrgz.qt6c0cv9.jb3vyjys.l9j0dhe7.du4w35lb.bp9cbjyn.btwxx1t3.dflh9lhu.scb9dxdr > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.tgvbjcpo.hpfvmrgz.qt6c0cv9.rz4wbd8a.a8nywdso.jb3vyjys.du4w35lb.bp9cbjyn.btwxx1t3.l9j0dhe7 > div > div > div > div:nth-child(2) > span > span > span')
if updater==None:
    engine.say("You have got no new notifications sir")
    engine.runAndWait()
else:
    msgs=updater.text
    engine.say(f"You have got {msgs} sir")

browser.close()
