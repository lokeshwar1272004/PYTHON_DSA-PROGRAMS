import speech_recognition as sr
recognition = sr.Recognizer()

def recognition_source():
    with sr.Microphone() as source:
        print("speak")
        recognition.adjust_for_ambient_noise(source)
        audio = recognition.listen(source)

    try:
        text = recognition.recognize_google(audio)
        print("ypu said"+text)
    except sr.UnknownValueError:
        print("not listen")
    except sr.RequestError:
        print("not by google")

recognition_source()

