def per_from_ber (bitErrorProb, packetLen_b):
    probOfSucc = (1 - bitErrorProb) ** 1000
    return 1 - probOfSucc
    


print ("{:.3f}".format(per_from_ber(0.0001, 1000)))