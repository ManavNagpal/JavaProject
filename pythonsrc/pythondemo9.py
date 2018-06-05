number1 = 16661
number2 = 0

temp = number1

reverse = 0

while(number1 != 0):
    remainder = number1 % 10
    reverse = reverse * 10 + remainder
    number1 = number1 / 10

if (reverse == temp):
    print "its a palindrome"
else:
    print "its not a palindrome"
    
