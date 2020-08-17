def avg_trials_from_ber (bit_error_probability, packetLength_b):
    
    packetErrorProbability = (1 - bit_error_probability) ** packetLength_b
    E = 1 / packetErrorProbability #expected number of trials until success.
    return E
    

print ("{:.3f}".format(avg_trials_from_ber(0.0001, 1000)))
