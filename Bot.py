import tgflow as tgf
from tgflow import TgFlow as tgf
from tgflow import handles as h
from enum import Enum
import requests
import json
from random import *
from time import *
seed(clock())
key='580697921:AAGs431pN6O5tDS20Ar2kFcx74aAQ6r7j2s'
mems = [['mem.png',0],'mem1.jpg','mem2.jpg','mem3.jpg','mem4.jpg','troolface.png']
def hse(i):
	#p = open(choice(mems),'rb')
    if i.text=='Да' or i.text=='да':
        tgf.bot.send_message(i.chat.id,'А он тебя не хочет')
    if i.text=='Нет' or i.text=='нет':
        tgf.bot.send_message(i.chat.id,'А он тебя хочет')
    """
    a = i.location
    bi = str(a).split(",")[0].split(": ")[1]
    bi2 = str(a).split(",")[1].split(": ")[1].split("}")[0]
    r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=burgerking&radius=6000&language=ru&opennow&location='+bi+','+bi2+'&key=AIzaSyDMkPyS3cWd1qIDDXYQHSLJ4PrV6ILkgVw')
    tp = r.text
    par_json = json.loads(tp)
    ft2 = str(par_json['results'][0]['geometry']["location"]["lat"])
    ft3 = str(par_json['results'][0]['geometry']["location"]["lng"])
    tgf.bot.send_location(i.chat.id,ft2,ft3)"""
    return States.START

class States(Enum):
    START=1
UI = {
    States.START:
    {'t':'Хочешь прекол?',
     'react':h.action(hse, react_to = 'text',update_msg=False),
     },
    }
tgf.configure(token=key,state=States.START,data={"foo":'bar'})
tgf.start(UI)
