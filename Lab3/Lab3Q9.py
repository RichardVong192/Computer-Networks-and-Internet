def total_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b, messageLength_b):
    l = linkLength_km
    c = speedOfLight_kms
    p = processingDelay_s
    r = dataRate_bps
    s = maxUserDataBitsPerPacket_b
    o = overheadBitsPerPacket_b
    m = messageLength_b
    
    num_packets = m / s
    total_bits = o + s
    prop_delay = l / c
    
    A_to_C = ((total_bits / r) + prop_delay + p)
    C_to_A = ((total_bits / r) + prop_delay + p)
    trans_delay_rest = (total_bits / r) * (num_packets - 1)
    result = A_to_C + C_to_A + trans_delay_rest
    
    return result

print(total_transfer_time (10000, 200000, 0.001, 1000000, 1000, 100, 1000000000))
