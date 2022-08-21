import telebot
import json
import asyncio

#Load Secrets
with open('secrets.json','r') as f:
    API_KEY = json.load(f)['API_KEY']

# t.me/phelipecomphFAQ_bot
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['geral'])
def answer_skills(message):
    text = "O Phelipe é um desenvolvedor focado em Dados e Automação"
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['habilidades'])
def answer_skills(message):
    text = "O Phelipe sabe muuito de Python, SQL, criação de DashBoards e ChatBots"
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['contato'])
def answer_skills(message):
    text = """Você pode falar com o Phelipe por um dos canais a baixo:
Linkedin: https://www.linkedin.com/in/phelipecomph/
Email: phelipecomph42@gmail.com
WhatsApp: (34) 984256742
Telegram: https://t.me/phelipecomph"""
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projetos'])
def answer_skills(message):
    text = """Tem 4 projetos que conheço bem, clique eu um dele para saber mais!:
/projeto1 Dashboard de Métricas Ágeis
/projeto2 Chatbot de Resultados no Discord
/projeto3 Bot de Telegram que centraliza mensagens
/projeto4 Eu!
"""
    bot.send_message(message.chat.id,text)
    
@bot.message_handler(commands=['projeto1'])
def answer_skills(message):
    text = """Dashboard de Métricas Ágeis"""
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projeto2'])
def answer_skills(message):
    text = """Chatbot de Resultados no Discord"""
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projeto3'])
def answer_skills(message):
    text = """Bot de Telegram que centraliza mensagens"""
    bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projeto4'])
def answer_skills(message):
    text = """Eu sou um simples bot Portfolio, respondo perguntas no formato de FAQ sobre meu desenvolvedor e outros projetos dele!
Obrigado por perguntar!
É um prazer te conhecer"""
    bot.send_message(message.chat.id,text)

def verify(message):
    return True

@bot.message_handler(func=verify)
def answer(message):
    text = """Olá eu sou o Bot do Phelipe com Ph!
Eu funciono como um portfolio!
Clique nas opções abaixo e eu te contarei um pouco mais sobre o Phelipe
/geral
/projetos
/habilidades
/contato
E se quiser ver com mais detalhes dá uma olhada no portfolio completo dele!
https://phelipecomph.github.io/"""
    bot.reply_to(message,text)


async def asyncbot():
    bot.polling()

while True:
    asyncio.run(asyncbot())
