from cmath import sqrt
import zipapp
import math
#56?
f = open("puzzledatasp.txt", "r") 
counter = 0
n= []
asnd = [12,48,30,95,15,55,97]
x= 0
def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("square root not defined for negative numbers")
for line in f:
    y = line.split()
    print(y[0])
    for all in range(0,3):
        n.append(int(y[all]))
print(n)
result =[]
zamn = 0
z = 3
counter = 0
y = 6
average = 0
dist = 0
winning = 0
while y!= 162:
    for x in range(z,y):
        average += ((n[x] - n[x-3])**2)
        
    
    dist += (isqrt(average))
    
    print(dist)
  
    if counter == 3:
        winning += 1
    if counter == 4:
        winning += 10
    if counter == 5:
        winning += 100
    if counter == 6:
        winning += 1000
    if counter == 7:
        winning += 10000
    t = average/60
    counter = 0
   
    
    average = 0
    z += 3
    y += 3
    
