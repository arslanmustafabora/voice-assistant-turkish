import pyautogui
import bot
def login():
    user_name = pyautogui.prompt(text="Enter your username", title="USERNAME", default="")
    password = pyautogui.password(text="Enter your password", title="PASSWORD", default="")
    return user_name, password
def screen(subjects):
    empty = ""
    today = ""
    for i in range(20):
        empty += str(subjects[i].text) + "\n"
        if "Bugün" in subjects[i].text:
            today += str(subjects[i].text) + "\n"

    bot.speak("Bugün size mail göndermiş kişiler şunlardır")
    bot.speak(today)
    pyautogui.alert(text=empty, title="Recently", button="Okey")