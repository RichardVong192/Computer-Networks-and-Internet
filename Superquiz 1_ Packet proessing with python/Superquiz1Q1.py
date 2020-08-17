def composepacket (version, hdrlen, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress):
    
    if version != 4:
        return 1
    elif hdrlen < 0 or hdrlen > 2**4-1:
        return 2
    elif tosdscp< 0 or tosdscp > 2**6-1:
        return 3
    elif totallength < 0 or totallength > 2**16-1:
        return 4
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
        alist = [initial_byte, tosdscp, totallength, identification, flags, fragmentoffset, timetolive, protocoltype, headerchecksum, sourceaddress, destinationaddress]
        result = bytearray()
        for item in alist:
            if item <= 2**8-1: #testing the highest value in 1 byte
                value = item.to_bytes(1, byteorder='big')
                result += value
            elif item <= 2**16-1: #testing the highest value in 2 bytes
                value = item.to_bytes(2, byteorder='big')
                result += value
            elif item <= 2**24-1: #testing the highest value in 3 bytes
                result = item.to_bytes(3, byteorder='big')
                result += value
            elif item <= 2**32-1: #testing the highest value in 4 bytes
                value = item.to_bytes(4, byteorder='big')
                result += value
        return result
        

print(composepacket(5,5,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))
	
print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[18])

print(composepacket(4,5,0,1500,24200,0,63,22,6,4711, 2190815565, 3232270145)[19])

print(composepacket(4,16,0,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,64,4000,24200,0,63,22,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,63,65536,24200,0,63,22,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,63,65535,65536,0,63,22,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,63,65535,65535,8,63,22,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,63,65535,65535,7,8192,22,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,63,65535,65535,7,8191,256,6,4711, 2190815565, 3232270145))

print(composepacket(4,15,63,65535,65535,7,8191,255,256,4711, 2190815565, 3232270145))

	
print(composepacket(4,15,63,65535,65535,7,8191,255,255,65536, 2190815565, 3232270145))

print(composepacket(4,5,0,1500,24200,0,63,22,6,-4711, 2190815565, 3232270145))