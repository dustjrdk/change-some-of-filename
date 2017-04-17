# -*- coding: cp949 -*-
import os

ddir = "C:\\Users\\SSPLab1\\Desktop\\이적 전집\\패닉 1집 달팽이"

old_name = " - "
new_name = ''

os.chdir(ddir)
list_screen = os.listdir(ddir)
print(list_screen)

for file in list_screen:

   
    new_file=file.replace(old_name,new_name)
    print(new_file)

    os.renames(file,new_file)
    

#print(list_screen)
