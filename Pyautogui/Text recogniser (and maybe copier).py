import pyautogui
import keyboard
import requests
from pytesseract import pytesseract
from PIL import Image
import time
APIKEY = "Wql2SW6qkFZH"

#
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pyautogui.PAUSE = 0.1
pytesseract.tesseract_cmd = path_to_tesseract
while True:
    if keyboard.is_pressed('.'):
        #pyautogui.screenshot('picture.png', region = (270,430,1400,250))
        pyautogui.screenshot('picture.png', region = (270,230,1400,750))
        break    

url = "https://random-stuff-api.p.rapidapi.com/ai"




image_path = r"picture.png"
print(pyautogui.position())
img = Image.open(image_path)
text = pytesseract.image_to_string(img)
#print(text[:-1])
texts = (text[:-1].replace("\n"," ")).lower()
print(texts)
querystring = {"msg":"Hi there, how are you? (REQUIRED) Can you synthesize this information? ","bot_name":"Random Stuff Api (OPTIONAL)","bot_gender":"male (OPTIONAL)","bot_master":"PGamerX (OPTIONAL)","bot_age":"19 (OPTIONAL)","bot_company":"PGamerX Studio (OPTIONAL)","bot_location":"India (OPTIONAL)","bot_email":"admin@pgamerx.com (OPTIONAL)","bot_build":"Public (OPTIONAL)","bot_birth_year":"2002 (OPTIONAL)","bot_birth_date":"1st January, 2002 (OPTIONAL)","bot_birth_place":"India (OPTIONAL)","bot_favorite_color":"Blue (OPTIONAL)","bot_favorite_book":"Harry Potter (OPTIONAL)","bot_favorite_band":"Imagine Doggos (OPTIONAL)","bot_favorite_artist":"Eminem (OPTIONAL)","bot_favorite_actress":"Emma Watson (OPTIONAL)","bot_favorite_actor":"Jim Carrey (OPTIONAL)","id":"For customised response for each user"}

headers = {
    'authorization': "Wql2SW6qkFZH",
    'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
    'x-rapidapi-key': "Wql2SW6qkFZH"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
#pyautogui.write(texts,interval=0.1)
