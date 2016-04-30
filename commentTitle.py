#!/usr/bin/python3
# coding: utf-8
###################################################################################################
#                                                               ________                          
#                                                        _     |__    __| __  _      __           
# ______    _____   ___  ___  ___  ___   _____  ______  | \_      |  |   |__|| \_   |  |    _____ 
#|   ___|  /     \ |   \/   ||   \/   | /  _  \|      \ |   _|    |  |   |  ||   _| |  |   /  _  \
#|  |____ |   o   ||        ||        |/  ____/|   _   ||  |___   |  |   |  ||  |___|  |_ /  ____/
#|_______| \_____/ |__|\/|__||__|\/|__|\______/|__| |__|\_____/   |__|   |__|\_____/|____|\______/
###################################################################################################
#2015/10/25 by DKZ https://davidkingzyb.github.io


import datetime
import os
import sys



TITLE='DKZ'
AUTHOR='DKZ'
CONTACT='https://davidkingzyb.github.io'
LICENSE=''
DESC=''

DATE=datetime.datetime.now().strftime('%Y/%m/%d')
YEAR=datetime.datetime.now().strftime('%Y')

HEADDIC={
    'html':'<!DOSTYPE html>',
    'py':'# coding: utf-8',
    '':''
}
COMMENTDIC={
    'html':{'start':'<!--','end':'-->'},
    'py':{'start':'"""','end':'"""'},
    'js':{'start':'/*','end':'*/'},
    'css':{'start':'/*','end':'*/'},
    'ts':{'start':'/*','end':'*/'}
}




LICENSEMIT="""
license:MIT

Copyright (c) %(year)s %(author)s

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

LICENSEBSD="""
license:BSD

Copyright (c) %(year)s %(author)s
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF 
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

LICENSEAPACHE="""
license:apache

Copyright %(year)s %(author)s

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

LICENSEGPL="""
license:GPL

Copyright (C) %(year)s %(author)s

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

