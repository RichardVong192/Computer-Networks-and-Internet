def destaddress (pkt):
    addr = pkt[16] << 24 | pkt[17] << 16 | pkt[18] << 8 | pkt[19] << 0
    dd = str(pkt[16]) + '.' + str(pkt[17]) + '.' + str(pkt[18]) + '.' + str(pkt[19])
    return addr, dd

print(destaddress(bytearray(b'E\x00\x00\x1e\x04\xd2\x00\x00@\x06\x00\x00\x00\x124V3DUf')))