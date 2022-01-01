from urllib.parse import urlencode
import requests
import json

def detect(word):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"
    word = word
    entry = {"q":word}
    payload = urlencode(entry)

    headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "54a24f1846msh64def632ccd4350p1e97e4jsn1749b28f76ab"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = json.loads(response.text)
    return result["data"]["detections"][0][0]["language"]

        
    
def translate(t,tarlang,sorlan):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    text = t
    targetlang = tarlang
    sorcelang = sorlan
    entry = {"q":text,"target":targetlang,"source":sorcelang}
    payload = urlencode(entry)

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "54a24f1846msh64def632ccd4350p1e97e4jsn1749b28f76ab"
        }
    response = requests.request("POST",url, data=payload, headers=headers)
    result = json.loads(response.text) 
    return result["data"]["translations"][0]["translatedText"]


text = input("what is your word: ")
lang = input("enter languge like 'en''es''ar': ")
dlnag = detect(text)
trn = translate(text,lang,dlnag)
print(trn)
