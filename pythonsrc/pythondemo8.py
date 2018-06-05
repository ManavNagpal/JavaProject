year=121

modulus = year % 100

print modulus
if (year % 400 == 0):
    print "Its a leap year"
else:
    if (year % 4 == 0 & year % 100 != 0):
        print "Its a leap year"
    else:
        print "Its not a leap year"
