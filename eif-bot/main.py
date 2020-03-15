#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import logging
import telegram
from datetime import datetime
from shedule_scrapper import get_dict
import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

#!/usr/bin/python3
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, RegexHandler
from telegram.ext.filters import Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


############################### Bot ############################################
def start(bot, update):
    update.message.reply_text(start_message(update),
                              reply_markup=main_menu_keyboard())



def main_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def eif_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=course_menu_message(),
                        reply_markup=eif_menu_keyboard())

def sbd_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=course_menu_message(),
                        reply_markup=sbd_menu_keyboard())


def pe_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=course_menu_message(),
                        reply_markup=pe_menu_keyboard())


def eif_submenu1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Выбери количество дней:',
                          reply_markup=eif1_submenu_keyboard())


def eif_submenu1_days(bot, update):

    query = update.callback_query
    global shedule
    rasp_list = shedule['ЭиФ'][1]
    n_days = int(query.data[-1])
    user = query.from_user
    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, 'выбрал(а) ЭиФ 1 курс на {} дня(ей)'.format(n_days)))
    rasp = "".join(rasp_list[:n_days]) + shedule['Дата']
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Расписание:\n{}'.format(rasp),
                          reply_markup=eif1_submenu_keyboard(), parse_mode=telegram.ParseMode.MARKDOWN)




def eif_submenu2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Выбери количество дней:',
                          reply_markup=eif2_submenu_keyboard())

def eif_submenu2_days(bot, update):
    query = update.callback_query
    global shedule
    rasp_list = shedule['ЭиФ'][2]
    n_days = int(query.data[-1])
    user = query.from_user

    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, 'выбрал(а) ЭиФ 2 курс на {} дня(ей)'.format(n_days)))
    rasp = "".join(rasp_list[:n_days]) + shedule['Дата']
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Расписание:\n{}'.format(rasp),
                          reply_markup=eif2_submenu_keyboard(), parse_mode=telegram.ParseMode.MARKDOWN)

def sbd_submenu1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Выбери количество дней:',
                          reply_markup=sbd1_submenu_keyboard())

def sbd_submenu1_days(bot, update):
    query = update.callback_query
    global shedule
    rasp_list = shedule['СБД'][1]
    n_days = int(query.data[-1])
    user = query.from_user

    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, 'выбрал(а) СБД 1 курс на {} дня(ей)'.format(n_days)))
    rasp = "".join(rasp_list[:n_days]) + shedule['Дата']
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Расписание:\n{}'.format(rasp),
                          reply_markup=sbd1_submenu_keyboard(), parse_mode=telegram.ParseMode.MARKDOWN)


def sbd_submenu2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Выбери количество дней:',
                          reply_markup=sbd2_submenu_keyboard())

def sbd_submenu2_days(bot, update):
    query = update.callback_query
    global shedule
    rasp_list = shedule['СБД'][2]
    n_days = int(query.data[-1])
    user = query.from_user

    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, 'выбрал(а) СБД 2 курс на {} дня(ей)'.format(n_days)))
    rasp = "".join(rasp_list[:n_days]) + shedule['Дата']
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Расписание:\n{}'.format(rasp),
                          reply_markup=sbd2_submenu_keyboard(), parse_mode=telegram.ParseMode.MARKDOWN)



def pe_submenu1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Выбери количество дней:',
                          reply_markup=pe1_submenu_keyboard())

def pe_submenu1_days(bot, update):
    query = update.callback_query
    global shedule
    rasp_list = shedule['ПЭ'][1]
    n_days = int(query.data[-1])
    user = query.from_user

    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, 'выбрал(а) ПЭ 1 курс на {} дня(ей)'.format(n_days)))
    rasp = "".join(rasp_list[:n_days]) + shedule['Дата']
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Расписание:\n{}'.format(rasp),
                          reply_markup=pe1_submenu_keyboard(), parse_mode=telegram.ParseMode.MARKDOWN)

def pe_submenu2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Выбери количество дней:',
                          reply_markup=pe2_submenu_keyboard())


def pe_submenu2_days(bot, update):
    query = update.callback_query
    global shedule
    rasp_list = shedule['ПЭ'][2]
    n_days = int(query.data[-1])
    user = query.from_user
    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, 'выбрал(а) ПЭ 2 курс на {} дня(ей)'.format(n_days)))
    rasp = "".join(rasp_list[:n_days]) + shedule['Дата']
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='Расписание:\n{}'.format(rasp),
                          reply_markup=pe2_submenu_keyboard(), parse_mode=telegram.ParseMode.MARKDOWN)


############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Экономика и финансы', callback_data='me')],
              [InlineKeyboardButton('Системы больших данных в экономике', callback_data='ms')],
              [InlineKeyboardButton('Поведенческая экономика', callback_data='mp')]]
  return InlineKeyboardMarkup(keyboard)


