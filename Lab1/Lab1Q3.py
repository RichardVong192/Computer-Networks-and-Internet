def convert (x, base):
    alist = []
    
    while x != 0:
        if x < 0:
            return -1
        if base < 0:
            return -2
        if x < 0:
            return -3
        if base < 2:
            return -4
        else:
            result = x // base
            listnumb = x % base
            x = result
            alist.append(listnumb)
    alist.reverse()
    return alist

print (convert(1234, 10))
print (convert(1234, 16))