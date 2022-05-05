f = open("puzzledatat.txt", "r") 
counter = 0
n= [86400]
x= 0
for x in f:
    
    n.append(int(x))
z = 1
counter = 0
y = 61
average = 0
while y!= 86400:
    for x in range(z,y):
        average += n[x]
 
    t = average/60
    average = 0
    print(t)
    if t<1500 or t > 1600:
        counter += 1
    t = 0
    z += 1
    y += 1
   
print(counter)
