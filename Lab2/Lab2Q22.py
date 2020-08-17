def queueing_delay (rate_Mbps, numPackets, packetLength_bytes):
    rate_bps = rate_Mbps * 1000000
    packetLength_b = packetLength_bytes * 8
    result = packetLength_b / rate_bps * numPackets
    result2 = result / 1000
    return result2

print ("{:.3f}".format(queueing_delay(100, 20, 1500)))