**DEMONSTRATION HOW SCRIPT IS WORKING (ДЕМОНСТРАЦИЯ КАК РАБОТАЕТ СКРИПТ):**
![Ouups, it's don't work](example.gif)


**ENGLISH LANGUAGE:**

This script was written by a person whose level of knowledge of the language Python proficiency is not very high, so clearly something could have been done better.

**WARNING:**

THE DOCUMENTATION WAS ORIGINALLY WRITTEN IN RUSSIAN AND TRANSLATED INTO ENGLISH USING AN ONLINE TRANSLATOR, SO THE TRANSLATION MAY NOT BE ACCURATE.
**I RECOMMEND READING, IF POSSIBLE, IN THE CREATOR'S NATIVE LANGUAGE** (WHICH IS LOCATED BELOW)

THE SCRIPT WAS CREATED FOR Linux Manjaro (KDE PLASMA), and I am not responsible for its performance on other operating systems or on other distributions.
EVEN IF YOU HAVE A SIMILAR SYSTEM TO MINE, USE IT **AT YOUR OWN RISK.**

**RECOMMENDATION:**

Try to familiarize yourself with the os library first before using the script.
Create your own text document in this folder, then copy the contents of the configuration file that changes this script.
Then comment out the lines (13-38) in the program and add your own to check if what you want is changing. (The wallpaper will not change, because it is just a copy of the configuration file, but you can understand if what is really needed is changing).

Step-by-step guide recommendations:
1) Create a text file - test.txt
2) Open your configuration file (home/username/.config/plasma-org.kde.plasma.desktop-appletsrc) and copy all the contents
3) Paste the copied into test.txt
4) Open main.py and comment out lines (13-38)
5) Enter the following code:
```python
os.chdir("..")
file_path = "test.txt" 

with open(file_path, "r") as f:
    file_contents = f.read()

search_str = 'Image='

with open(file_path) as f:
    for num, line in enumerate(f, 1):
        if search_str in line:
            index = num
            break

new_contents = file_contents.replace(file_contents.split("\n")[index-1], way_to_wallpaper)

with open(file_path, "w") as f:
    f.write(new_contents)
```
6) Check if your test text file changes the content you need.
7) If the result is positive, delete the new lines, and uncomment the lines (13-38)

**DOCUMENTATION:**

This script uses the built-in Python library (os). There is no need to pump anything.

I will conditionally divide the script into several blocks for the convenience of describing the code:

1)  Block No. 1:

This block imports the os library, as well as the built-in random module

```python
import os - Importing the os library
import random - Importing the random module
```

2) Block No. 2:

This block finds and selects a random image from the Wallpapers folder (which is located in the same directory, if you downloaded everything correctly).
It also puts it in a state that allows you to make changes to the configuration file.
```python
os.chdir("Wallpapers") # Go to the Wallpapers folder
wallpaper = os.listdir()    # Finding all the image files that are in the folder. You can also delete/add new images of your choice
randomizer = random.randint(0, len(wallpaper)-1) # Selecting the index of a random single image
random_wallpaper = wallpaper[randomizer] # Selecting this image itself
way_to_wallpaper = "Image="+os.getcwd()+"/"+random_wallpaper # Getting the full name of this image suitable for entering into the config file
```
3) Block No. 3:

This block finds the configuration file itself
```python
home_dir = os.path.expanduser("~") #Go to the home folder
os.chdir(home_dir) # Go to the home folder
os.chdir(".config") # Go to the .config folder
file_path = "plasma-org.kde.plasma.desktop-appletsrc" # Selecting the configuration file itself
```
4) Block No. 4:

Reading, writing and saving a file
```python
with open(file_path, "r") as f: #Reading the file itself
    file_contents = f.read()

search_str = 'Image=' # Finding the part that we will replace

with open(file_path) as f: # Search for the index of the string(the part to be replaced)
    for num, line in enumerate(f, 1):
        if search_str in line:
            index = num
            break

new_contents = file_contents.replace(file_contents.split("\n")[index-1], way_to_wallpaper) # Changing this line to a line containing our image

with open(file_path, "w") as f: # Saving file changes
    f.write(new_contents)

os.system("kquitapp5 plasmashell && kstart5 plasmashell &") # Restarting the desktop
```
Created by a beginner in programming, and in python in particular - NaiNaniNai



**RUSSIAN LANGUAGE (РУССКИЙ ЯЗЫК):**

