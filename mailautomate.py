import speech_recognition as sr
import pyttsx3
import smtplib

def mailsend():
    engine=pyttsx3.init()
    rec=sr.Recognizer()

    def speech():
        try:
            with sr.Microphone() as source:
                audio=rec.listen(source)
                text=rec.recognize_google(audio)
                aud=format(text)
                aud.lower()
                return aud
                
        except:
            engine.say("Not recognisable")
            engine.runAndWait()

    i=0
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    while True:
        if i==0:
            engine.say("Who the recipient sir")
            engine.runAndWait()
            mailid=speech()
            mailid.lower()
            if "myself" in mailid:
                id="sreeharijnair03@gmail.com"
            else:
                engine.say("no such recipient in the list sir")
                engine.runAndWait()
        elif i==1:
            engine.say("whats the body sir")
            engine.runAndWait()
            body=speech()
        else:
            break
        i+=1

    print(f"recipient:{id} body:{body}")
    server.login("sreeharigraph2003@gmail.com","sreeharigraphaccount")
    server.sendmail("sreeharigraph2003@gmail.com",str(id),str(body))
    engine.say("Mail is successfully send to the recipient")
    engine.runAndWait()
