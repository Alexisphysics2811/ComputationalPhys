def incremental(f,x0,b,h):
    x1 = x0 + h
    n = 1
    while f(x0) > 0 and f(x1) > 0:
        if x1 > b:
            return "None"
        x0 = x1
        x1 = x0 + h
        n+=1
    return x1, n

def bisection(f,x0,x1,tol=1e-6):
    n = 1
    while abs(x0 - x1) > tol:
        x2 = (x0 + x1)/2
        if f(x0)*f(x2) < 0:
            x1 = x2
        if f(x1)*f(x2) < 0:
            x0 = x2
        n+=1
    return x1,n

def newton_raphson(f, f_prime, x0, tol=1e-6):
    x1 = x0 - f(x0)/f_prime(x0)
    n = 1
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = x0 - f(x0)/f_prime(x0)
        n += 1
    return x1, n

def secant(f, x0, x1, tol=1e-6):
    n = 1
    while abs(x1 - x0) > tol:
        x2 = x1 - f(x1)*((f(x1) - f(x0))/(x1 - x0))**(-1)
        x0 = x1
        x1 = x2
        n += 1
    return x1, n
