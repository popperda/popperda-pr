import requests

#make the request
r = requests.get('https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=player&timeframe=alltime').json()
search = input("who do you want to find? ")
a = requests.get('https://api.wynncraft.com/v2/player/'+str(search)+'/stats').json()
try:    
    print(a['data'][0]['username'])
    print(a['data'][0]['rank'])
    print(a['data'][0]['meta']['firstJoin'])
    print(a['data'][0]['meta']['lastJoin'])
    print((a['data'][0]['meta']['playtime'])//60 )
    print(a['data'][0]['meta']['location']['server'])
    print(a['data'][0]['global']['totalLevel'])
    print((a['data'][0]['global']['blocksWalked']) )
    print(a['data'][0]['global']['logins'])
    print(a['data'][0]['global']['deaths'])
    print(a['data'][0]['ranking']['player']['solo']['combat'])
    print(a['data'][0]['classes'][0]['name'])
    print(a['data'][0]['classes'][0]['quests']['list'])
    print(a['data'][0]['classes'][0]['professions']['combat']) #level and percentage to next level
    print([a['data'][0]['classes'][0]['skills']])
except IndexError:
    print("No player with such name!")
#get the data
toep = (input("top how much? "))
top = int(toep)
max = len(r['data'])

#Print the data
for n in range(top):

    print(r['data'][n]['name'])

