def APAGA(d, k): 	
    n = len(d)
    i = 1
    while len(d) > n - k and i <= n - k:
        if d[i-1]==9:
            i += 1
        if d[i-1] < d[i]:
            d.pop(i-1)
        else:
            d.pop(i)
    while len(d) > n - k:
        d.pop(-1)
    return d

x = [7,9,8,4,9,2,5,7,3,5]
#x = [9,9,9,9,9,9]
k = 7
print(APAGA(x,k))
