import telebot
import requests

api_token = "YOUR_API_TOKEN"
bot = telebot.TeleBot(api_token)


def specific_category(category):
    response = requests.get(f"https://excuser-three.vercel.app/v1/excuse/{category}")
    data = response.json()
    return data[0]['excuse']


@bot.message_handler(commands=["family"])
def family(message):
    excuse = specific_category("family")
    bot.reply_to(message, f"Here's your family excuse:\n\n{excuse}")


@bot.message_handler(commands=["children"])
def children(message):
    excuse = specific_category("children")
    bot.reply_to(message, f"Here's your children excuse:\n\n{excuse}")


@bot.message_handler(commands=["college"])
def college(message):
    excuse = specific_category("college")
    bot.reply_to(message, f"Here's your college excuse:\n\n{excuse}")


@bot.message_handler(commands=["party"])
def party(message):
    excuse = specific_category("party")
    bot.reply_to(message, f"Here's your party excuse:\n\n{excuse}")


@bot.message_handler(commands=["funny"])
def funny(message):
    excuse = specific_category("funny")
    bot.reply_to(message, f"Here's your funny excuse:\n\n{excuse}")


@bot.message_handler(commands=["unbelievable"])
def unbelievable(message):
    excuse = specific_category("unbelievable")
    bot.reply_to(message, f"Here's your unbelievable excuse:\n\n{excuse}")


@bot.message_handler(commands=["developers"])
def developers(message):
    excuse = specific_category("developers")
    bot.reply_to(message, f"Here's your developers excuse:\n\n{excuse}")


@bot.message_handler(commands=["gaming"])
def gaming(message):
    excuse = specific_category("gaming")
    bot.reply_to(message, f"Here's your gaming excuse:\n\n{excuse}")


@bot.message_handler(commands=["office"])
def office(message):
    excuse = specific_category("office")
    bot.reply_to(message, f"Here's your office excuse:\n\n{excuse}")


@bot.message_handler(commands=["random"])
def random(message):
    response = requests.get(f"https://excuser-three.vercel.app/v1/excuse/")
    data = response.json()
    bot.reply_to(message, f"Here's your random excuse:\n\n<b>Category:</b> {data[0]['category']}\n\n<b>Excuse:</b>\n{data[0]['excuse']}", parse_mode="HTML")


bot.infinity_polling()
