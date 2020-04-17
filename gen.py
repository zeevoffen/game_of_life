from functools import reduce

def calc(n):
    m = [1,2,1,2,1,2,1,2]
    s=0
    for i in range(8):
        a=(m[i]*n[i])
        s+=a%10+int(a/10)
    return 10*int((s+9)/10) - s



import random
for i in range(100):
    r = [random.randint(0, 9) for iter in range(8)]
    print (r,calc(r))
