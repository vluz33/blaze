import requests
from flask import Flask, jsonify

app=Flask(__name__)

#criacao dos recursos
link1 = 'https://blaze.com/api/roulette_games/current'
req1=requests.get(link1)
d1=req1.json()


#unico endpoint
@app.route('/')
def homepage():
  if d1['color']==0:
    token ='6078935508:AAGfzFwISS11HHzF6HlJI5WwjdL_8ZiqYh4'
    chat_id = '-1001911037404'
    message='\U00002b1c'
    URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message
    resposta = requests.get(URL)
    return d1

#localhost
app.run(port=5000,host='localhost',debug=True)
