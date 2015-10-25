#!/usr/bin/python3
# -*- coding: UTF-8 -*-
###################################################################################################
#                                                                 ________                          
#                                                          _     |__    __| __  _      __           
#   ______    _____   ___  ___  ___  ___   _____  ______  | \_      |  |   |__|| \_   |  |    _____ 
#  |   ___|  /     \ |   \/   ||   \/   | /  _  \|      \ |   _|    |  |   |  ||   _| |  |   /  _  \
#  |  |____ |   o   ||        ||        |/  ____/|   _   ||  |___   |  |   |  ||  |___|  |_ /  ____/
#  |_______| \_____/ |__|\/|__||__|\/|__|\______/|__| |__|\_____/   |__|   |__|\_____/|____|\______/
####################################################################################################
#  2015/10/25 by DKZ https://davidkingzyb.github.io


import commentTitle
import os

files=os.listdir()

def doAddTitles(files,lines):
    for x in files:
        if len(x.split('.'))==2 and x!='commentTitle.py' and x!='addTitles.py':
            if x.split('.')[1]=='py' or x.split('.')[1]=='js' or x.split('.')[1]=='ts':
                commentTitle.doSave(x,lines)

if __name__ == '__main__':
    print("title:")
    inputstr=input()
    lines=commentTitle.doComment(inputstr)

    doAddTitles(files,lines)
    print('ok')
