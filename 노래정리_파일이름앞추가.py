# -*- coding: cp949 -*-
import os

ddir = 'C:\\Users\\SSPLab1\\Desktop\\Music\Begin Again - OST'

add_name = 'Begin Again-'

os.chdir(ddir)
list_screen = os.listdir(ddir)
print(list_screen)

for file in list_screen:
    
    new_file = add_name + file
    os.renames(file,new_file)
    

#print(list_screen)

