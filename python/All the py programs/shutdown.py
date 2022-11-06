from logging import shutdown
import os
import pyttsx3
sec = 10
os.system(f'shutdown /s /t {sec}')
pyttsx3.speak('bye bye')