import os
import random

os.chdir("Wallpapers")
wallpaper = os.listdir()
randomizer = random.randint(0, len(wallpaper)-1)
random_wallpaper = wallpaper[randomizer]
way_to_wallpaper = "Image="+os.getcwd()+"/"+random_wallpaper
home_dir = os.path.expanduser("~")
os.chdir(home_dir)
os.chdir(".config")
file_path = "plasma-org.kde.plasma.desktop-appletsrc"

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

os.system("kquitapp5 plasmashell && kstart5 plasmashell &")


