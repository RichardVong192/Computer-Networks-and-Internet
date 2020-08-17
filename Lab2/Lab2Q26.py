def average_trials (P):
    probOfSucc = 1 - P
    result =  1 / probOfSucc
    return result
    


print ("{:.3f}".format(average_trials(0.1)))
