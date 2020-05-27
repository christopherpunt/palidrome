
#helper function for oldpalindrome
def oldPal(myString):
    for i in range(int(len(myString))):
        if myString[i] != myString[-(i+1)]:
            return False
    return True

def oldPalindrome(string):
    for char in range(len(string)):
        newWord = string[0:char] + string[char + 1:len(string)]
        return oldPal(newWord)


def newPalindrome(string):
    for char in range(len(string)):
        newWord = string[0:char] + string[char + 1:len(string)]
        return newPal(newWord)

def newPal(myString):
    for n in range(int(len(myString)/2)):
        print(myString[n]  + " " + myString[len(myString) - n - 1])
        if(myString[n] != myString[len(myString) - n - 1]):
            return False
    return True



# print(oldPalindrome("bhannah"))
