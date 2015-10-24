letter = {
    'a': ["   ###    ", "  ## ##   ", " ##   ##  ", "##     ## ", "######### ", "##     ## ", "##     ## "],
    'b': ["########  ", "##     ## ", "##     ## ", "########  ", "##     ## ", "##     ## ", "########  "],
    'c': [" ######  ", "##    ## ", "##       ", "##       ", "##       ", "##    ## ", " ######  "],
    'd': ["########  ", "##     ## ", "##     ## ", "##     ## ", "##     ## ", "##     ## ", "########  "],
    'e': ["######## ", "##       ", "##       ", "######   ", "##       ", "##       ", "######## "],
    'f': ["######## ", "##       ", "##       ", "######   ", "##       ", "##       ", "##       "],
    'g': [" ######   ", "##    ##  ", "##        ", "##   #### ", "##    ##  ", "##    ##  ", " ######   "],
    'h': ["##     ## ", "##     ## ", "##     ## ", "######### ", "##     ## ", "##     ## ", "##     ## "],
    'i': ["#### ", " ##  ", " ##  ", " ##  ", " ##  ", " ##  ", "#### "],
    'j': ["      ## ", "      ## ", "      ## ", "      ## ", "##    ## ", "##    ## ", " ######  "],
    'k': ["##    ## ", "##   ##  ", "##  ##   ", "#####    ", "##  ##   ", "##   ##  ", "##    ## "],
    'l': ["##       ", "##       ", "##       ", "##       ", "##       ", "##       ", "######## "],
    'm': ["##     ## ", "###   ### ", "#### #### ", "## ### ## ", "##     ## ", "##     ## ", "##     ## "],
    'n': ["##    ## ", "###   ## ", "####  ## ", "## ## ## ", "##  #### ", "##   ### ", "##    ## "],
    'o': [" #######  ", "##     ## ", "##     ## ", "##     ## ", "##     ## ", "##     ## ", " #######  "],
    'p': ["########  ", "##     ## ", "##     ## ", "########  ", "##        ", "##        ", "##        "],
    'q': [" #######  ", "##     ## ", "##     ## ", "##     ## ", "##  ## ## ", "##    ##  ", " ##### ## "],
    'r': ["########  ", "##     ## ", "##     ## ", "########  ", "##   ##   ", "##    ##  ", "##     ## "],
    's': [" ######  ", "##    ## ", "##       ", " ######  ", "      ## ", "##    ## ", " ######  "],
    't': ["######## ", "   ##    ", "   ##    ", "   ##    ", "   ##    ", "   ##    ", "   ##    "],
    'u': ["##     ## ", "##     ## ", "##     ## ", "##     ## ", "##     ## ", "##     ## ", " #######  "],
    'v': ["##     ## ", "##     ## ", "##     ## ", "##     ## ", " ##   ##  ", "  ## ##   ", "   ###    "],
    'w': ["##      ## ", "##  ##  ## ", "##  ##  ## ", "##  ##  ## ", "##  ##  ## ", "##  ##  ## ", " ###  ###  "],
    'x': ["##     ## ", " ##   ##  ", "  ## ##   ", "   ###    ", "  ## ##   ", " ##   ##  ", "##     ## "],
    'y': ["##    ## ", " ##  ##  ", "  ####   ", "   ##    ", "   ##    ", "   ##    ", "   ##    "],
    'z': ["######## ", "     ##  ", "    ##   ", "   ##    ", "  ##     ", " ##      ", "######## "],
    ' ':["   ", "   ", "   ", "   ", "   ", "   ", "   "],
    '0':["  #####   ", " ##   ##  ", "##     ## ", "##     ## ", "##     ## ", " ##   ##  ", "  #####   "],
    '1':["   ##   ", " ####   ", "   ##   ", "   ##   ", "   ##   ", "   ##   ", " ###### "],
    '2':[" #######  ", "##     ## ", "       ## ", " #######  ", "##        ", "##        ", "######### "],
    '3':[" #######  ", "##     ## ", "       ## ", " #######  ", "       ## ", "##     ## ", " #######  "],
    '4':["##        ", "##    ##  ", "##    ##  ", "##    ##  ", "######### ", "      ##  ", "      ##  "],
    '5':["######## ", "##       ", "##       ", "#######  ", "      ## ", "##    ## ", " ######  "],
    '6':[" #######  ", "##     ## ", "##        ", "########  ", "##     ## ", "##     ## ", " #######  "],
    '7':["######## ", "##    ## ", "    ##   ", "   ##    ", "  ##     ", "  ##     ", "  ##     "],
    '8':[" #######  ", "##     ## ", "##     ## ", " #######  ", "##     ## ", "##     ## ", " #######  "],
    '9':[" #######  ", "##     ## ", "##     ## ", " ######## ", "       ## ", "##     ## ", " #######  "],
    '+':["       ", "  ##   ", "  ##   ", "###### ", "  ##   ", "  ##   ", "       "],
    '-':["        ", "        ", "        ", "####### ", "        ", "        ", "        "],
    '&':["  ####    ", " ##  ##   ", "  ####    ", " ####     ", "##  ## ## ", "##   ##   ", " ####  ## "],
}

def doBigComment(string):
    lines = ["", "", "", "", "", "", ""]
    for x in range(0,7):
        linestr=''
        for c in string:
            linestr=linestr+letter[c][x]
        lines[x]=linestr
    return lines

def printComment(lines):
    for i in range(0,7):
        print('// '+lines[i])

print('input comment:')
inputstr=input()
lines=doBigComment(inputstr)
printComment(lines)  