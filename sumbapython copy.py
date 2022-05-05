import zipapp

#56?
f = open("puzzledatats.txt", "r") 
counter = 0
n= [1]
asnd = [12,48,30,95,15,55,97]
x= 0

for line in f:
    y = line.split()
    print(y[0])
    for all in range(0,6):
        n.append(int(y[all]))
print(n)
result =[]
zamn = 0
z = 1
counter = 0
y = 7
average = 0
winning = 0
while y!= 30006:
    for x in range(z,y):
        for h in range(0,7):
            if (n[x]) == asnd[h]:
                counter +=1
                print(counter)
    print(x)

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
   
    
    t = 0
    z += 6
    y += 6
    print(winning)
print(winning)
