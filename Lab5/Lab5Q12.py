def p_persistent_csma_collision_probability (p):
    
    prob_both_collide = p**2
    r = (1-p)**2
    result = prob_both_collide / (1 - r)
    
    return result
    
    
print ("{:.3f}".format(p_persistent_csma_collision_probability(0.2)))