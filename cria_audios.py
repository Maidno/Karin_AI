from gtts import gTTS
from playsound import playsound

def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/comando_invalido.mp3')
    playsound('audios/comando_invalido.mp3')

cria_audio('você pode tentar novamente !')
