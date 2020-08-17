def packet_transfer_time (linkLength_km, speedOfLight_kms, processingDelay_s, dataRate_bps, maxUserDataBitsPerPacket_b, overheadBitsPerPacket_b):
    L = linkLength_km
    C = speedOfLight_kms
    P = processingDelay_s
    R = dataRate_bps
    S = maxUserDataBitsPerPacket_b
    O = overheadBitsPerPacket_b
    
    M = S + O #message length
    AB_prop_delay = L / C
    trans_delay = M / R
    BC_prop_delay = L / C
    
    result = AB_prop_delay + trans_delay + P + BC_prop_delay + trans_delay + P
    return result
    
	
print(packet_transfer_time (15000, 250000, 0.001, 1000000, 4192, 100))