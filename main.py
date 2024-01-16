#импорты
from gtts import gTTS
import os
#спрашиватель
a= input("название файла/file name ")
x = input("введите текст/text ")
#проверка
b = (a)+".mp3"
print(b)
c = "start "+(b)
#сохранение/save
audio = gTTS(text=x,
             lang="ru",
             slow=False)
audio.save(b)
