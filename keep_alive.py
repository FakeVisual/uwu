from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "im up bitch"

def run():
  app.run(host='0.0.0.0',port=1919

def keep_alive():  
    t = Thread(target=run)
    t.start()
