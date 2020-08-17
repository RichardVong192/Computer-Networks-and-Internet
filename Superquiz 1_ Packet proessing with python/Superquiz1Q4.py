def payload (pkt):
    hdrlen = pkt[0] & 0xF #take item at position 0, then take last 4 bits
    hdr_Bytes = hdrlen * 4 #32 bits = 4 bytes
    return pkt[hdr_Bytes:]

print(payload(bytearray(b'E\x00\x00\x17\x00\x00\x00\x00@\x06i\x8d\x11"3DUfw\x88\x10\x11\x12')))