Этот скрипт был написан человеком, чьи уровень знания языка Питон чуть выше плинтуса, поэтому явно что-то можно было сделать лучше.

**ПРЕДУПРЕЖДЕНИЕ:**

СКРИПТ БЫЛ СОЗДАН ДЛЯ Linux Manjaro (KDE PLASMA), и я не отвечаю за его работоспособность на других операционных системах или на других дистрибутивах.
ДАЖЕ ЕСЛИ У ВАС СХОЖАЯ СИСТЕМА С МОЕЙ, ТО ИСПОЛЬЗУЙТЕ **НА СВОЙ СТРАХ И РИСК.**

**РЕКОМЕНДАЦИЯ:**

Попробуйте сперва ознакомиться с библиотекой os перед использованием скрипта.
Создайте собственный текстовый документ в этой папке, затем скопируйте содержимое конфигурационного файла, который меняет этот скрипт.
Затем в программе закомментируйте строки (13-38) и добавьте свои, чтобы проверить меняется ли то, что вы хотите. (Обои не поменяются, поскольку это просто копия конфигурационного файла, но за то вы можете понять меняется ли то, что действительно надо).

Поэтапный гайд рекомендации:
1) Создайте текстовый файл - test.txt
2) Откройте свой конфигурационный файл (home/имяпользователя/.config/plasma-org.kde.plasma.desktop-appletsrc) и скопируйте все содержимое
3) Вставьте скопированные в test.txt
4) Откройте main.py и закомментируйте строки (13-38)
5) Внесите следующий код:
```python
os.chdir("..")
file_path = "test.txt" 

with open(file_path, "r") as f:
    file_contents = f.read()

search_str = 'Image='

with open(file_path) as f:
    for num, line in enumerate(f, 1):
        if search_str in line:
            index = num
            break

new_contents = file_contents.replace(file_contents.split("\n")[index-1], way_to_wallpaper)

with open(file_path, "w") as f:
    f.write(new_contents)
```
6) Проверьте меняет ли ваш тестовый текстовый файл нужное вам содержимое.
7) При положительном результате, удалите новые строчки, и раскомментируйте строки (13-38)

**ДОКУМЕНТАЦИЯ:**

Данный скрипт использует встроенную библиотеки Python'а (os). Ничего докачивать не надо.

Скрипт условно разделю на несколько блоков для удобства описания кода:

1) Блок №1:

Этот блок импортирует библиотеку os, а также встроенный модуль random
```python
import os  - Импортирование библиотеки os
import random - Импортирование модуля random
```
2) Блок №2:

Этот блок находит и выбирает случайное изображение из папки Wallpapers(которая находится в этом же каталоге, если вы все правильно скачали).
Также приводит его в состояние, позволяющего внести изменения в конфигурационный файл.
```python
os.chdir("Wallpapers")  # Переход в папку Wallpapers
wallpaper = os.listdir()    # Нахождение всех файлов изображения, что находятся в папке. Вы также можете удалить/добавить новые изображения на свой выбор
randomizer = random.randint(0, len(wallpaper)-1) # Выбор индекса случайного одного изображения
random_wallpaper = wallpaper[randomizer] # Выбор самого этого изображения
way_to_wallpaper = "Image="+os.getcwd()+"/"+random_wallpaper # Получение полного названия этого изображения, подходящего для внесения в конфиг-файл
```
3) Блок №3:

Этот блок находит сам конфигурационный файл
```python
home_dir = os.path.expanduser("~") # Переход в домашнюю папку
os.chdir(home_dir) # Переход в домашнюю папку
os.chdir(".config") # Переход в папку .config
file_path = "plasma-org.kde.plasma.desktop-appletsrc" # Нахождние конфигурационного файла
```
4) Блок №4:

Чтение, запись и сохранение файла
```python
with open(file_path, "r") as f: #Чтение самого файла
    file_contents = f.read()

search_str = 'Image=' # Поиск части, которую мы будем заменять

with open(file_path) as f: #Поиск индекса строки(части,которую нужно заменить)
    for num, line in enumerate(f, 1):
        if search_str in line:
            index = num
            break

new_contents = file_contents.replace(file_contents.split("\n")[index-1], way_to_wallpaper)  # Изменение этой строки на строку, содержающую наше изображение

with open(file_path, "w") as f:  # Сохранение изменений файла
    f.write(new_contents)

os.system("kquitapp5 plasmashell && kstart5 plasmashell &") # Перезапуск рабочего стола
```
Создано новичком в программировании, и в частности питоне - NaiNaniNai
