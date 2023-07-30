def sum_n(n):
    if type(n)!=int or n<=0:
        raise ValueError('Invalid Type or Value')
    res=(n*(n+1)/2)
    print(res)
    return 

if __name__=='__main__':
    sum_n(10)