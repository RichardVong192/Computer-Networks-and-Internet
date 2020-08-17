def transmission_delay (packetLength_bytes, rate_mbps):
    packetLength_bytes = 8 * packetLength_bytes
    rate_mbps = 1000000 * rate_mbps
    return packetLength_bytes / rate_mbps

print ("{:.3f}".format(transmission_delay(1000000, 4)))