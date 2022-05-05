import uuid

print("Wildlife program ---------------- 5.8 ----/-")
def discount(a,b,c):
    prices = [20,12,16,60,15]
    day = (input("1 day or 2 days?"))
    while True:
      if (day.isnumeric() == True):
        break
      else:
        day = (input("1 day or 2 days? "))
    if (int(day) == 2):
      prices = [30,18,24,90,22.5]
    price = 0
    familycount = 0
    at = 0
    ct = 0
    st = 0
    g = 0
    if((a+b) * 2 < c):
      return "INVALID"
    while (a>1 and c>2) :
        familycount +=1
        a -= 2
        c -= 3
    while (a>0 and b>0 and (b+a) >1 and c>2):
        familycount +=1
        a-=1
        b-=1
        c-=3
    while (b>1 and c>2) :
        familycount +=1
        b -= 2
        c -= 3
   
    print(a,b,c)
    if(a+b+c>= 6):
      print("group")
      g += 1
    else:
      at += a
      st += b
      ct += c
    price += familycount*prices[3]
    price += at*prices[0]
    price += st*prices[2]
    price += ct*prices[1]
    price += g*prices[4]
    print(price)


    return (familycount,at,st,ct,g)
def purchase():
  prices = [20,12,16,60,15]
  adults = 0
  children = 0
  senior = 0
  price = 0
  i = 0
  people = 0
  buy = input("buy tickets? Y/N ")
  while(buy == "Y"):
    day = (input("1 day or 2 days?"))
    while True:
      if (day.isnumeric() == True):
        break
      else:
        day = (input("1 day or 2 days? "))
    if (int(day) == 2):
      prices = [30,18,24,90,22.5]
    ticketnumber = (input("how many tickets? "))
    while True:
      if (ticketnumber.isnumeric() == True):
        break
      else:
        ticketnumber = (input("how many tickets? "))
    
    n = 1
    while (n <= int(ticketnumber)):
      ticket = input("Input Ticket ")  
      if(ticket == "adult"):
        price += prices[0]
        n +=1
        people +=1
      elif(ticket == "child"):
        price += prices[1]
        n+=1
        people += 1
      elif(ticket == "senior"):
        price += prices[2]
        n+=1
        people +=1
      elif(ticket == "family"):
        price += prices[3]
        n+=1
        people += 5
      elif(ticket == "group"):
        n+=1
        while True:
          groups = int(input("how many in the group "))
          if (groups >= 6):
            price +=  prices[4] * groups
            people += groups
            break
          else:
             groups = int(input("how many in the group "))
      else:
        ticket = input("Input Ticket ")
    attraction = "start"
    while(attraction != "exit"):
      attraction = input("Input attraction -- exit to leave: ")
      
      if (int(day)==2):
          if(attraction == "bbq"):

            price += 5*people
      if (attraction == "penguin"):
        price += 2*people
      elif (attraction == "lion"):
        price += 2.5*people
    i += 1
    print(price)
    price = 0
    print ("booking number: " + str(i))
    #For the Family estimation
    if (adults >1 & children == 2):
      print("hi")   
      adults -= 2
      children -=2
      price += 60
    elif (adults>1 & children >2):
      adults -=2
      children -=3
      price += 60
    adults = int(input("amount of adults "))
    children = int(input("amount of children "))
    senior = int(input("amount of seniors "))
    print (discount(adults,senior,children))
    buy = input("buy tickets? Y/N ")

purchase()