def eif_menu_keyboard():
  keyboard = [[InlineKeyboardButton('1 курс', callback_data='me_1')],
              [InlineKeyboardButton('2 курс', callback_data='me_2')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)


def sbd_menu_keyboard():
  keyboard = [[InlineKeyboardButton('1 курс', callback_data='ms_1')],
              [InlineKeyboardButton('2 курс', callback_data='ms_2')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)


def pe_menu_keyboard():
  keyboard = [[InlineKeyboardButton('1 курс', callback_data='mp_1')],
              [InlineKeyboardButton('2 курс', callback_data='mp_2')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)


def eif1_submenu_keyboard(): # прописать дни
  keyboard = [[InlineKeyboardButton('1 день', callback_data='me1_1')],
              [InlineKeyboardButton('3 дня', callback_data='me1_3')],
              [InlineKeyboardButton('5 дней', callback_data='me1_5')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def eif2_submenu_keyboard(): # прописать дни
  keyboard = [[InlineKeyboardButton('1 день', callback_data='me2_1')],
              [InlineKeyboardButton('3 дня', callback_data='me2_3')],
              [InlineKeyboardButton('5 дней', callback_data='me2_5')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)


def sbd1_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('1 день', callback_data='ms1_1')],
              [InlineKeyboardButton('3 дня', callback_data='ms1_3')],
              [InlineKeyboardButton('5 дней', callback_data='ms1_5')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def sbd2_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('1 день', callback_data='ms2_1')],
              [InlineKeyboardButton('3 дня', callback_data='ms2_3')],
              [InlineKeyboardButton('5 дней', callback_data='ms2_5')],
              [InlineKeyboardButton('Главное меню', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def pe1_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('1 день', callback_data='mp1_1')],
                [InlineKeyboardButton('3 дня', callback_data='mp1_3')],
                [InlineKeyboardButton('5 дней', callback_data='mp1_5')],
                [InlineKeyboardButton('Главное меню', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def pe2_submenu_keyboard():
    keyboard = [[InlineKeyboardButton('1 день', callback_data='mp2_1')],
                [InlineKeyboardButton('3 дня', callback_data='mp2_3')],
                [InlineKeyboardButton('5 дней', callback_data='mp2_5')],
                [InlineKeyboardButton('Главное меню', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def listener(update):
    user = update.message.from_user

    print('{} - {} {}[@{}]: {}'.format(datetime.now().strftime('%d-%m-%Y %H:%M'), user.first_name, user.last_name,
                                       user.username, update.message.text))


############################# Messages #########################################
def start_message(update):
    user = update.message.from_user
    one_emoji = bytes.decode(b'\xF0\x9F\x98\x8A', 'utf8')  # light_smile
    return 'Привет, {}!{}\n\nЭтот бот расскажет тебе о расписании магистратуры отделения экономики ЭМИТ РАНХИГС' \
               ' на ближайшие ' \
               'учебные дни.\n\nРасписание обновляется каждые 12 часов.\n' \
           'Выбери направление подготовки:'.format(user.first_name, one_emoji)


def main_menu_message():
    return 'Выбери направление подготовки:'


def course_menu_message():
    return 'Выбери курс:'


def days_menu_message():
    return 'Выбери количество дней:'


############################# Work #########################################
def callback_alarm(bot, job):
    global shedule
    shedule = get_dict()
    print('shedule has been prepared!')


def main():
    ############################# Handlers #########################################
    TOKEN = '845092429:AAEo5DslhGj0ZFMuRxkKMsiT2wLhqHOIPI8'
    updater = Updater(TOKEN)

    j = updater.job_queue
    j.run_repeating(callback_alarm, interval=43200, first=0)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(eif_submenu1, pattern='me_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(eif_submenu1_days, pattern='me1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(sbd_submenu1, pattern='ms_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(sbd_submenu1_days, pattern='ms1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(pe_submenu1, pattern='mp_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(pe_submenu1_days, pattern='mp1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(eif_submenu2, pattern='me_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(eif_submenu2_days, pattern='me2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(sbd_submenu2, pattern='ms_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(sbd_submenu2_days, pattern='ms2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(pe_submenu2, pattern='mp_2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(pe_submenu2_days, pattern='mp2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(eif_menu, pattern='me'))
    updater.dispatcher.add_handler(CallbackQueryHandler(sbd_menu, pattern='ms'))
    updater.dispatcher.add_handler(CallbackQueryHandler(pe_menu, pattern='mp'))

    updater.dispatcher.add_handler(RegexHandler(r'[а-яА-Я\w*\d*]', listener))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
################################################################################