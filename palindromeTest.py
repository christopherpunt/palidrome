from palindrome import *

string0 = ""
string1 = "t"
string2 = "testword"
string3 = "bhannah"
string4 = "hanbnah"
string5 = "kayfak"
string6 = "rabdar"


#run Tests

assert oldPalindrome(string1) == True
assert newPalindrome(string1) == True

assert oldPalindrome(string2) == False
assert newPalindrome(string2) == False

assert oldPalindrome(string3) == True
assert newPalindrome(string3) == True

assert oldPalindrome(string4) == True
assert newPalindrome(string4) == True

assert oldPalindrome(string5) == True
assert newPalindrome(string5) == True

assert oldPalindrome(string6) == True
assert newPalindrome(string6) == True