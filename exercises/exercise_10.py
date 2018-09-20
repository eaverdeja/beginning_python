def printVerticalString(string):
    if string == '':
        return False
    else:
        print(string[0])
        printVerticalString(string[1:])

def transformStringDoubleChars(string, accumulated = ''):
    if len(string) == 1:
        return accumulated + string[0]
    
    accumulated = accumulated + string[0] + string[0:]
    return transformStringDoubleChars(string[1:], accumulated)

def isVowel(char):
    if(char == 'a' or char == 'e' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        return True
    else:
        return False

def transformStringDoubleVowels(string, accumulated = ''):
    if(isVowel(string[0])):
        if len(string) == 1:
            if(isVowel(string[0])):
                return accumulated + string[0] + string[0]
            return accumulated + string[0]
        accumulated = accumulated + string[0] + string[0]
    else:
        accumulated = accumulated + string[0]

    return transformStringDoubleVowels(string[1:], accumulated)

string = input('informe uma string')

printVerticalString(string)
print(transformStringDoubleChars(string))
print(transformStringDoubleVowels(string))
