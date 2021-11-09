import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
output = ''
wikipedia.set_lang('fr')

def analyze():
    global output
    if "qui est " in output:
        output = output.replace("qui est ", "")
        try:
            print(wikipedia.summary(output, sentences=1))
        except Exception as e:
            print(e)
    if "qu'est-ce qu" in output:
        output = output.replace("qu'est-ce qu", "")
        for i in output:
            if i != ' ':
                output = output[1:]
            else:
                output = output[1:]
                break
        print(output)
        try:
            print(wikipedia.summary(output, sentences=1))
        except Exception as e:
            print(e)

with sr.Microphone() as source:
    print ('Listening...')
    audio = listener.listen(source, phrase_time_limit = 3)
    try:
        output = listener.recognize_google(audio, language='fr-FR')
        print(f"Heard : {output}")
    except:
        print('Couldn\'t recognize what tf you said')

analyze()
