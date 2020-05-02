import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import cv2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def speak(text):
    tts = gTTS(text=text, lang="tr")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    r.pause_treshold = 1
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio,language = "tr-TR")
            print(said)
        except Exception as e:
            print(str(e))


    return said.lower()


WAKE = "yardımcı"


if __name__ == '__main__':

    speak("Sisteme hoş geldiniz")
    while True:

        text = listen()

        if text.count(WAKE) > 0:
            speak("Göreve hazırım")
            job = listen()
            if "mail" in job:
                speak("Maillerinize bakmadan önce yüzünüzü tanıtın")
                os.system("python TobbMailAutomation.py")
                speak("Sisteme son giren kişi lastSeen.jpeg dosyasındadır")


            elif "görüşürüz" in job:
                speak("Görüşürüz efendim")
                break

            elif "müzik" in job:
                speak("Spotify açılıyor")
                os.system(r"")          #Spotifyın exe dosyasının konumunu veriniz

            elif "arkadaşlarla muhabbet" in job:
                speak("Discord açılıyor")
                os.system(r"")          #Discordun exe dosyasının konumunu veriniz 

            elif "oyunlar" in job:
                speak("Steam açılıyor")
                os.system(r"")          #Steamin exe dosyasının konumunu veriniz

            elif "araştır" in job:
                speak("Ne araştırmamı istersiniz?")
                research = listen()
                speak("{} hakkında araştırma yapıyorum".format(research))

                opt = Options()
                opt.add_argument("headless")
                br = webdriver.Chrome(options=opt)
                br.get("https://www.google.com.tr")
                searchBar = br.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
                searchBar.send_keys(research+"\n")
                time.sleep(1)
                description = br.find_elements_by_class_name("kno-rdesc")
                for i in description:
                    speak(i.text)


            else:
                speak("Anlamadım")

