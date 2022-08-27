# -*- coding: utf-8 -*-
#Coded by Coder Productions
#Сюда нельзя лазить!
import os
import random
from subprocess import check_output
from os.path import abspath
import subprocess
from turtle import width
a = 0
import time
import sys
from sys import platform
def clear():
    os.system('cls || clear')
def pip():
    print('Program: В данный момент происходит установка некоторых файлов, для роботы программы\nВремя установки продлится 3-5 минут')
    time.sleep(3)
    if platform == "linux" or platform == "linux2":
        print('Linux os: Программа не будет работать')
        sys.exit(1)
    elif platform == "darwin":
        input('Mac os: Данная программа не поддерживаается вашей операционной системой\nНажмите Enter для продолжения: ')
        sys.exit(1)
    elif platform == "win32":
        os.system('pip install pipwin --quiet --disable-pip-version-check')
        os.system('pipwin install pyaudio --quiet --disable-pip-version-check')
        os.system('pipwin install pyttsx3 --quiet --disable-pip-version-check')
    os.system('pip install vosk --quiet --disable-pip-version-check')
    os.system('pip install SpeechRecognition --quiet --disable-pip-version-check')
    os.system('pip install youtube_dl --quiet --disable-pip-version-check')
    os.system('pip install pyttsx3 --quiet --disable-pip-version-check')
    os.system('pip install pyaudio --quiet --disable-pip-version-check')
    os.system('pip install Wave --quiet --disable-pip-version-check')
    os.system('pip install pytube --quiet --disable-pip-version-check')
    os.system('pip install json --quiet --disable-pip-version-check')
    os.system('pip install requests --quiet --disable-pip-version-check')
    os.system('pip install bs4 --quiet --disable-pip-version-check')
    os.system('pip install google --quiet --disable-pip-version-check')
    os.system('pip3 install Plyer --quiet --disable-pip-version-check')
    os.system('pip install colorama --quiet --disable-pip-version-check')
    os.system('pip install pyqt5 --quiet --disable-pip-version-check')
    os.system('pip install PyQtWebEngine --quiet --disable-pip-version-check')
    
    os.system('pip install pyperclip --quiet --disable-pip-version-check')
    os.system('pip install pyfiglet --quiet --disable-pip-version-check') 
    os.system('winget install --id Git.Git -e --source winget --quiet --disable-pip-version-check')
    
    print('Program: Перезапустите программу')
    input('Input : ')
    time.sleep(1)
    sys.exit(1)
while 1:
    try:
        from PyQt5.QtCore import *
        from PyQt5.QtWidgets import *
        from PyQt5.QtWebEngineWidgets import *
        from colorama import Fore
        from colorama import init
        from pyfiglet import Figlet
        import folium
        import pyperclip
        from colorama import *
        import plyer
        import youtube_dl
        from pytube import YouTube
        import webbrowser
        from vosk import Model, KaldiRecognizer #pip install vosk
        import speech_recognition  #pip install SpeechRecognition
        import pyttsx3  #pip install pyttsx3
        import wave  #pip install Wave
        import json #pip install json
        import requests #pip install requests
        from bs4 import BeautifulSoup #pip install bs4
        parametr = 1
        break
    except ImportError:
        pip()
def checkfile(file):
    try:
        with open(file, 'r', encoding='utf-8') as check:
            check.read()
            check.close
        return True
    except:
        return False

