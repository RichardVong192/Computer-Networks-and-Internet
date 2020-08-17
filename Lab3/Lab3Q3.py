def message_delay (connSetupTime_s, cableLength_km, speedOfLight_kms, messageLength_b, dataRate_bps):
    
    TS = connSetupTime_s
    l = cableLength_km
    c = speedOfLight_kms
    m = messageLength_b
    r = dataRate_bps
    
    prop_delay  = l / c #propagate along a cable, length / speed of light
    trans_delay = m / r #transmit onto the cable, message / rate of cable
    
    A_to_C = trans_delay + prop_delay
    B_to_C = prop_delay #"Things appear as if B is not present at all"
    result = TS + A_to_C + B_to_C
    return result
    
print ("{:.3f}".format(message_delay(0.305, 15000, 200000, 5000, 1000000)))

    