def connection_setup_delay (cableLength_km, speedOfLight_kms, dataRate_bps, messageLength_b, processingTimes_s):
    
    l = cableLength_km
    c = speedOfLight_kms
    r = dataRate_bps
    m = messageLength_b
    p = processingTimes_s
    
    prop_delay  = l / c #propagate along a cable, length / speed of light
    trans_delay = m / r #transmit onto the cable, message / rate of cable
    
    A_to_B = trans_delay + prop_delay + p
    B_to_C = trans_delay + prop_delay + p
    
    result = A_to_B + B_to_C
    return result * 2 #(A to C then back again)
    
#print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 1000, 0.001)))

print ("{:.4f}".format(connection_setup_delay(10000, 200000, 1000000, 4000, 0.001)))