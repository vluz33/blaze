import requests
from flask import Flask, jsonify
import pandas as pd



app=Flask(__name__)

@app.route('/')
def homepage():
  return 'funciona'

link='https://blaze.com/api/roulette_games/current'
ler=requests.get(link)
d=ler.json()
#print (d)

@app.route('/mandarmensagem')
def mandar():
  token ='6078935508:AAGfzFwISS11HHzF6HlJI5WwjdL_8ZiqYh4'
  chat_id = '-1001911037404'
  if d['color']==0:
      message='\U00002b1c'
      URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message
      resposta = requests.get(URL)
  return 'a'

app.run(host='0.0.0.0')
