# -*- coding: cp949 -*-
import os

ddir = "C:\\Users\\SSPLab1\\Desktop\\Camera"

os.chdir(ddir)
list_screen = os.listdir(ddir)
#print(list_screen)

for file in list_screen:
    Iyear16 = file.find('2016')
    Iyear17 = file.find('2017')
    
    if Iyear16 is not -1:
        Nday = file[Iyear16 + 4 : Iyear16 + 8]
        
        new_file=file.replace('2016'+Nday,'16'+Nday+'\\2016'+Nday)
        print(new_file)

        os.renames(file,new_file)

    if Iyear17 is not -1:
        Nday = file[Iyear17 + 4 : Iyear17 + 8]
        
        new_file=file.replace('2017'+Nday,'17'+Nday+'\\2017'+Nday)
        print(new_file)

        os.renames(file,new_file)

#print(list_screen)
