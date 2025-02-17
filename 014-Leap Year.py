"""
Write a program that checks if a given input year is a leap year or not

Condition 1: be multiple of 4 but not of 100
Condition 2: be multiple of 400 ( being multiple of 400 is automatically means being 
    multiple of 4)
"""
def LeapYear(n1):
    if(n1%4==0 and n1%100!=0) or (n1%400==0):
        print("It's a Leap Year!")
    else:
        print("It's not a Leap year")

n1=int(input("Year:"))
LeapYear(n1)
