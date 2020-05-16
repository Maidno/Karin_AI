
import speech_recognition as sr
from playsound import playsound
from requests import get  # Aqui eu faço o get do site em questão
from bs4 import BeautifulSoup #Aqui eu faço o tratamento dos dados
from gtts import gTTS
import webbrowser as browser
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

#Configurações
hotword = 'karin'   #E uma inteligênçia artificial que gosta de Animes, séries , e pessoas divertidas

with open('karin-ai-b7527489ec09.json') as credenciais_google:
    credenciais_google = credenciais_google.read()


# FUNÇÕES PRINCIPAIS
def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print('Diga o comando: ')
            audio = microfone.listen(source)

            try:
                trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print('COMANDO: ', trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google Cloud Speech could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
    return trigger

def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save('audios/mensagem.mp3')
    print('Karin: ', mensagem)
    playsound('audios/mensagem.mp3')

def executa_comandos(trigger):
    if 'ultimas noticias' in trigger:
        ultimas_noticias()

    elif 'toca' in trigger and 'Ghost in the shell' in trigger:
        playlists('Ghost_in_the_shell')

    elif 'toca' in trigger and 'Studio ghibli' in trigger:
        playlists('Studio_ghibli')

    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('C. Inválido', mensagem)
        responde('comando_invalido')


## FUNÇÕES DE COMANDOS ##

def ultimas_noticias():
    site = get('http://jovemnerd.com/')
    noticias = BeautifulSoup(site.text, 'html.parser')

    for h2 in noticias.findAll('h2')[:4]:
        mensagem = h2.a.text
        cria_audio(mensagem)

def playlists(playlister):
    if playlister == 'Ghost in the shell':
        browser.open('https://open.spotify.com/playlist/37i9dQZF1DX9v9O7wB8rQi')
    elif playlister == 'Studio ghibli':
        browser.open('https://open.spotify.com/playlist/37i9dQZF1DX7GTqMQDhOum')


def main():
    while True:
        monitora_audio()
main()

