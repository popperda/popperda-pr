from flask import Flask,request, render_template,redirect
from typing import NewType, Text
import requests
from requests.api import post
import flask_login
import sqlite3
import uuid
import hashlib
from datetime import datetime
import create_account
from flask_socketio import SocketIO, emit

path = '/home/jatrhead/path/to/flask_app_directory'
#just checking name probably the userx
app = Flask(__name__)
database_filename = "tasker.db"
app.config['SECRET_KEY'] = 'lksdj fksdf skdjf ,sdf sdf ks,djferj seflkjwerekr'
socketio = SocketIO(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    def __init__(self, userid, email, name):
        self.id =userid
        self.email = email
        self.name = name
    def get_dict(self):
        return{"userid": self.id, "email": self.email, "name": self.name}
@login_manager.user_loader
def load_user(userid):
    users = database_read(f"SELECT * FROM accounts WHERE userid = '{userid}';")
    if len(users) !=1:
        return None
    user = User(users[0]['userid'],users[0]['email'],users[0]['name'])
    user.id = userid
    return user

def database_write(sql, data = None):
    connection = sqlite3.connect(database_filename)
    connection.row_factory = sqlite3.Row
    db = connection.cursor()
    if data:
        rows_affected = db.execute(sql,data).rowcount
    else:
        rows_affected = db.execute(sql).rowcount
    connection.commit()
    db.close()
    connection.close()
    return rows_affected
def database_read(sql, data = None):
    connection = sqlite3.connect(database_filename)
    connection.row_factory = sqlite3.Row
    db = connection.cursor()
    if data:
        db.execute(sql, data)
    else:
        db.execute(sql)
    records = db.fetchall()
    rows = [dict(record) for record in records]
    db.close()
    connection.close()
    return rows
    
def bazaarsearch(a):
    
    item = a
    data = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&productId={item}").json()
    
    try:
        print(data["products"][item]["buy_summary"][0]["pricePerUnit"])
        print(data["products"][item]["sell_summary"][0]["pricePerUnit"])
        print(data["products"][item]["buy_summary"][0]["amount"])
        a= (data["products"][item]["buy_summary"][0]["pricePerUnit"])
        b= (data["products"][item]["sell_summary"][0]["pricePerUnit"])
        c = int(a-b)
        return c
    except KeyError:
        return "nothing found, sorry. Try reformatting."
        
def search(a):
    items = a
    print(items)
    datatwo = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyDOCVpIpvA9nDCFD4T7jU2XjdvWeVk_gAw&cx=7e0287b28799017cb&q="+ str(items) ).json()
    data = datatwo["items"][0]["link"]
    data1 = datatwo["items"][1]["link"]
    data3 = datatwo["items"][2]["link"]

    dataone = (data,data1,data3)
   
    return (dataone)
    
def bazaarcheck():
    from typing import NewType
    import requests
    # gets in json


    dataone = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&page=0").json()
    # gets the auctions

    auction1 = dataone["products"]
    #with pages
    totalbazaar = []
    items = []

    i=0
    data = requests.get("https://api.hypixel.net/skyblock/bazaar?c8262998-f925-414d-8c84-a17accddec0a&productId={item}").json()
    # adds the auction that is a bin
    tempprice = 0
    tempsell = 0
    profit = []
  




    try: 
        
        for a in data["products"]:
            print(a)
            tempprice = int(data["products"][a]["buy_summary"][0]["pricePerUnit"])
            tempsell = int(data["products"][a]["sell_summary"][0]["pricePerUnit"])
            product = tempprice-tempsell
            profit.append([a,product])
        #enchanted carrot on stick broken + bazaar cookie for some reason remove them from products
        #print(profit)
    except IndexError:
        
        for a in data["products"]:
            if a != "ENCHANTED_CARROT_ON_A_STICK" :
                if a != "BAZAAR_COOKIE":
                    print(a)
                    c= (data["products"][a]["buy_summary"][0]["pricePerUnit"])
                    b= (data["products"][a]["sell_summary"][0]["pricePerUnit"])
                    pro = (c-b)
                    profit.append([a,pro])
    profit.sort(key=lambda x:x[1], reverse=True)
    print(profit)
    return profit
def help(b):
    import requests


#make the request
    r = requests.get('https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=player&timeframe=alltime').json()
    a = requests.get('https://api.wynncraft.com/v2/player/'+str(b)+'/stats').json()
    data = []
    try:    
        user =(a['data'][0]['username'])
        rank = (a['data'][0]['rank'])
        firstlog = (a['data'][0]['meta']['firstJoin'])
        recentlog = (a['data'][0]['meta']['lastJoin'])
        playtime =((a['data'][0]['meta']['playtime'])//60 )
        wc = (a['data'][0]['meta']['location']['server'])
        Levels=(a['data'][0]['global']['totalLevel'])
        travelled = ((a['data'][0]['global']['blocksWalked']) )
        logins = (a['data'][0]['global']['logins'])
        deaths = (a['data'][0]['global']['deaths'])
        combrank =(a['data'][0]['ranking']['player']['solo']['combat'])
        mainclass=(a['data'][0]['classes'][0]['name'])
        quests =(a['data'][0]['classes'][0]['quests']['list'])
        levelpercent=(a['data'][0]['classes'][0]['professions']['combat']) #level and percentage to next level
        skills = ([a['data'][0]['classes'][0]['skills']])
        data.append(user)
        data.append(rank)
        data.append(firstlog)
        data.append(recentlog)
        data.append(playtime)
        data.append(wc)
        data.append(Levels)
        data.append(travelled)
        data.append(logins)
        data.append(deaths)
        data.append(combrank)
        data.append(mainclass)
        data.append(quests)
        data.append(levelpercent)
        data.append(skills)
        print(data)
    except IndexError:
        print("No player with such name!")
        t = []
        t.append("No Player With Such Name!")
        return t
    return data 
def auction(a):
    data = requests.get("https://api.hypixel.net/skyblock/auctions").json()
    
    dataone = requests.get("https://api.hypixel.net/skyblock/auctions").json()


    auction1 = dataone["auctions"]
    #with pages
    totalauction = []
    items = []
    item2 = []
    item = a
    i=0
    total = data["totalPages"]
    # adds the auction that is a bin
    while i != total:
        updatepage = requests.get("https://api.hypixel.net/skyblock/auctions?c8262998-f925-414d-8c84-a17accddec0a&page="+str(i)).json()
        auctions = updatepage["auctions"]
        
        totalauction += auctions
        i+=1
        for auction in auctions:
            try:
                if auction["bin"] :
                    if str(auction["item_name"]).count(item.title()) > 0:
                        items.append([auction["item_name"],auction["starting_bid"],  auction["category"], auction["auctioneer"]])
                else:
                    if str(auction["item_name"]).count(item.title()) > 0:
                        item2.append([auction["item_name"],auction["starting_bid"],  auction["category"], auction["auctioneer"]])
                    
            except KeyError:
                pass
    #  for auctionaa in auctions:
            #try:
                #if auctionaa["bin"]:
                    #if str(auctionaa["item_name"]).count(item.title()) > 0:
                        #item2.append([auctionaa["item_name"], auctionaa["starting_bid"], auctionaa["category"], auctionaa["auctioneer"]])
            #except KeyError:
                #pass
        

    Newvalue = []
    OldValue = []
    item2.sort(key=lambda x:x[1])
    # sorts by the prices, use items.sort(key=lambda x:x[1], reverse=True) for highest prices first
    items.sort(key=lambda x:x[1])

    return items
  

    
  

    


@app.route("/")
def index_page():
    if flask_login.current_user.is_authenticated:

        return render_template("Homepage.html")
    else:
        return redirect("/Enter")

@app.route("/new_folder",methods=["POST"])
@flask_login.login_required
def create_new_folder():
    form = dict(request.values)
    id = str(uuid.uuid1())
    form['id'] = id
    sql = f"INSERT INTO folders (userid,id,name) VALUES (:userid,'{id}',:name);"
    ok = database_write(sql, form)
    if ok == 1:
        return "OK"
    else:
        return "ERROR"
@app.route("/save_task", methods=["POST"])
def task_update():
    form = dict(request.values)
    id = form['id']
    folderid = form['folderid']
    print("Form information received", form)
    if "submit-close" in form:
        form['status'] = "Completed"
    if "submite-delete" in form:
        database_write(f"DELETE FROM tasks WHERE id={id};")
        return redirect(f"/main?folderid={folderid}")
    if id == "":
        id = str(uuid.uuid1())
        form['id'] = id
        form['link'] = ""
        form['created'] = datetime.now().strftime("%Y-%m-%d")
        sql= """INSERT INTO tasks
        (userid,folderid,id,title,due,reminder,created,category,priority,status,notes,link) VALUES
        (:userid,:folderid,:id,:title,:due,:reminder,:created,:category,:priority,:status,:notes,:link); """
        ok = database_write(sql,form)
    else:
        form['link']= ""
        sql = """UPDATE tasks SET title =:title, due=:due, reminder=:reminder, category=:category, priority=:priority, status=:status, notes=:notes, link=:link WHERE id =:id"""
        ok = database_write(sql,form)
    if ok == 1:
        return redirect("/home")
        return redirect(f"/main?folderid={folderid}&id={id}")
        
    else:
        return redirect(f"/error?folderid={folderid}&id={id}") 
@app.route("/error")
def error_page():
    return("ERROR")
@app.route("/wynn")
@flask_login.login_required
def wynns():

    return render_template('Template1 - Copy.html')   
@app.route("/wynn", methods = ["POST"])

def wynn():
   text = request.form['text']
   datas = help(text)
   return render_template('Wynn.html', datas=datas)


@app.route("/home")
@flask_login.login_required
def home():
    folderid = "0"
    if 'folderid' in request.values:
        folderid = request.values['folderid']
    id = "1"
    if 'id' in request.values:
        id = request.values['id']
    print(id)
    user = flask_login.current_user.get_dict()
    folders = database_read(f"SELECT * FROM folders WHERE userid ='{user['userid']}' ORDER BY name;")
    items = database_read(
        f"SELECT * FROM tasks WHERE folderid='{folderid}' AND status != 'Completed' AND userid='{user['userid']}';")
    maintask = database_read(
        f"SELECT * FROM tasks WHERE id ='{id}' AND userid = '{user['userid']}';"
    )
    if len(maintask)==1:
        maintask = maintask[0]
    else:
        maintask= {}
   
    return render_template('main-original1.html', personName="Jared",folders=folders, user=user, tasks=items,
    maintask=maintask, folderid=folderid, id=id)
@app.route("/login")
def login():
    return"Login Here. Pass=_____ User=____"
@app.route("/logout")
def logout():
    flask_login.logout_user()
    return"Please do not leave"
@app.route("/register", methods = ['GET'])
def register():

    return render_template('Registerpage.html')
@app.route("/register", methods = ['POST'])
def registers():
    try: 
        form = dict(request.values)
        print(form['email'])
        create_account.create_account(form['userid'],form['email'],form['name'],form['password'])
        return render_template('Template1.html')
    except:
        return render_template('Registerpage.html', error = "Sorry, this username has been TAKEN")

@app.route('/Enter', methods = ['GET'])
def Enter():
    
   return render_template('Template1.html', alert=" ")
@app.route('/Enter', methods = ['POST'])
def Enter_request():
    form = dict(request.values)
    users = database_read("SELECT * FROM accounts WHERE userid=:userid",form)
    if len(users) ==1:
        salt = users[0]['salt']
        saved_key = users[0]['password']
        generated_key = hashlib.pbkdf2_hmac(
            'sha256',
            form['password'].encode('utf-8'),
            salt.encode('utf-8'),
            10000 ).hex()
        if saved_key == generated_key:
            user = load_user(form['userid'])
            flask_login.login_user(user)
            return render_template("Homepage.html")
        else: 
            return render_template("Template1.html", alert="INVALID USER or PASSWORD. TRY AGAIN.")
    else:
        return render_template("Template1.html", alert="INVALID USER or PASSWORD. TRY AGAIN.")
    
@app.route('/sb')
def sb():
# gets in json

    return render_template('Template1 - Copy.html')   
@app.route('/sb', methods = ['POST'])
def sb_search():
# gets in json
   text = request.form['text']
   item1 = auction(text)
   return render_template('AuctionSearchup.html',text=text, item1 = item1)

@app.route('/meeopp')
def meeopp(): 
   return render_template('ABOUTME.html')
#we doing some learning and subjects - for my own revision, and also to help others (possibly LOL)
@app.route('/learning')
def learning():
    return render_template('Learning.html')
@app.route('/learning', methods = ['POST'])
def learningsearch():
    text = request.form['text']
@app.route('/bazaar')
def bazaarchecks():
    bazaarlist = bazaarcheck()
    return render_template("Bazaarcheck.html",bazaarlist=bazaarlist)
@app.route('/bazaar', methods = ['POST'])
def bazaar_search():
# gets in json
   text = request.form['text']
   item1 = bazaarsearch(text)
   return render_template('Bazaarsearch.html',text=text, item1 = item1)
@app.route('/mario')
def trte():
    return render_template('Mario Game.html')
@app.route('/quick')
def quick():
   
   return render_template('Bazaarcheck.html')
@app.route('/quick', methods = ['POST'])
def quicksearch():
   text = request.form['text']
   item1 = search(text)
   return render_template('Bazaarsearch.html',text=text, item1 = item1)
@app.route('/chat')
@flask_login.login_required


def index():
    user = flask_login.current_user.get_dict()
    return render_template('chat.html', user=user)
@socketio.on('client_message')
def receive_message (client_msg):
    emit('server_message', client_msg, broadcast=True)
@app.route('/chat2', methods = ['POST'])
def it():
    text = request.form['text']
    sql = f"INSERT INTO Messages1(channel) VALUES ('{text}');"
    folders = database_write(sql,text)
@app.route('/chat2', methods = ['GET'])
def its():
    folders = database_read(f"SELECT * FROM Messages1 WHERE 1=1 ;")
    return render_template("chat2.html",folders=folders)


if __name__ == "__main__":
    socketio.run(app)
    #this allows it to run on any network, thats why there is 0.0.0.0 
    # like the web router things, port is the computers
    #the port number is lika flat number in a building
    # so essentially its saying go to a building then send this package
    #to a particular program
    app.run(host="0.0.0.0", port=80, debug=True)
#USING HTML LETS GOOOOO
# revision remember
#there are opening and ending tags
# example: <p> Hello </p> to end, we can add images etc
# a href: hyperlink
#image= <img src="picture link.jpg">
# divs <div></div>
#we can have classes for divs
# <div class = "Green"> then <p>hi</p> </div>
# Css is the painitng and stuff, HTML is structure is basically that