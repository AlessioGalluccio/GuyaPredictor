# Useful script to change the names of the images

import os
print("Insert chapter: ")
num_chapter = input()
path_dir = "J:/esercizi web/GuyaAI/AllGuyaImages/" + num_chapter + "/"
for count, filename in enumerate(os.listdir(path_dir)): 
    dst = path_dir + num_chapter +"_" + str(count) + ".png"
    src = path_dir + filename
    # rename() function will 
    # rename all the files 
    os.rename(src, dst) 
print("ok")