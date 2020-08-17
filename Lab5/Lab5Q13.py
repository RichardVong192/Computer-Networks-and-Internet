def p_persistent_csma_access_delay (p):
    return 1/p - 1
    
print ("{:.3f}".format(p_persistent_csma_access_delay(0.1)))