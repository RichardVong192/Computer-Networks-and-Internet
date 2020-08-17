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

print(decodedate(1107298273))
print(decodedate(2298488591))
print(decodedate(998246312))

