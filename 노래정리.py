# -*- coding: cp949 -*-
import os

ddir = 'C:\\Users\\SSPLab1\\Desktop\\Music'
ffolder = '\\아이돌'

singer = []

os.chdir(ddir+ffolder)
list_screen = os.listdir(ddir+ffolder)

for file in list_screen:
    n = file.find('-')

    if n:
        sing = file[:n]
        if sing not in singer:
            singer.append(sing)

print(singer)
#print(list_screen)

