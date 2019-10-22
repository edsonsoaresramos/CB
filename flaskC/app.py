from flask import Flask, render_template, request, make_response, redirect, url_for, session
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
from flaskC.CB import CB

app = Flask(__name__)

app.secret_key = b'\x0f~\xcfK\x08XML\x8f!\xb5\x05?\x1a9yE\x18"L\xf2\x08\x84o'

response = ""

italian_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(italian_bot)
trainer.train("chatterbot.corpus.italian")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(italian_bot.get_response(userText))

def popup():
    root = Tk()
    cb = CB()
    msg = cb.listenMessage(root)
    return msg
    #root.mainloop()

@app.route("/popupTk", methods=['GET', 'POST'])
def openPopup():
    userText = popup()
    return userText + ";" + str(italian_bot.get_response(userText))

if __name__ == "__main__":
    app.run()


