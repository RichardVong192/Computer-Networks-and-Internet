import math
def total_number_bits (maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    M = messageLength_b
    
    if (M % S) != 0:
        num_overhead = ((M // S) + 1) * O
    else:
        num_overhead = (M // S) * O
        
    result = M + num_overhead
    return result
    

    
print ("{:.1f}".format(total_number_bits(1000, 100, 10000)))
print ("{:.1f}".format(total_number_bits(1000, 100, 10001)))
print ("{:.1f}".format(total_number_bits(1000, 100, 10999)))

