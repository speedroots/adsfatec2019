'''
Autor: Rafael Marques de Almeida
Projeto: 1ª Parte Chatbot pelo Telegram
Curso: Análise e Desenvolvimento de Sistemas
Interação Humano Computador(IHC) - Professor Giuliano Araújo Bertoti
'''
import telepot
from Estimulus import Estimulus

token = telepot.Bot("750732573:AAFdeaN9Ut9Z-0Uuc-zMboyHjAeMSvE6yyo")
bot = Estimulus("Estimulus")

def RecebeMSG(msg):
   
    frase = bot.escuta(frase = msg['text'])
    respostas = bot.pensa(frase)
    chatID = msg ['chat']['id']
    token.sendMessage(chatID,respostas)

token.message_loop(RecebeMSG)

while True:
    pass