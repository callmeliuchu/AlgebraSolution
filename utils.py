def gcd(y,x):
    if x == 0:
        return y
    return gcd(x,y%x)
