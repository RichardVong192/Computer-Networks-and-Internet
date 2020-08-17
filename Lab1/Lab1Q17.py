def decodedate (x):
    #take x and bitwise AND it, then shift it by 28 (32-4) because we want
    #the first 4 bits. This will get you the valye of the month
    month = ((x & 0xF0000000) >> 28)
    
    #First 5 numbers is 1's
    day = ((x & 0xF800000) >> 23)
    
    #Takes the remainder (so all 1's)
    year = (x & 0x7FFFFF)
    
    result = ('{}.{}.{}'.format(day+1,month+1,year))
    return result




def encodedate (day, month, year):
    x = 0
    x = (x & 0x0FFFFFFF) | ((month-1) << 28)
    x = (x & 0xF07FFFFF) | ((day-1) << 23)
    x = (x & 0xFF800000) | (year)
    
    if day not in range(1, 32):
        return -1
    elif month not in range(1, 13):
        return -1
    elif month not in range(0, 2**23):
        return -1
    return x
     
    
print(encodedate(5,5,2017))
print(encodedate(9,11,4444))
print(encodedate(30,12,345752))
print(encodedate(32,5,2017))
print(encodedate(5,15,2017))
print(encodedate(0,5,2017))
print(encodedate(5,0,2017))