def chck_path(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True

    
class VoiceAssistant:
    name = ""
    sex = ""
    speech_language = "ru"
    recognition_language = ""
    


def update(x):
    url = f"https://sites.google.com/view/coderprogrammers/codechecker"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    vs = '#перенос'
    version_ACTUA = soup.find("div", class_="tyJCtd mGzaTb Depvyb baZpAe").text.replace(f'\\n{vs}','\n')
    
    from os.path import sep
    g = __file__.split(sep)[-1]
    with open (g, 'w',  encoding='utf-8') as f:
        f.write(version_ACTUA)
        print('Program: Чтобы обновление вступило в силу перезапустите программу')
def start(versionactivity, x, admin_preset, empty):
    def animation(x):
        animation = "|/-\\"
        for i in range(x):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
    def checkadmin():
        if admin_preset == 1:
            print(f'[{Fore.YELLOW} ⚝ {Fore.WHITE} ] Alis started in development mode [{Fore.YELLOW} ⚝ {Fore.WHITE} ] ')
    def checkversion(x):
        version ='Version - 7.0.0'
        url = f"https://sites.google.com/view/coderprogrammers/alis_version_checher"
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        version_ACTUALITY = soup.find("div", class_="jXK9ad-SmKAyb").text
        if version != version_ACTUALITY and x == 1:
            print('Версия устарела')
            url = f"https://sites.google.com/view/coderprogrammers/codechecker"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            vs = '#перенос'
            version_ACTUA = soup.find("div", class_="tyJCtd mGzaTb Depvyb baZpAe").text.replace(f'\\n{vs}','\n')
            play_voise('Так как ваша версия устарела, я обновлю её', 'Так как ваша версия устарела, я обновлю её')
            from os.path import sep
            g = __file__.split(sep)[-1]
            with open (g, 'w',  encoding='utf-8') as f:
                f.write(version_ACTUA)
                print('Program: Чтобы обновление вступило в силу перезапустите программу')
        elif x != 1:
            print('Program: Авто-обновление отключено')
    def setup_assistant_voice():
        voices = ttsEngine.getProperty("voices")
        if assistant.speech_language == "en":
            assistant.recognition_language = "en-US"
            if assistant.sex == "man":
                ttsEngine.setProperty("voice", voices[1].id)
            else:
                ttsEngine.setProperty("voice", voices[2].id)
        else:
            assistant.recognition_language = "ru-RU"
            ttsEngine.setProperty("voice", voices[0].id)
    def play_voise(text_to_speech, text_to_print = 'Null'):
        ttsEngine.say(text_to_speech)
        ttsEngine.runAndWait()
        print(f'Alis: {text_to_print}\n\n')

    def xC_3():
        return "ty$ #t d / m Gza Tb / De pv yb/ ba 🎸p A 7"
    def record_audio(*args: tuple):
        with microphone:
            recorded_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)
            try:
                print("Program: Говорите")
                audio = recognizer.listen(microphone, 5, 5)
                with open("microphone-results.wav", "wb") as file:
                    file.write(audio.get_wav_data())
            except speech_recognition.WaitTimeoutError:
                play_voise('Ой произошла ошибка', 'Ой произошла ошибка')
                return
            try:
                print("Program: Стоп. Распознавание")
                recorded_data = recognizer.recognize_google(audio, language="ru").lower()
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                print("Program: Попытка использовать офлайн-распознавание... Для этого скачайте vosk - model - ru. И переместите её в папку с Alis")
                recorded_data = use_offline_recognition()
            return recorded_data
        os.remove("microphone-results.wav")
    def record_audio2(*args: tuple):
        """
        Запись и распознавание аудио
        """
        with microphone:
            recorded_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)
            try:
                print("Program: Говорите...")
                audio = recognizer.listen(microphone, 5, 5)
                with open("microphone-find.wav", "wb") as file:
                    file.write(audio.get_wav_data())
            except speech_recognition.WaitTimeoutError:
                print("Program: Error")
                return
            try:
                print("Program: Распознавание")
                recorded_data2 = recognizer.recognize_google(audio, language="ru").lower()
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                print("Program: Попытка использовать офлайн-распознавание...")
                recorded_data2 = use_offline_recognition()
            return recorded_data2

    def record_audio3(*args: tuple):
        """
        Запись и распознавание аудио
        """
        with microphone:
            recorded_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)
            try:
                print("Название файла...")
                audio = recognizer.listen(microphone, 5, 5)
                with open("microphone-find.wav", "wb") as file:
                    file.write(audio.get_wav_data())
            except speech_recognition.WaitTimeoutError:
                print("Program: Error")
                return
            try:
                print(f"Записываю текст в файл ")
                recorded_data3 = recognizer.recognize_google(audio, language="ru").lower()
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                print("Program: Попытка использовать офлайн-распознавание...")
                recorded_data3 = use_offline_recognition()
            return recorded_data3
    def use_offline_recognition():
        recorded_data = ""
        try:
            if not os.path.exists("models/vosk-model-small-ru-0.4"):
                print("Program: Ссылка на скачивание мини версии --+ https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip")
                exit(1)
            if input('Program: Вывести инструкцию по скачиванию и установке? [Y/n] -- ') == 'y':
                print('Program: Для начала стоит скачать модель vosk по ссылке\nДалее стоит распаковать папку внутри\nПереметить её в одну папку с Alis\nПереименуйте её в vosk_main-ru')
            wave_audio_file = wave.open("microphone-results.wav", "rb")
            model = Model("vosk_main-ru")
            offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())
            data = wave_audio_file.readframes(wave_audio_file.getnframes())
            if len(data) > 0 and offline_recognizer.AcceptWaveform(data):
                recorded_data = offline_recognizer.Result()
                recorded_data = json.loads(recorded_data)
                recorded_data = recorded_data["text"]
        except Exception:
            print("К сожалению модель Vosk не найдена")
        return recorded_data
    if __name__ == "__main__":
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        ttsEngine = pyttsx3.init()
        assistant = VoiceAssistant()
        asault_ = xC_3()
        assistant.name = "Alis"
        assistant.sex = "man"
        assistant.speech_language = "ru"
        setup_assistant_voice()
        checkadmin()
        checkversion(x)
        while versionactivity == 1:
            voice_input = record_audio()
            voice_input = voice_input.replace('элис', 'Alis')
            print(f'Вы: {voice_input}')
            voice_input = voice_input.split(" ")
            command = ' '.join(voice_input)
            find1 = command
            homeDir = os.path.expanduser("~/Onedrive/Рабочий стол/")
            h = os.listdir(homeDir)
            find = homeDir + find1


            if f'{find1.title()}.lnk' in h:
                play_voise('Запускаю', 'Запускаю')
                os.system( 'start cmd "' + find + '.lnk"')



            elif f'{find1.title()}.url' in h:
                play_voise('Запускаю', 'Запускаю')
                os.system('start cmd "' + find + '.url"')



            elif f'{find1.title()}.exe' in h:
                play_voise('Запускаю', 'Запускаю')
                os.system('start cmd "' + '"' + find + '.exe"')



            else:
                if 'привет' == command:
                    play_voise('Привет, я Alis', 'Привет, я Alis')


                elif 'telegram' == command:
                    play_voise('Открываю телеграм', 'Открываю Telegram')
                    
                    webbrowser.open('https://web.telegram.org')


                elif 'google' == command:
                    play_voise('Открываю гугл', 'Открываю Google')
                    
                    webbrowser.open('https://www.google.com')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово :)')
                elif 'сайт' == command:
                    
                    
                    webbrowser.open('https://sites.google.com/view/alisvoise/alis?authuser=0')
                    

                elif 'музыка' == command or 'spotify' == command:
                    play_voise('Открываю Спотифай', 'Открываю spotify')
                    
                    webbrowser.open('https://open.spotify.com')


                elif 'погода' == command or 'откройпогоду' == command:
                    play_voise('Открываю погоду', 'Открываю погоду.')
                    
                    webbrowser.open('https://weather.com/weather/today')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово :)')



                elif 'youtube' == command or 'откройyoutube' == command:
                    play_voise('Открываю ютуб', 'Открываю YouTube O.O')
                    
                    webbrowser.open('https://www.youtube.com')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово!')



                elif 'google trnslator' == command or 'google переводчик' == command:
                    play_voise('Открываю гугл переводчик', 'Открываю Google-Переводчик 去')
                    
                    webbrowser.open('https://translate.google.com')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово :)')



                elif 'taskmanager' == command or 'диспетчер задач' == command:
                    play_voise('Открываю диспетчер задач', 'Открываю диспетчер задач :O')
                    os.system('taskmgr')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово!')



                elif 'calculator' == command or 'калькулятор' == command:
                    play_voise('Открываю калькулятор', 'Открываю Calculator')
                    os.system('calc')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово :|')



                elif 'notepad' == command or 'блокнот' == command:
                    play_voise('Открываю блокнот', 'Открываю Блокнот :3')
                    os.system('notepad')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово!')



                elif 'explorer' == command or 'проводник' == command:
                    play_voise('Открываю проводник', 'Открываю Exploarer')
                    os.system('explorer')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово!')



                elif 'добавить команду' == command or 'add command' == command:
                    cfgcommand = input('Как вызвать команду\n [ <voise command> ]')
                    play_voise(f'Для того что-бы вызвать команду скажите, {cfgcommand}', f'Для того что-бы вызвать команду скажите, {cfgcommand}')
                    cfg_voise = input('Что мне говорить?\n чтобы я промолчала напишите 0\n [ <voise> ]')
                    if cfg_voise != '0':
                        play_voise(f'Я отвечу {cfg_voise}', f'Я отвечу {cfg_voise}')
                    elif cfg_voise == "0":
                        play_voise(f'Я буду молчать', f'Я буду молчать :(')
                    clear()
                    f = input('Введите действие [ </...> ]')

                    enter = '\n'
                    tab = '\n   '
                    tab2 = '                '
                    tab3 = '\r                '
                    s = "'"
                    m_check = 0
                    if f == 'открыть сайт' or f == 'сайт' or f == 'site':
                        m_check = 1
                        if cfg_voise == "0":
                            clear()
                            opensite_cfg = input('Ваш сайт')
                            command_cfg = f'{tab2}elif {s}{cfgcommand}{s} == command:{tab}{tab2}{tab}{tab2}webbrowser.open("{opensite_cfg}"){tab3}else:# -- Config --'
                        else:
                            clear()
                            opensite_cfg = input('Ваш сайт')
                            command_cfg = f'{tab2}elif {s}{cfgcommand}{s} == command:{tab}{tab2}play_voise({s}{cfg_voise}{s}){tab}{tab2}{tab}{tab2}webbrowser.open("{opensite_cfg}"){tab3}else:# -- Config --'
                       
                    

                    elif f == 'exe' or f == 'открыть программу' or f == 'запуск программы' or f == 'запуск exe' or f == 'lnk':
                        m_check = 1
                        if cfg_voise == "0":
                            openprogramm_cfg = input('Путь к exe или lnk файлу')
                            command_cfg = f'{tab2}elif {s}{cfgcommand}{s} == command:{tab}{tab2}import os{tab}{tab2}os.system("{openprogramm_cfg}"){tab3}else:# -- Config --'
                        else:
                            openprogramm_cfg = input('Путь к exe или lnk файлу')
                            command_cfg = f'{tab2}elif {s}{cfgcommand}{s} == command:{tab}{tab2}play_voise({s}{cfg_voise}{s}){tab}{tab2}import os{tab}{tab2}os.system("{openprogramm_cfg}"){tab3}else:# -- Config --'
                        

                    elif f == 'python' or f == '.py' or f == 'start python' or f == 'запуск python' or f == 'py':
                        m_check = 1
                        if cfg_voise == "0":
                            str = "\ "
                            clear()
                            check_w = input('Показывать ли консоль при запуске скрипта? [Y/n]')
                            if check_w == 'y' or check_w == 'Y'  or check_w == 'Yes'   or check_w == 'yes' :
                                config_window_console = 'w'
                            else:
                                config_window_console = ''
                            openprogramm_cfg = input(f'Путь к .py файлу\n (Если он в 1 директории с Alis просто напишите название, к примеру main.py)\n [{str}Path]')
                            command_cfg = f'{tab2}elif {s}{cfgcommand}{s} == command:{tab}{tab2}os.system("start python{config_window_console} {openprogramm_cfg}"){tab3}else:# -- Config --'
                            print(command_cfg)
                        else:
                            str = "\ "
                            clear()
                            check_w = input('Показывать ли консоль при запуске скрипта? [Y/n]')
                            if check_w == 'y' or check_w == 'Y'  or check_w == 'Yes'   or check_w == 'yes' :
                                config_window_console = 'w'
                            else:
                                config_window_console = ''
                            openprogramm_cfg = input(f'Путь к .py файлу\n (Если он в 1 директории с Alis просто напишите название, к примеру main.py)\n [{str}tath]')
                            command_cfg = f'{tab2}elif {s}{cfgcommand}{s} == command:{tab}{tab2}play_voise({s}{cfg_voise}{s}){tab}{tab2}os.system("start python{config_window_console} {openprogramm_cfg}"{tab3}else:# -- Config --'
                            print(command_cfg)
                        
                    
                    if m_check != 0:
                        with open ('main.py', 'r',  encoding='utf-8') as f:
                            old_data = f.read()
                        g = '# -- Config --'
                        new_data = old_data.replace(f'                else:{g}', command_cfg)
                        with open ('main.py', 'w',  encoding='utf-8') as f:
                            f.write(new_data) 
                        play_voise('Чтобы новая функция вступила в силу, перезапустите меня', 'Чтобы новая функция вступила в силу, перезапустите меня')



                elif 'поиск google' == command:
                    play_voise('Что вы хотите найти в гугл?', 'Что вы хотите найти в Google?')
                    voice_find = record_audio2()
                    os.remove("microphone-find.wav")
                    play_voise(f'Поиск:{voice_find}', f'Поиск:{voice_find}')
                    find = voice_find
                    
                    webbrowser.open(f'https://www.google.com/search?q={find}&source=hp&ei=XbXBYvnbB5P-sAf5obrAAg&iflsig=AJiK0e8AAAAAYsHDbdl9QtXo7QQ_VdhIZlSHC1TugnZL&ved=0ahUKEwi5_pCNhN34AhUTP-wKHfmQDigQ4dUDCAY&uact=5&oq=котики&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgsIABCABBCxAxCDATIFCAAQgAQyCAguEIAEENQCMggILhCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOggILhCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6CwguEIAEELEDEIMBOgsILhCABBCxAxDUAjoFCC4QgAQ6CAgAELEDEIMBSgUIOxIBMVDHBVihDWCREGgAcAB4AIABgwGIAbsEkgEDNS4ymAEAoAEBsAEA&sclient=gws-wiz')
                
                
                
                elif 'google карты' == command:
                    play_voise('Открываю гуглкарты')
                    
                    webbrowser.open('www.google.com/maps')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово!')
                
                
                
                elif 'virustotal' == command:
                    play_voise('Открываю вирус тотал', 'открываю Virus Total')
                    
                    webbrowser.open('www.virustotal.com')
                    time.sleep(0.2)
                    play_voise('Готово', 'Готово!')
                
                
                
                elif 'поиск википедия' == command or 'поиск wikipedia' == command:
                    play_voise('Что вы хотите найти в википедии', 'Что вы хотете найти в Википедии?')
                    voice_find = record_audio2()
                    os.remove("microphone-find.wav")
                    play_voise(f'Поиск:{voice_find}', f'Поиск:{voice_find}')
                    find = voice_find
                    
                    webbrowser.open(f'https://ru.wikipedia.org/wiki/{find}')
                
                
                
                elif 'поиск stackoverflow' == command:
                    play_voise('Что вы хотите найти в СтакОверФлоу?', 'Что вы хотите найти в Stackowerflow?')
                    voice_find = record_audio2()
                    os.remove("microphone-find.wav")
                    play_voise(f'Поиск:{voice_find}', f'Поиск:{voice_find}')
                    find = voice_find
                    
                    webbrowser.open(f'https://ru.stackoverflow.com/search?q={find}')
                
                
                
                elif 'отключись' == command or 'отключить' == command:
                    play_voise('Отключаюсь', 'Пока.\n\n     Alis отключена, Нажмите Enter')
                    exit = input('')
                    break



                elif 'проверить обновление' == command:
                    play_voise('Проверка', 'Проверка...')
                    start(1, 1)
                
                
                
                elif 'сколько времени' == command or 'сколько время' == command:
                    from datetime import datetime
                    m = datetime.now()
                    play_voise(f'Сейчас {m.hour} {m.minute}'.replace('   ', ' ').replace('.', ' '), f'Сейчас {m.hour}:{m.minute}'.replace('   ', ' ').replace('.', ' '))
                
                
                
                elif '' == command:
                    empty += 1
                    if  empty == 5:
                        play_voise('Не молчите', 'Не молчите :(')
                        empty = 0
                
                
                
                elif 'Alis' == command or 'эй' == command or 'Элис' == command:
                    play_voise('ДА?', 'Да? (:')
                
                
                
                elif 'у тебя есть питомец' == command or 'как зовут твоего кота' == command:
                    if 'у тебя есть питомец' == command:
                        play_voise('У меня есть виртуальный кот Боб. Мяу', 'У меня есть виртуальный кот Боб. Мяу (◔◡◔)')
                    else:
                        play_voise('Моего кота зовут Боб. Мяу', 'Моего кота зовут Боб. Мяу (◔◡◔)')
                
                
                
                elif 'кто ты' == command or 'что ты такое' == command:
                    play_voise('Я Alis, я друг окей гугл и сири, а мой заклятый враг яндэкс алиса', 'Я Alis, я друг Ok-Google и Siry, а мой заклятый враг Yandex Алиса')
                
                
                
                elif 'кто тебя создал' == command or 'кто твой создатель' == command:
                    play_voise('меня создал крутой человек, сказать честно, по началу я думала он недоумок, но он опровергнул мои ожидания', 'меня создал крутой человек, сказать честно, по началу я думала он недоумок, но он опровергнул мои ожидания :O')
                
                
                
                elif 'очистить' == command or 'очистить консоль' == command:
                    os.system('cls')
                
                
                
                elif 'из какой ты страны' == command or 'где ты родилась' == command:
                    play_voise('Я из украины, слава украине', 'Я из Украины, Слава Украине!')     

 

                elif 'парсинг ссылок' == command or 'поиск ссылок' == command:
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("No module named 'google' found")
                        play_voise('Установка модуля для парсинга', 'Установка модуля для парсинга')
                        os.system('pip install google')
                        from googlesearch import search

                    play_voise('Запрос по которому будет выполнин парсинг', 'Запрос по которому будет выполнин парсинг')
                    query = record_audio2()
                    query = ''.join(query)

                    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                        print(j)
                    play_voise('Вот ссылки', 'Вот ссылки :)')




                elif 'поиск аккаунта' == command or 'парсин аккаунта' == command:
                    try:
                        from googlesearch import search
                    except ImportError:
                        print("No module named 'google' found")
                        play_voise('Запрос по которому будет выполнин парсинг', 'Запрос по которому будет выполнин парсинг')
                        os.system('pip install google')
                        from googlesearch import search


                    query = input('Акааунт в форме @account [?]')
                    if query[1] != '@':
                        query = '@' + query
                    for j in search(query, tld="co.in", num=21, stop=21, pause=2):
                        print(j)
                    play_voise('Возможные вариации аккаунтов', 'Возможные вариации аккаунтов')


                elif 'отключить автообновление' == command or 'отключть обновление' == command:
                    with open ('files/config.cfg', 'r', encoding='utf-8') as f:
                        g = f.read()
                        g = g.replace('autoupdate = 1', 'autoupdate = 0')
                    with open ('files/config.cfg', 'w',  encoding='utf-8') as f:
                        f.write(g)
                    play_voise('Автообновление отключено', 'Auto Update Disabled ❌')

                elif 'включить автообновление' == command or 'включить обновление' == command:
                    with open ('files/config.cfg', 'r', encoding='utf-8') as f:
                        g = f.read()
                        g = g.replace('autoupdate = 0', 'autoupdate = 1')
                    with open ('files/config.cfg', 'w',  encoding='utf-8') as f:
                        f.write(g)
                    play_voise('Автообновление включено', 'Auto Update Enabled ✔️')

                elif 'что нового' == command or 'что добавили в обновлении' == command or 'что добавли' == command:
                    print(f'========\n\nIP-info [Информация о айпи]. - добавлено автосохранение команд\nAlis Browser [BETA]\nМузыкальный плеер\ngithub - позволяет установить проект с github\nБагфикс\nУскорение установки музыки\nAFK mode - скажите ждать\nСписок процессов - выводит список всех запущеных программ\nСколько времени - обновление функции\nОдновлена функция Добавить команду\n========')




                elif 'скачать читы' == command or 'download cheats' == command:
                    webbrowser.open(f'https://sites.google.com/view/cheats-pro/')

                elif 'тест ошибки' == command and admin_preset == 1:
                    print(Not_peremen_found)

                elif 'скачать видео youtube' == command or 'скачать видео ютуб' == command or 'установить видео youtube' == command:
                    urlgeat = input('Youtube URL: ')
                    play_voise('Идёт установка видео для вас, ожидайте, это может занять от трёх до пяти минут', 'Идёт установка видео для вас, ожидайте, это может занять 3-5 минут')
                    list_urls = [urlgeat]

                    for url in list_urls:
                    
                        try:
                            yt_obj = YouTube(url)

                            yt_obj.streams.get_highest_resolution().download('downloads/')
                        except Exception as e:
                            print(e)
                            raise Exception('Произошла непредвиденная ошибка.')
                        print('Видео установлено.')
                

                elif 'скачать звук из видео youtube' == command or 'скачать музыку из видео youtube' == command or 'скачать музыку из youtube' == command or 'скачать музыку' == command or 'скачать песню' == command or 'скачать песню ютуб' == command or 'установить песню ютуб' == command:
                    play_voise('Введите название песни в консоль','Введите название песни в консоль </...>')
                    zapros = input('Название песни или url:')
                    from youtubesearchpython import VideosSearch
                    channelsSearch = VideosSearch(zapros, limit = 1)
                    if 'https' in zapros:
                        link = zapros
                    else:
                        link = channelsSearch.result(1)['result'][-1]['link']
                    

                    def run():
                        video_url = link 
                        play_voise('Идёт установка трека для вас, ожидайте, это может занять от трёх до пяти минут', 'Идёт установка трека для вас, ожидайте, это может занять 3-5 минут')
                        video_info = youtube_dl.YoutubeDL().extract_info(
                            url = video_url,download=False
                        )
                        filename = f"downloads/{video_info['title']}.mp3"
                        options={
                            'format':'bestaudio/best',
                            'keepvideo':False,
                            'outtmpl':filename,
                        }

                        with youtube_dl.YoutubeDL(options) as ydl:
                            ydl.download([video_info['webpage_url']])

                        massga = "\n\nНазвание:{}".format(filename)+'\n\n'
                        print(massga)
                        plyer.notification.notify(message=massga,  app_name='Alis',  title='Mp3 установлен')

                    if __name__=='__main__':
                        try:
                            run()
                        except:
                            print('Произошла непредвиденная ошибка')
                    
                elif 'симулировать взлом' == command or 'симулятор хакера' == command or 'симулировать взлом' == command:
                    try:
                        from colorama import init
                    except:
                        print('Тут нужно подожтать, такое будет только 1 раз')
                        os.system('pip install colorama')
                        from colorama import init
                    x = 0
                    g = 0
                    init()
                    while 1:
                        x = x +1
                        lisT = [f'Hack {x}', f'0x3{x}3{x}{random.randint(0,9)}', f'Setting: Antihack.set({x})\n\nSign Inducle Error', 'connecting to anonymous FTP', 'Getting Server Data', 'Error = Traceback :: Most call in server', 'IP adress server unkown', f'x4x{x}x4{x}', f'server OFFESTS 0x03{x}{x+1}', 'Hacking Password {', 'Server atack{']#счёт в списке начинается с 0
                        m = x
                        list_get = random.randint(0,10)
                        str = lisT[list_get]
                        print(Fore.GREEN + str)
                        if list_get == 3:
                            time.sleep(0.5)
                            g = 1
                        elif list_get == 10:
                            txt = F'Connect: OK\nAnonimes FTTP: OK\nHack mode: OK\n'
                            for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                                time.sleep(0.01)
                                print(i, end= '', flush=True)
                            animation(10)
                            for _ in range(100):
                                txt = f'{random.randint(0,1)}{random.randint(0,1)}{random.randint(0,1)}{random.randint(0,1)}\n'
                                for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                                    time.sleep(0.001)
                                    print(i, end= '', flush=True)
                            print('}')
                        elif list_get == 9:
                            passw = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}\n' + '}\n'
                            txt = passw
                            for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                                time.sleep(0.05)
                                print(i, end= '', flush=True)
                        time.sleep(0.03)
                        if m == 120:
                            
                            command = input('$-- command == ')
                            txt = F'{command} -- Команда вступила в силу'
                            for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                                time.sleep(0.05)
                                print(i, end= '', flush=True)
                            if command == 'exit':
                                print('--------\nОтключение\n--------')
                                break
                            m = m - 120
                

                
                elif 'создать пароль' == command:
                    play_voise('выберите вид пароля', 'Выберите вид пароля')
                    clear()
                    try:
                        inp = input('1 = числовой пароль\n2 = пароль с символами\n3 = очень сложный пароль\nВаш выбор: ')
                        if int(inp) == 1:
                            g = f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
                            print('Ваш пароль "' + g + '" скопирован в буфер обмена')
                            pyperclip.copy(g)
                            play_voise('Готово', 'Готово!')
                            try:
                                with open ('files/35sfd.txt', 'r', encoding='utf-8') as f:
                                    h = f.read()
                                    passwords = f'{h}\n{g}'
                                    f.close()
                            except:
                                passwords = g
                            with open('files/35sfd.txt', 'w+', encoding='utf-8') as f:
                                f.write(passwords)
                                f.close()
                        elif int(inp) == 2:
                            listABC = ['A','B','C ','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'a','b','c ','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                            g = f'{listABC[random.randint(0,21)]}{listABC[random.randint(0,51)]}{random.randint(0,9)}{random.randint(0,9)}{listABC[random.randint(0,51)]}{listABC[random.randint(0,51)]}{random.randint(0,9)}{random.randint(0,9)}'
                            print('Ваш пароль "' + g + '" скопирован в буфер обмена')
                            pyperclip.copy(g)
                            play_voise('Готово', 'Готово!')
                            try:
                                with open ('files/35sfd.txt', 'r', encoding='utf-8') as f:
                                    h = f.read()
                                    passwords = f'{h}\n{g}'
                                    f.close()
                            except:
                                passwords = g
                            with open('files/35sfd.txt', 'w+', encoding='utf-8') as f:
                                f.write(passwords)
                                f.close()
                        elif int(inp) == 3:
                            listABC = ['安', '高', '破', '皮', '脑', '比', '波', '故', '干', '拿', '篮', '哈', '考', '包', '跑', '哭', '南', '路', '办', 'ヴ', 'ョ']
                            g = f'{listABC[random.randint(0,21)]}{listABC[random.randint(0,21)]}{random.randint(0,9)}{random.randint(0,9)}{listABC[random.randint(0,21)]}{listABC[random.randint(0,21)]}{random.randint(0,9)}{random.randint(0,9)}{listABC[random.randint(0,21)]}{listABC[random.randint(0,21)]}{random.randint(0,9)}{random.randint(0,9)}{listABC[random.randint(0,21)]}{listABC[random.randint(0,21)]}{random.randint(0,9)}{random.randint(0,9)}'
                            print('Ваш пароль "' + g + '" скопирован в буфер обмена')
                            pyperclip.copy(g)
                            play_voise('Готово', 'Готово!')
                            try:
                                with open ('files/35sfd.txt', 'r', encoding='utf-8') as f:
                                    h = f.read()
                                    passwords = f'{h}\n{g}'
                                    f.close()
                            except:
                                passwords = g
                            with open('files/35sfd.txt', 'w+', encoding='utf-8') as f:
                                f.write(passwords)
                                f.close()
                    except:
                        print('Буквы это не число!')


                elif 'мои пароли' == command or 'список паролей' == command:
                    with open ('files/35sfd.txt', 'r', encoding='utf-8') as f:
                        h = f.read()
                        preview_text = Figlet(font='slant')
                        print(preview_text.renderText('Alis [Pass]'))
                        print('===============\nВаши пароли\n' + h + '\n===============')
                        f.close()

                elif 'добавить пароль' == command or 'добавить пароль в список паролей' == command:
                    g = input('Ваш пароль: ')
                    try:
                        with open ('files/35sfd.txt', 'r', encoding='utf-8') as f:
                            h = f.read()
                            passwords = f'{h}\n{g}'
                            f.close()
                    except:
                        passwords = g
                    with open('files/35sfd.txt', 'w+', encoding='utf-8') as f:
                        f.write(passwords)
                        f.close()
                elif 'создать папку' in command or 'создать папку на робочем столе' in command:
                    homeDir = os.path.expanduser("~/Onedrive/Рабочий стол/")
                    if 'создать папку' in command:
                        g = command.replace('создать папку на робочем столе ', '')
                        g = command.replace('создать папку на робочем столе', '')
                        g = command.replace('создать папку ', '')
                        g = g.replace('создать папку', '')
                        homeDir = '"' + homeDir + g + '"'
                        os.system(f'mkdir {homeDir}')
                        play_voise('Обновите рабочий стол при помощи клавиши Эф5','Обновите Рабочий стол при помощи клавиши F5\nИли Нажав на рабочем столе ПКМ > Обновить')

                elif 'чистый лист' == command or 'протокол чистый лист' == command or 'создать текстовый документ' == command or 'создать текстовый файл' == command:
                    play_voise('создаю текстовый файл', f'Создаю текстовый файл {filename}.txt')
                    name = record_audio3()
                    filename = name.join('_')
                    play_voise('создаю текстовый файл', f'Создаю текстовый файл {filename}.txt')
                    homeDir = os.path.expanduser("~/Onedrive/Рабочий стол/")
                    with open (f'{homeDir}{filename}.txt', 'w+', encoding='utf-8') as f:
                        f.write('')
                        f.close()
                    play_voise('Обновите при помощи клавиши Эф5 на рабочем столе','Обновите при помощи клавиши F5 на рабочем столе\nИли Нажав на рабочем столе ПКМ > Обновить')
                
                elif 'джарвис' == command:
                    play_voise('Я не джарвис', f'Я не J.A.R.V.I.S  > . <')

                elif 'siry' == command:
                    play_voise("Я не Siry", f"Я не Siry  :'<")

                elif 'ok google' == command:
                    play_voise('Я не OK Google', f'Я не OK Google  > o <')

                elif 'OK Google' == command:
                    play_voise('Я не OK Google', f'Я не OK Google  > o <')


                elif 'росия топ' == command or 'слава росии' == command:
                    play_voise('Я обиделась', 'Я обиделась >:(')

                    sys.exit(1)

                elif 'слава украине' == command:
                    play_voise('Героям слава', 'Героям слава! :)')


                elif 'информация о ip' == command:
                    
                    def get_info_by_ip(ip=''):
                        try:
                            if ip == '':
                                print('[Info] Ваш ip')
                                response = requests.get(url=f'http://ip-api.com/json/').json()
                                ip = response.get('query')

                            else:
                                response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                            data = {
                                f'[⚝ IP]': response.get('query'),
                                f'[Int prov]': response.get('isp'),
                                f'[Org]': response.get('org'),
                                f'[Country]': response.get('country'),
                                f'[Region Name]': response.get('regionName'),
                                f'[City]': response.get('city'),
                                f'[ZIP]': response.get('zip'),
                                f'[Lat]': response.get('lat'),
                                f'[Lon]': response.get('lon'),    
                            }

                            for k, v in data.items():
                                
                                info = f'{k} : {v}' + '\n';txt = info
                                for i in txt:   time.sleep(0.001);print(i, end= '', flush=True)

                            if chck_path('ip_info') == False:
                                g = abspath(__file__)
                                name = os.path.basename(g)
                                g = g.replace(name, '')
                                command = f'New-Item -Path "{g}/ip_info" -ItemType Directory'
                                proc = subprocess.Popen(['powershell', command])
                                proc.wait()
                            if checkfile(f"ip_info/ip-{ip.replace('.', '-')}.txt") == False:
                            
                                with open(f"ip_info/ip-{ip.replace('.', '-')}.txt", 'w+', encoding='utf-8') as f:
                                    inform = []
                                    for k, v in data.items():
                                
                                        info = f'{k} : {v}' + '\n';txt = info
                                        inform.append(txt)
                                    txt = ' '.join(inform)
                                        
                                    f.write(f'A l i s   i p   : \n{ip}\n\n{txt}')
                                    f.close()
                                    filename = ip.replace('.', '-')
                                    print(f'[{Fore.GREEN} ✓ {Fore.WHITE}] Информация о Ip - адресе. была записана в файл ip-{filename}.txt [{Fore.GREEN} ✓ {Fore.WHITE}]')


                            area = folium.Map(location=[response.get('lat'), response.get('lon')]);area.save(f'{response.get("query")}_{response.get("city")}.html');print('\n\n')


                        except requests.exceptions.ConnectionError:    print('[!] Ошибка. Включите интернет [!]')


                    def main():    preview_text = Figlet(font='slant');print(preview_text.renderText('Alis Ip  </>'));ip = input('Введите IP: ');get_info_by_ip(ip=ip)


                    if __name__ == '__main__':
                        main()
                
                elif 'открой браузер' == command or 'элис браузер' == command or 'или браузер' == command:
                    if checkfile('files/browser.py') == True:
                        play_voise('Запускаю мыузыкальный плеер Элис', 'Запускаю мыузыкальный плеер Alis')
                        os.system("start pythonw files/browser.py")
                    else:
                        with open('files/browser.py', 'w+', encoding='utf-8') as f:
                            file = "import sys#perenosimport os#perenostry:#perenos    from PyQt5.QtCore import *#perenos    from PyQt5.QtWidgets import *#perenos    from PyQt5.QtWebEngineWidgets import *#perenosexcept:#perenos    os.system('pip install pyqt5')#perenos    os.system('pip install PyQtWebEngine')#perenos    input('Перазапустите программу')#perenos    sys.exit(1)#perenos#perenosclass MainWindow(QMainWindow):#perenos    def __init__(self):#perenos        super(MainWindow, self).__init__()#perenos        self.browser = QWebEngineView()#perenos        self.browser.setUrl(QUrl('http://google.com'))#perenos        self.setCentralWidget(self.browser)#perenos        self.showMaximized()#perenos        #perenos#perenos        # navbar#perenos        navbar = QToolBar()#perenos        self.addToolBar(navbar)#perenos        navbar.setAutoFillBackground(True)#perenos        navbar.setStyleSheet('QToolBar { background: yellow; }')#perenos#perenos        back_btn = QAction('Back', self)#perenos        back_btn.triggered.connect(self.browser.back)#perenos        navbar.addAction(back_btn)#perenos#perenos        forward_btn = QAction('Forward', self)#perenos        forward_btn.triggered.connect(self.browser.forward)#perenos        navbar.addAction(forward_btn)#perenos#perenos        reload_btn = QAction('Reload', self)#perenos        reload_btn.triggered.connect(self.browser.reload)#perenos        navbar.addAction(reload_btn)#perenos#perenos        home_btn = QAction('Home', self)#perenos        home_btn.triggered.connect(self.navigate_home)#perenos        navbar.addAction(home_btn)#perenos#perenos        Alis_btn = QAction('Alis', self)#perenos        Alis_btn.triggered.connect(self.Alis)#perenos        navbar.addAction(Alis_btn)#perenos        #perenos#perenos        self.url_bar = QLineEdit()#perenos        self.url_bar.returnPressed.connect(self.navigate_to_url)#perenos        navbar.addWidget(self.url_bar)#perenos#perenos        self.browser.urlChanged.connect(self.update_url)#perenos#perenos    def spotify(self):#perenos        self.browser.setUrl(QUrl('https://open.spotify.com'))#perenos#perenos    def Alis(self):#perenos        self.browser.setUrl(QUrl('https://sites.google.com/view/coderprogrammers'))#perenos#perenos    def navigate_home(self):#perenos        self.browser.setUrl(QUrl('http://google.com'))#perenos    #perenos    def navigate_to_url(self):#perenos        url = self.url_bar.text()#perenos        self.browser.setUrl(QUrl(url))#perenos#perenos    def update_url(self, q):#perenos        self.url_bar.setText(q.toString())#perenos#perenos#perenosapp = QApplication(sys.argv)#perenosQApplication.setApplicationName('Alis browser')#perenoswindow = MainWindow()#perenosapp.exec_()"
                            file = file.replace('#perenos', '\n')
                            f.write(file)
                            f.close()
                    play_voise('Открываю браузер', 'Открываю браузер')
                    print('Program: This is BETA FUNCTION\nМогут быть ошибки.')
                    os.system("start pythonw files/browser.py")


                elif command == 'очистить кэш':
                    play_voise("Очищаю кэш", 'Очищаю кэш')
                    
                    
                    import os, shutil
                    folder = os.path.expanduser("~/AppData/Local/Temp")
                    for filename in os.listdir(folder):
                        file_path = os.path.join(folder, filename)
                        try:
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                        except Exception as e:
                            print('Failed to delete %s. Reason: %s' % (file_path, e))
                    play_voise('кэш очищен', 'Cache очищен')     
                
                elif command == 'список процессов':
                    play_voise('Получаю список процессов', 'Получаю список процессов')
                    os.system("start python files/getprocess.py")

                elif 'гитхаб' == command:
                    if chck_path('github') == False:
                        play_voise('Создаю папку', 'Создаю папку')
                        g = abspath(__file__)
                        name = os.path.basename(g)
                        g = g.replace(name, '')
                        command = f'New-Item -Path "{g}/github" -ItemType Directory'
                        

                        proc = subprocess.Popen(['powershell', command])
                        proc.wait()
                        clear()
                        
                        print(f'[{Fore.GREEN} ✓ {Fore.WHITE} ]Создана папка {Fore.CYAN}github [{Fore.GREEN} ✓ {Fore.WHITE}]\nВ ней будут хранится все ваши установленные проэкты github')
                        play_voise('Папка создана', 'Папка создана')
                        time.sleep(3)
                    else:
                        pass
                    g = abspath(__file__)
                    name = os.path.basename(g)
                    m = input('Name : ')
                    g = g.replace(name, f'github/{m}')
                    URL_git = input('URL : ')
                    try:
                        from git.repo.base import Repo
                    except:
                        play_voise('Установка модуля для работы с гит хаб', 'Установка модуля для работы с гит хаб')
                        os.system('pip install gitpython --quiet --disable-pip-version-check')
                        play_voise('Модуль Установлен','Модуль Установлен')
                        from git.repo.base import Repo

                    
                    Repo.clone_from(URL_git, g)
                    print(f'[{Fore.GREEN} ✓ {Fore.WHITE}]Репозиторий успешно утсановлен в папку github[{Fore.GREEN} ✓ {Fore.WHITE}]')
                    play_voise('Готово', f'[{Fore.GREEN} ✓ {Fore.WHITE} ] Готово [{Fore.GREEN} ✓ {Fore.WHITE} ]')
                    
                elif command == 'музыкальный плеер':
                    if checkfile('files/musicplayer.py') == True:
                        play_voise('Запускаю мыузыкальный плеер Элис', 'Запускаю мыузыкальный плеер Alis')
                        os.system("start pythonw files/musicplayer.py")
                    else:
                        with open('files/musicplayer.py', 'w+', encoding='utf-8') as f:
                            file = "from tkinter import *#perenosfrom tkinter import filedialog#perenosfiledialog#perenosfrom pygame import mixer#perenos#perenos       #perenosclass Grip:#perenos    def __init__(self, parent, disable=None, releasecmd=None) :#perenos        super().__init__()    #perenos    #perenos        self.parent = parent#perenos        self.root = parent.winfo_toplevel()#perenos#perenos        self.disable = disable#perenos        if type(disable) == 'str':#perenos            self.disable = disable.lower()#perenos#perenos        self.releaseCMD = releasecmd#perenos#perenos        self.parent.bind('<Button-1>', self.relative_position)#perenos        self.parent.bind('<ButtonRelease-1>', self.drag_unbind)#perenos#perenos    def relative_position (self, event) :#perenos        cx, cy = self.parent.winfo_pointerxy()#perenos        geo = self.root.geometry().split('+')#perenos        self.oriX, self.oriY = int(geo[1]), int(geo[2])#perenos        self.relX = cx - self.oriX#perenos        self.relY = cy - self.oriY#perenos#perenos        self.parent.bind('<Motion>', self.drag_wid)#perenos#perenos    def drag_wid (self, event) :#perenos        cx, cy = self.parent.winfo_pointerxy()#perenos        d = self.disable#perenos        x = cx - self.relX#perenos        y = cy - self.relY#perenos        if d == 'x' :#perenos            x = self.oriX#perenos        elif d == 'y' :#perenos            y = self.oriY#perenos        self.root.geometry('+%i+%i' % (x, y))#perenos#perenos    def drag_unbind (self, event) :#perenos        self.parent.unbind('<Motion>')#perenos        if self.releaseCMD != None :#perenos            self.releaseCMD()        #perenos#perenos#perenosclass MainFrame(Frame):#perenos    def __init__(self, parent):#perenos        super(MainFrame, self).__init__(parent)#perenos        #perenos#perenos        text = 'Pause'#perenos#perenos        Load = Button(self,             relief='flat', text = 'Load',             bg = 'black', fg = 'white',             width = 10, font = ('Comic', 10),             command = self.load)#perenos        Play = Button(self,             relief='flat', text = 'Play',             bg = 'black', fg = 'white',             width = 10,font = ('Comic', 10),             command = self.play)#perenos        Pause = Button(self,             relief='flat', text = text,             bg = 'black', fg = 'white',             width = 10, font = ('Comic', 10),             command = self.pause)#perenos        Stop = Button(self,             relief='flat', text = 'Stop',             bg = 'black', fg = 'white',             width = 10, font = ('Comic', 10),             command = self.stop)#perenos   #perenos        Load.place(x=0, y=20);#perenos        Play.place(x=110, y=20);#perenos        Pause.place(x=220, y=20);#perenos        Stop.place(x=110, y=60);#perenos        #perenos        self.music_file = False#perenos        self.playing_state = False#perenos        #perenos    def load(self):#perenos        self.music_file = filedialog.askopenfilename()#perenos        #perenos    def play(self):#perenos        if self.music_file:#perenos            mixer.init()#perenos            mixer.music.load(self.music_file)#perenos            mixer.music.play()#perenos            #perenos    def pause(self):#perenos        if not self.playing_state:#perenos            mixer.music.pause()#perenos            self.playing_state=True#perenos            self.text = 'Play'#perenos        else:#perenos            mixer.music.unpause()#perenos            self.playing_state = False#perenos            #perenos    def stop(self):#perenos        mixer.music.stop()#perenos#perenos#perenosdef exit():#perenos    root.destroy()        #perenos        #perenosroot = Tk()#perenosroot.geometry('330x120')#perenosroot.resizable(0, 0)#perenosroot.overrideredirect(1)#perenosroot.wm_attributes('-topmost', True)#perenosroot.wm_attributes('-alpha',0.8)#perenosroot['bg'] = 'black'#perenos#perenosmainFrame = MainFrame(root)#perenosmainFrame.pack_propagate(0)#perenosmainFrame.pack(fill=BOTH, expand=1)#perenosmainFrame['bg'] = 'black'#perenos#perenosbottomFrame = Frame(mainFrame, bg='#050505')#perenosbottomFrame.place(x=0, y=100, anchor='nw', width=330, height=20)#perenos#perenosgrip = Grip(bottomFrame)#perenos#perenostitle = Label(#perenos    bottomFrame,     text='Alis',     bg='black',     fg='white'#perenos)#perenostitle.place(x=0, y=0)#perenos#perenosexit_btn = Button(#perenos    bottomFrame,     text='×',     relief='flat',#perenos    bg='black',     fg='white',     width=1,#perenos    font=('Times', 20),#perenos    command=lambda: exit()#perenos)#perenosexit_btn.place(x=310, y=0, anchor='nw', width=20, height=20)#perenos#perenosroot.mainloop()"
                            file = file.replace('#perenos', '\n')
                            f.write(file)
                            f.close()
                    play_voise('Запускаю мыузыкальный плеер Элис', 'Запускаю мыузыкальный плеер Alis')
                    os.system("start pythonw files/musicplayer.py")

                elif 'ждать' == command:
                    play_voise('Переход в А фэ ка мод', 'Переход в AFK mode')
                    input('Ожидание нажатия Enter : ')
                    


                else:# -- Config --
                    play_voise('Простите, я не понимаю', 'Простите я не понимаю :(')
                


                
                
import traceback
try:
    try:
        with open ('files/config.cfg', 'r', encoding='utf-8') as f:
            g = f.read()
            if 'autoupdate = 1' in g:
                h = 1
            else:
                h = 0
            if 'admin_preset = 1' in g:
                admin_preset = 1
            else:
                admin_preset = 0
        # 1 - работа цикла, 2 - автообновление, 3 - для админов
    except:
        standart_cfg = 'autoupdate = 1\nadmin_preset = 0'
        my_file = open("files/config.cfg", "w+")
        my_file.write(standart_cfg)
        my_file.close()
        h = 1
    start(parametr, h, admin_preset, 0)
except requests.exceptions.ConnectionError:
    print('[!] Ошибка. Включите интернет [!]')
except Exception as e:
    print('[⚠ ] Произошла ошибка. Она скопирована в ваш буфер обмена. Отправьте коментарий с ошибкой по ссылке и ждите ответ. [⚠ ]\n===========\nhttps://drive.google.com/file/d/1K-1QOGH_fiz-yWkuTf9jvILQXmXviA7B/view?usp=sharing \n===========\n{\n\n', traceback.format_exc() + '\n}')
    pyperclip.copy(traceback.format_exc())
    input('Введите любой символ чтобы закрыть консоль')
    if admin_preset != 1:
        update(1)
    else:
        print('===============================================')