def revisedcompose (hdrlen, tosdscp, identification, flags, fragmentoffset, timetolive, protocoltype, sourceaddress, destinationaddress, payload):
    version = 4 
    totallength = hdrlen * 4 + len(payload)
    headerchecksum = 0

    if hdrlen < 5 or hdrlen > 2**4-1:
        return 2
    elif tosdscp < 0 or tosdscp > 2**6-1:
        return 3
    elif identification < 0 or identification > 2**16-1:
        return 5
    elif flags < 0 or flags > 2**3-1:
        return 6
    elif fragmentoffset < 0 or fragmentoffset > 2**13-1:
        return 7
    elif timetolive < 0 or timetolive > 2**8-1:
        return 8
    elif protocoltype < 0 or protocoltype > 2**8-1:
        return 9
    elif headerchecksum < 0 or headerchecksum > 2**16-1:
        return 10
    elif sourceaddress < 0 or sourceaddress > 2**32-1:
        return 11
    elif destinationaddress < 0 or destinationaddress > 2**32-1:
        return 12
    else: 
        initial_byte = version << 4 | hdrlen #add another 4 bits to version, then add hdrlen to it with bitwise or
        tosdscp1 = tosdscp << 2 | 0 #there are 2 unused bits
        flags1 = flags << 5 | fragmentoffset >> 8
        fragmentoffset1 = fragmentoffset & 0xFF
        
        array = bytearray()
        array.append(initial_byte)
        array.append(tosdscp1)
        array.extend(totallength.to_bytes(2, byteorder='big'))
        array.extend(identification.to_bytes(2, byteorder='big'))
        array.append(flags1)
        array.append(fragmentoffset1)
        array.extend(timetolive.to_bytes(1, byteorder='big'))
        array.extend(protocoltype.to_bytes(1, byteorder='big'))
        array.extend(headerchecksum.to_bytes(2, byteorder='big'))
        array.extend(sourceaddress.to_bytes(4, byteorder='big'))
        array.extend(destinationaddress.to_bytes(4, byteorder='big'))        

        if hdrlen > 5: #more than 5 bytes
            array.extend((0).to_bytes(4, byteorder='big')) #extend by 0's for the remainder 32-bit words
        x = 0
        for i in range(0, 20, 2): #we are in 8 bit and question ask to work in 16bit so go from 0 to 20 with 2 level increments
            sixteen_bit = (array[i] << 8 | array[i+1]) #so bitshift it left by 8 then use bitwise OR to add the next value
            x += sixteen_bit
        while x > 0xFFFF:    #now we are working in 16bit
            x0 = x & 0xFFFF  #assign to X0 the lowest 16 bits, '&' is bit-wise and
            x1 = x >> 16     # '>>' is right-shift operator, i.e. shift X to the right by 16 bits
            x = x0 + x1      #assignment
        x = 0xFFFF - x
        b1 = x >> 8 #first significant bit
        b2 = x & 0xFF #second significant bit
        array[10] = b1 #add to index
        array[11] = b2 #add to index
        array.extend(payload) #extend the array with the payload
        return array

print(revisedcompose (6, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15])))
print(revisedcompose(16,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(4,0,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,64,4000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,0x10000,0,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,8,63,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,0,8192,22,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,0,8191,256,0x06, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,0,8191,64,256, 2190815565, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,0,8191,64,0x06, 4294967296, 3232270145, bytearray([])))
print(revisedcompose(5,63,4711,0,8191,64,0x06, 2190815565, 4294967296, bytearray([])))
print(revisedcompose (5, 24, 4711, 0, 22, 64, 0x06, 0x22334455, 0x66778899, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17])))
print(revisedcompose (5, 24, 4711, 0, 22, 64, 0x06, 0x66778899, 0x22334455, bytearray([0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17])))
