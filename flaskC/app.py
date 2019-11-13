from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
from flaskC.CB import CB
import yaml

app = Flask(__name__)

app.secret_key = b'\x0f~\xcfK\x08XML\x8f!\xb5\x05?\x1a9yE\x18"L\xf2\x08\x84o'

idioms = ""

chat_bot_storage = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer = ChatterBotCorpusTrainer(chat_bot_storage)
trainer.train("chatterbot.corpus.italian")

def startIdiomCombo():
    with open("comboIdiom.yaml", 'r') as stream:
        idioms = yaml.load(stream)
    return idioms

@app.route("/")
def home():
    idioms = startIdiomCombo()
    return render_template("index.html", idioms=idioms)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    idiom = request.args.get('optIdiom');
    if idiom == 'Spagnolo':
        trainer = ChatterBotCorpusTrainer(chat_bot_storage)
        trainer.train("chatterbot.corpus.spanish")
        return str(chat_bot_storage.get_response(userText))
    elif idiom == 'Portoghese':
        trainer = ChatterBotCorpusTrainer(chat_bot_storage)
        trainer.train("chatterbot.corpus.portuguese")
        return str(chat_bot_storage.get_response(userText))
    elif idiom == 'Inglese':
        trainer = ChatterBotCorpusTrainer(chat_bot_storage)
        trainer.train("chatterbot.corpus.english")
        return str(chat_bot_storage.get_response(userText))
    else:
        return str(chat_bot_storage.get_response(userText))

def popup():
    root = Tk()
    cb = CB()
    msg = cb.listenMessage(root)
    return msg
    #root.mainloop()

@app.route("/popupTk", methods=['GET', 'POST'])
def openPopup():
    userText = popup()
    idiom = request.args.get('optIdiom');
    if idiom == 'Spagnolo':
        trainer = ChatterBotCorpusTrainer(chat_bot_storage)
        trainer.train("chatterbot.corpus.spanish")
        return userText + ";" + str(chat_bot_storage.get_response(userText))
    elif idiom == 'Portoghese':
        trainer = ChatterBotCorpusTrainer(chat_bot_storage)
        trainer.train("chatterbot.corpus.portuguese")
        return userText + ";" + str(chat_bot_storage.get_response(userText))
    elif idiom == 'Inglese':
        trainer = ChatterBotCorpusTrainer(chat_bot_storage)
        trainer.train("chatterbot.corpus.english")
        return userText + ";" + str(chat_bot_storage.get_response(userText))
    else:
        return userText + ";" + str(chat_bot_storage.get_response(userText))

if __name__ == "__main__":
    app.run()


