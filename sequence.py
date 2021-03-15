import numpy as np

#initialize variables
x = np.zeros(10)
x[0] = 1
x[1]= 1.5
sumx = sum23x = 0

#print initial values
for i in range(0,2,1):
        print(x[i])

#calculate next number in sequence and add it to the array
#round to 7 decimal places and print value
for i in range(2,10,1):
        x[i] = 0.2 * x[i-1] + 1.2 * x[i-2]
        print(np.round(x[i],7))

#calculate sum of values that are between 2 and 3
for i in range(0,10,1):
        if(2 <= x[i] <= 3):
                sum23x += x[i]

#calculate total sum
sumx = np.sum(x)

#print total sum
#print sum of values between 2 and 3
print(np.round(sumx,7))
print(np.round(sum23x,7))
