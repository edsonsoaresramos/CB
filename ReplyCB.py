from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('ReplyChatBot')
trainer = ListTrainer(bot)

conversazioni = open('ReplyChats.txt','r').readlines()
trainer.train(conversazioni)

trainer.train(conversazioni)

while True:
    messaggio = input('Tu: ')
    if messaggio.strip() != 'se vedemo':
        reply = bot.get_response(messaggio)
    print('ReplyChatBot: ', reply)
    if messaggio.strip() == 'se vedemo':
        print('ReplyChatBot:Ciao se beccamo')
        break

