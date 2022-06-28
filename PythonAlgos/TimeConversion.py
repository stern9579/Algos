

def timeConversion(s):
    a = s[-2:]
    b = s[:2]
    c = s[2:-2]
    print(b)

    if a == "PM":
        if int(b) <= 11:
            (b) = int(b) + 12
            print(b)
    if a == "AM":
        if int(b) == 12:
            b = '00'
    
    output = str(b) + c
    
    return output


time = '07:05:45PM'
time2 = '12:05:45AM'
time3 = '04:59:59AM'



print(timeConversion(time))
print(timeConversion(time2))
print(timeConversion(time3))