LICENSELGPL="""
license:LGPL

Copyright (C) %(year)s %(author)s

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

LICENSESDIC={
    'mit':LICENSEMIT,
    'gpl':LICENSEGPL,
    'apache':LICENSEAPACHE,
    'bsd':LICENSEBSD,
    'lgpl':LICENSELGPL,
    '':''
}

FONTCT={

    "A":["    __    ","   /  \\   ","  / /\\ \\  "," / /__\\ \\ ","/  ____  \\","__|    |__"],
    "B":[" _______  ","|   _   \\ ","|  |_|  / ","|   _   \\ ","|  |_|   |","|_______/ "],
    "C":[" ________ ","|   _____|","|  |      ","|  |      ","|  |_____ ","|________|"],
    "D":["`_______  ","|   __  \\ ","|  |  \\  \\","|  |  |  |","|  |__|  |","|________/"],
    "E":[" ________ ","|   _____|","|  |____  ","|   ____| ","|  |_____ ","|________|"],
    "F":[" ________ ","|   _____|","|  |____  ","|   ____| ","|  |      ","|__|      "],
    "G":[" ________ ","/   _____|","|  | ____ ","|  ||_   \\","|  |__|  |","|________/"],
    "H":[" __    __ ","|  |  |  |","|  |__|  |","|   __   |","|  |  |  |","|__|  |__|"],
    "I":["  ______  "," |_    _| ","   |  |   ","   |  |   ","  _|  |_  "," |______| "],
    "J":["     ____ ","    |_   |","      |  |","___   |  |","\\  \\__/  |"," \\______/ "],
    "K":["`__   __  ","|  | /  / ","|  |/  /  ","|   _  \\  ","|  | \\  \\ ","|__|  \\__\\"],
    "L":[" __       ","|  |      ","|  |      ","|  |      ","|  |_____ ","|________|"],
    "M":[" __    __ ","|  \\  /  |","|   \\/   |","|        |","|  |\\/|  |","|__|  |__|"],
    "N":[" ___   __ ","|   \\ |  |","|    \\|  |","|        |","|  |\\    |","|__| \\___|"],
    "O":["  ______  "," /      \\ ","/   __   \\","|  |__|  |","\\        /"," \\______/ "],
    "P":[" ________ ","|   __   \\","|  |__|  /","|   ____/ ","|  |      ","|__|      "],
    "Q":["  ______  "," /      \\ ","/   __   \\","|  |__/  /","\\        \\"," \\____/\\_/"],
    "R":[" ________ ","|   __   \\","|  |__|  /","|   _   / ","|  | \\  \\ ","|__|  \\__\\"],
    "S":["  _______ ","/  _____/ ","\\  \\_____ "," \\_____  \\","______/  /","\\_______/ "],
    "T":[" ________ ","|__    __|","   |  |   ","   |  |   ","   |  |   ","   |__|   "],
    "U":[" __    __ ","|  |  |  |","|  |  |  |","|  |  |  |","|  |__|  |","|________|"],
    "V":[" __    __ ","|  |  |  |","|  |  |  |","\\  \\  /  /"," \\  \\/  / ","  \\____/  "],
    "W":[" __    __ ","|  |  |  |","|  |/\\|  |","|        |","|   /\\   |","|__/  \\__|"],
    "X":[" __  ____ ","\\  \\/   / "," \\     /  ","  /   /   "," /     \\  ","|___/\\__\\ "],
    "Y":[" __  ____ ","\\  \\/   / "," \\     /  ","  /   /   "," /   /    ","|___/     "],
    "Z":["`_______  ","|___   /  ","   /  /   ","  /  /    "," /  /____ ","/________|"],
    "a":["         ","         ","  ____   "," /    \\  ","/  /   \\_","\\_______/"],
    "b":["         ","         "," ___     ","|   |___ ","|  ___  |","|_______|"],
    "c":["         ","         "," ______  ","|   ___| ","|  |____ ","|_______|"],
    "d":["         ","         ","     ___ "," ___|   |","|  ___  |","|_______|"],
    "e":["        ","        ","  _____ "," /  _  \\","/  ____/","\\______/"],
    "f":["        "," ______ ","|   ___|","|  |__  ","|   __| ","|__|    "],
    "g":["        ","        ","  _____ "," / _   |","_\\___  |","\\______|"],
    "h":["         "," __      ","|  |     ","|  |____ ","|   _   |","|__| |__|"],
    "i":["    "," __ ","|__|","|  |","|  |","|__|"],
    "j":["       ","    __ ","   |__|","   |  |","___|  |","\\_____/"],
    "k":["        "," __  __ ","|  |/ / ","|    /  ","|  |\\ \\ ","|__| \\_\\"],
    "l":["      "," __   ","|  |  ","|  |  ","|  |_ ","|____|"],
    "m":["          ","          "," ___  ___ ","|   \\/   |","|        |","|__|\\/|__|"],
    "n":["         ","         "," ______  ","|      \\ ","|   _   |","|__| |__|"],
    "o":["         ","         ","  _____  "," /     \\ ","|   o   |"," \\_____/ "],
    "p":["         ","         "," _______ ","|   __  |","|    ___|","|___|    "],
    "q":["         ","         "," _______ ","|  __   |","|___    |","    |___|"],
    "r":["       ","       "," __  __","|  |/_/","|   |  ","|___|  "],
    "s":["       ","       "," ______","/  ___/","\\___  \\","\\_____/"],
    "t":["       "," _     ","| \\_   ","|   _| ","|  |___","\\_____/"],
    "u":["        ","        "," __  __ ","|  | | |","|  |_| |","|______|"],
    "v":["        ","        "," __  __ ","|  | | |","\\   \\/ /"," \\____/ "],
    "w":["          ","          "," __    __ ","|  |/\\|  |","|        |","|___/\\___|"],
    "x":["        ","        ","  __  __"," \\  \\/_/"," _\\  \\  ","/_/\\__\\ "],
    "y":["        ","        ","  __  __"," \\  \\/ /","  \\   / ","  /__/  "],
    "z":["        ","        ","_______ ","\\__   / ","  /  /__"," /_____/"],
    "0":["  _____   "," /  _  \\  ","/  / \\  \\ ","|  | |  | ","\\  \\_/  / "," \\_____/  "],
    "1":["   ___    ","  /_  |   ","    | |   ","    | |   ","   _| |_  ","  |_____| "],
    "2":[" _______  ","/______ \\ ","   ___/ / ","  / ___/  "," / /_____ ","/________|"],
    "3":[" _______  ","/______ \\ ","   ___/ / ","  |__  /  "," ____\\  \\ ","\\_______/ "],
    "4":[" _     _  ","| |   | | ","| \\___| | "," \\____  | ","      | | ","      |_| "],
    "5":["  ______  "," |  ____| "," | |____  "," \\___   \\ "," ____/  / ","\\______/  "],
    "6":["  ______  "," /  ____| ","/  /____  ","|  ___  \\ ","|  \\_/  / "," \\_____/  "],
    "7":[" ________ ","|_____   |","      / / ","     / /  ","    / /   ","   /_/    "],
    "8":["  _____   "," /  _  \\  "," \\ |_| /  "," /  _  \\  ","|  |_|  | "," \\_____/  "],
    "9":["  _____   "," /  _  \\  ","/  /_\\  \\ ","\\_____  | "," ____/  | "," \\_____/  "],
    "+":["          ","     _    ","   _| |_  ","  |_   _| ","    |_|   ","          "],
    "-":["          ","          ","   _____  ","  |_____| ","          ","          "],
    "*":["          ","  __  __  ","  \\ \\/ /  ","  /_/\\_\\  ","          ","          "],
    "/":["     __   ","    / /   ","   / /    ","  / /     "," /_/      ","          "],
    "=":["          ","   _____  ","  |_____| ","   _____  ","  |_____| ","          "],
    " ":["      ","      ","      ","      ","      ","      "],
    ".":["         ","         ","         ","  ____   "," |    |  "," |____|  "],
    "_":["         ","         ","         ","         "," _______ ","|_______|"],
    ":":["         ","         ","  __     "," |__|    ","  __     "," |__|    "],
    ";":["         ","  __     "," |__|    ","  __     "," |_ |    ","   |/    "],
    ",":["         ","         ","  ____   "," |    |  "," |__  |  ","    |/   "],
    "\"":["  __  __ "," /_/ /_/ ","         ","         ","         ","         "],
    "'":["  __     "," /_/     ","         ","         ","         ","         "],
    "?":[" ______  ","/ ____ \\ ","\\_\\  / / ","    |_|  ","     _   ","    |_|  "],
    "<":["    __   ","   / /   ","  / /    ","  \\ \\    ","   \\_\\   ","         "],
    ">":["   __    ","   \\ \\   ","    \\ \\  ","    / /  ","   /_/   ","         "],
    "\\":["  __     ","  \\ \\    ","   \\ \\   ","    \\ \\  ","     \\_\\ ","         "],
    "|":["    _    ","   | |   ","   | |   ","   | |   ","   |_|   ","         "],
    "(":["    __   ","   / /   ","  | |    ","  | |    ","   \\_\\   ","         "],
    ")":["   __    ","   \\ \\   ","    | |  ","    | |  ","   /_/   ","         "],
    "[":["   ___   ","  |  _|  ","  | |    ","  | |_   ","  |___|  ","         "],
    "]":["   ___   ","  |_  |  ","    | |  ","   _| |  ","  |___|  ","         "],
    "^":["   __    ","  /  \\   "," /_/\\_\\  ","         ","         ","         "],
    "&":["  ___    "," / __\\   "," \\ \\ __  "," / _/ /  ","/ |/  \\  ","\\___/\\_\\ "],
    "%":[" _   __  ","|_| / /  ","   / /   ","  / / _  "," /_/ |_| ","         "],
    "$":["    _    ","  _| |__ "," /  ___/ "," \\___  \\ "," \\_   _/ ","   |_|   "],
    "#":["  _   _  "," | |_| | ","|   _   |"," | |_| | ","|   _   |"," |_| |_| "],
    "@":["         ","  ____   "," / __ \\  ","| | _| | ","| |____| "," \\_____/ "],
    "!":["    _    ","   | |   ","   | |   ","   |_|   ","    _    ","   |_|   "],



}


def doCT(comment):
    lines = ["", "", "", "", "", ""]
    for x in range(0,6):
        linestr=""
        for c in comment:
            linestr=linestr+FONTCT[c][x]
        lines[x]=linestr
    return lines

def touch(filename,con):
    with open(filename,'wb') as f:
        f.write(con.encode('utf-8'))

def saveCommentTitle(filename,output):
    if os.path.exists(filename):
        with open(filename,'rb') as oldf:
            old=oldf.read()
        touch(filename,output)
        with open(filename,'ab') as tempf:
            tempf.write(old)
    else:
        touch(filename,output)

def makeCommentTitle(filename,title,author,contact,license,desc):
    output=''

    title=title if title!='' else TITLE
    author=author if author!='' else AUTHOR
    contact=contact if contact!='' else CONTACT
    license=license if license!='' else LICENSE
    licensestr=LICENSESDIC.get(license.lower(),'Copyright (c) %(year)s %(author)s')
    desc=desc if desc!='' else DESC
    filetype=filename.split('.')[1]
    head=HEADDIC.get(filetype,'')
    commentstart=COMMENTDIC.get(filetype,{'start':'','end':''})['start']
    commentend=COMMENTDIC.get(filetype,{'start':'','end':''})['end']
    lines=doCT(title)


    output=output+head+'\n'+commentstart+'\n'
    output=output+licensestr%{'author':author,'year':YEAR}+'\n'
    output=output+'='*len(lines[0])+'\n'
    for l in lines:
        output=output+l+'\n'
    output=output+'='*len(lines[0])+'\n'
    output=output+DATE+' by '+author+' '+contact+'\n'
    output=output+desc+'\n'+commentend

    saveCommentTitle(filename,output)

class fail(Exception):
    def __init__(self,msg):
        Exception.__init__(self)
        self.msg=msg

def main():
    if len(sys.argv)>1:
        filename=sys.argv[1]
        if len(filename.split('.'))!=2:
            raise fail('fail: file name format error')
        title=''
        author=''
        contact=''
        license=''
        desc=''
    else:
        print('file name:')
        filename=input()
        if len(filename.split('.'))!=2:
            raise fail('fail: file name format error')
        print('title:')
        title=input()
        print('author:')
        author=input()
        print('contact:')
        contact=input()
        print('license:')
        license=input()
        print('desc:')
        desc=input()
    
    makeCommentTitle(filename,title,author,contact,license,desc)
        

if __name__ == '__main__':
    try: input = raw_input
    except NameError: pass
    try:
        main()
    except fail:
        print('fail: file name format error')
        
    
