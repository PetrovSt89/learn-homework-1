"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import ephem

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

def greet_user(update, context):
    logger.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    logger.info(user_text)
    update.message.reply_text(user_text)

def planets(update, context):
    textT = update.message.text
    textT = textT.split()
    planet_name =textT[1]
    if planet_name == 'Mars':
        planet = ephem.Mars('2023/02/16')
    elif planet_name == 'Pluto':
        planet = ephem.Pluto('2023/02/16')
    else:
        update.message.reply_text('Я не знаю таких планет')
        return
    planet = ephem.constellation(planet)
    logger.info('Вызван /planet')
    update.message.reply_text(planet)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
