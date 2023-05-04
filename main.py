import os
import random


# Choose random image
os.chdir("Wallpapers")  # Download the entire directory, otherwise this command will not work for you
wallpaper = os.listdir()    # This command find all files(image) in folder "Wallpapers", you can change the images in Folder, if you want.
randomizer = random.randint(0, len(wallpaper)-1)
random_wallpaper = wallpaper[randomizer]
way_to_wallpaper = "Image="+os.getcwd()+"/"+random_wallpaper

# Search for the file responsible for the current desktop wallpaper
home_dir = os.path.expanduser("~")
os.chdir(home_dir)
os.chdir(".config")
file_path = "plasma-org.kde.plasma.desktop-appletsrc" # Selecting the configuration file itself

# Reading the file itself
with open(file_path, "r") as f:
    file_contents = f.read()

search_str = 'Image='

with open(file_path) as f:
    for num, line in enumerate(f, 1):
        if search_str in line:
            index = num
            break

# Changing the desired part of this file
new_contents = file_contents.replace(file_contents.split("\n")[index-1], way_to_wallpaper)

# Writing changes back to the file
with open(file_path, "w") as f:
    f.write(new_contents)

# Restarting the desktop to change the wallpaper
os.system("kquitapp5 plasmashell && kstart5 plasmashell &")


