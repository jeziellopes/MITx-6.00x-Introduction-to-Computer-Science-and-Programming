def f(x):
    import math
    #return 10*math.e**(math.log(0.5)/5.27*x)
    #return 60*math.e**(math.log(0.5)/55.6*x)
    return 150*math.e**(math.log(0.5)/32.2*x)
    #return 200*math.e**(math.log(0.5)/14.1*x)
    #return 400*math.e**(math.log(0.5)/3.66*x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    
    if start >= stop-step:
        return step * f(stop-step)

    return (f(start) * step) + radiationExposure(start + step, stop, step)    

def radiationExposureERRADO(start, stop, step):
    
    start = float(start)
    stop = float(stop)
    step = float(step)

    soma = 0.0
    point = start
    
    while point <= stop-step:
        point += step
        soma += f(point)
        
    return soma





