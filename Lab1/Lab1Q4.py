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

def convert_number(x):
    if x == 10:
        return 'A'
    elif x == 11:
        return 'B'
    elif x == 12:
        return 'C'
    elif x == 13:
        return 'D'
    elif x == 14:
        return 'E'
    elif x == 15:
        return 'F'

def hexstring (x):
    result = '0x'
    if type(x) is not int:
        return -1
    if (x > 0) is False:
        return -2
    else:
        alist = convert(x, 16)
        for i in alist:
            if i <= 9:
                result += str(i)
            else:
                while i > 15:
                    i = i // 16
                letter = convert_number(i)
                result += letter
    return result

print(hexstring(1234))