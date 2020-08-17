def total_time (cableLength_KM, packetLength_b):
    speedOfLight_kms = 200000 #kms
    dataRate_bits = 10 #Gbps
    
    time = cableLength_KM / speedOfLight_kms #calculate time through cable
    delay = packetLength_b / 1000000000 / dataRate_bits #calculate delayLength/convert/rate
    result = (delay + time) * 1000 #add delay and time and convert
    return result

print ("{:.4f}".format(total_time(10000, 8000)))