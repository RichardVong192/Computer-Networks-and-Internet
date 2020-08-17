import math
def number_fragments (messageSize_bytes, overheadPerPacket_bytes, maximumNPacketSize_bytes):
    s = messageSize_bytes
    o = overheadPerPacket_bytes
    m = maximumNPacketSize_bytes
    result = math.ceil(s / (m - o))
    return result

print (number_fragments(10000, 100, 1000))