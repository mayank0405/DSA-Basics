def sparse(n):
    if n == 0 or  n == 1:
        return True
    
    return (n & (n>>1) == 0)