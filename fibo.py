def nth_fibonacci(n): 
    n = int(n)
    fibs = [1,1] # initialize with first two elements
    while len(fibs) < n:
        fibs.append(fibs[-2]+fibs[-1])
    return fibs[n-1]