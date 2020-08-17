def transmission_delay (packetLength_bytes, rate_bps):
    packetLength_bits = packetLength_bytes * 8
    return packetLength_bits / rate_bps
    
    

print ("{:.3f}".format(transmission_delay(1000000, 4000000)))