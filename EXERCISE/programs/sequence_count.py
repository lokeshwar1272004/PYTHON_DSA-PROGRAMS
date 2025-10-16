import speech_recognition as sr

recognizer = sr.Recognizer()


def recognize_speech_from_mic():
 with sr.Microphone() as source:
  print("Please speak something...")
  recognizer.adjust_for_ambient_noise(source)
  audio = recognizer.listen(source)

  try:
   text = recognizer.recognize_google(audio)
   print("You said: " + text)
  except sr.UnknownValueError:
   print("Sorry, I could not understand the audio.")
  except sr.RequestError:
   print("Could not request results from Google Speech Recognition service.")


# Call the function
recognize_speech_from_mic()


