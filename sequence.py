import numpy as np

x = np.zeros(10)
x[0] = 1
x[1]= 1.5
sumx = 0
sum23x = 0

for i in range(0,2,1):
        print(x[i])

for i in range(2,10,1):
        x[i] = 0.2 * x[i-1] + 1.2 * x[i-2]
        print(np.round(x[i],7))

for i in range(0,10,1):
        if(2 < x[i] <3):
                sum23x = sum23x + x[i]

sumx = np.sum(x)
print(np.round(sumx,7))
print(np.round(sum23x,7))
