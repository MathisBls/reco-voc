import speech_recognition as sr
import pyautogui

r = sr.Recognizer()

# Utilisation du microphone par défaut
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)

    # Détection de seuil
    r.energy_threshold = 500

    while True:
        print("Dites quelque chose...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='fr-FR', show_all=False)
            print(text)

            for word in text.split():
                if word == "droite":
                    pyautogui.keyDown('d')
                elif word == "saute":
                    pyautogui.keyDown('a')
                else:
                    pass

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))
