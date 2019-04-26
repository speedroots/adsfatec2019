import telepot
from Estimulus import Estimulus

token = telepot.Bot("750732573:AAFdeaN9Ut9Z-0Uuc-zMboyHjAeMSvE6yyo")
bot = Estimulus("Estimulus")

def RecebeMSG(msg):
    frase = bot.escuta(frase = msg['text'])
    respostas = bot.pensa(frase)
    bot.fala(respostas)
    #chatID = msg ['chat']['id']
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    token.sendMessage(chatID,respostas)


token.message_loop(RecebeMSG)

while True:
    pass
 
    
