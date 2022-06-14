"""
Given a year, determine whether it is a leap year. If it is a leap year,
return the Boolean True, otherwise return False. 

The year can be evenly divisible by 4, is a leap year, unless:
    the year can be evenly divisible by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year. 
"""

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 == 0 and year % 400 != 0:
            return leap
        else:
            leap = True
    return leap

year = int(raw_input())
print is_leap(year)

