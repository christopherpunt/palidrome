
#helper function for oldpalindrome
def oldPal(myString):
    for i in range(int(len(myString))):
        if myString[i] != myString[-i-1]:
            return False
    return True

def oldPalindrome(string):
    for char in range(len(string)):
        newWord = string[0:char] + string[char + 1:len(string)]
        if oldPal(newWord) == True:
            return True
    return False



#helper function for newPalindrome that is more efficient
def newPal(myString):
    for n in range(int(len(myString)/2)):
        if(myString[n] != myString[len(myString) - n - 1]):
            return False
    return True

def newPalindrome(string):
    for char in range(len(string)):
        newWord = string[0:char] + string[char + 1:len(string)]
        if newPal(newWord) == True:
            return True
    return False

