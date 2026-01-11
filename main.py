#python и telegram модули
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#стандартные модули проекта
import constants as c
import menu as btn
import utilites as u

#классы
import clases.Person as p
import clases.DAO as d

#обработчики
import handlers.handler_game as hg
import handlers.handler_cash as hc
import handlers.handler_life as hl
import handlers.handler_actives as ha

#опросы
import polls.new_game as ng
import polls.new_business as nb
import polls.change_active as ca
import polls.new_stocks as ns
import polls.new_bonds as nbnds
import polls.new_deposits as nd
import polls.new_auto as na
import polls.new_flight as nf
import polls.new_yacht as ny
import polls.new_mansion as nm
import polls.new_flats as nfl
import polls.new_lands as nl
import polls.new_chalets as nc
import polls.new_profession as np

class BotExceptionHandler(telebot.ExceptionHandler):
    def handle(self, exception):
        print('Произошла ошибка:', exception)
        u.logging.warning(f'Ошибка polling. ', f'Error: {exception}')
        return True

bot = telebot.TeleBot(u.get_from_env('TG_TOKEN'), exception_handler=BotExceptionHandler())
#bot = telebot.TeleBot(u.get_from_env('TG_TOKEN'))
u.bot = btn.bot = hg.bot = hc.bot = hl.bot = ha.bot = ng.bot = nb.bot = ca.bot = ns.bot = nbnds.bot = nd.bot = na.bot = nf.bot = ny.bot = nm.bot = nfl.bot = nl.bot = nc.bot = np.bot = bot
hg.curr_poll = curr_poll = None
d.DAO.bd_task(d.DAO.create_table)

@bot.message_handler(commands=['start'])
def welcome(message):
    file = open(c.IMG_WELCOME, 'rb')
    text =  c.TEXT_WELCOME + f'{message.from_user.first_name}!' + c.TEXT_WELCOME2
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Подробнее', callback_data='welcome'))
    bot.send_photo(message.chat.id, file, caption = text, reply_markup=markup)

def welcome2(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Начать игру', callback_data='new_game'))
    markup.add(InlineKeyboardButton('Продолжить игру', callback_data='continue_game'))
    markup.add(InlineKeyboardButton('Как пользоваться ботом?', callback_data='about_bot'))
    #markup.add(InlineKeyboardButton('Повар', callback_data='test'))
    bot.send_message(message.chat.id, c.TEXT_WELCOME3, reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:True)
def callback_messagge(callback):
    if callback.data == 'welcome':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        welcome2(callback.message)

    elif callback.data == 'new_game':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game_choise(callback.message)

    elif callback.data == 'new_game_blanc':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game(callback.message)

    elif callback.data == 'new_game_base':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game(callback.message, True)

    elif callback.data == 'new_game_list1':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game_list(callback.message, 'lvl1')

    elif callback.data == 'new_game_list2':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game_list(callback.message, 'lvl2')

    elif callback.data == 'new_game_list3':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game_list(callback.message, 'lvl3')

    elif callback.data == 'continue_game':
        if d.DAO.bd_task(d.DAO.get_user, callback.message.chat.id):
            bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
            ng.get_balance(callback.message, False)
        else:
            bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
            bot.send_message(callback.message.chat.id, c.TEXT_WELCOME5)
            ng.new_game_choise(callback.message)

    elif callback.data == 'test':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        user = p.Person.get_data(1)
        bot.send_message(callback.message.chat.id, user.text_balance(), parse_mode='HTML')
        btn.menu_setter(callback.message, btn.set_main_menu)

    elif callback.data == 'set_balance':
        user = p.Person.get_data(callback.message.chat.id)
        bot.send_message(callback.message.chat.id, user.text_balance(), parse_mode='HTML')
        btn.menu_setter(callback.message, btn.set_main_menu)

    elif callback.data == 'about_bot':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        hg.curr_poll = 3
        hg.curr_poll = hg.about_bot(callback.message, hg.curr_poll)

    elif callback.data == 'next':
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        hg.curr_poll = hg.about_bot(callback.message, hg.curr_poll)

    elif callback.data in [el['name'] for lvl in c.PROFESSIONS.items() for el in lvl[1]]:
        bot.edit_message_reply_markup(callback.message.chat.id, message_id=callback.message.message_id, reply_markup='')
        ng.new_game_setup(callback.message, callback.data)


@bot.message_handler(content_types=['text'])
def check_menu_game(message):
    u.custom_logs()
    m1 = hg.check_menu_game(message) #реакции на кнопки меню
    m2 = hc.check_menu_cash(message) #реакции на кнопки с наличкой
    m3 = hl.check_menu_life(message) #реакции на кнопки с жизненными ситуациями
    m4 = ha.check_menu_actives(message) #реакции на пункты меню с активами
    
    if message.text.lower() == 'я есть грут':
        bot.send_message(message.chat.id, 'я есть грут', message_effect_id=5107584321108051014)
    elif all([m1, m2, m3, m4]):
        bot.send_message(message.chat.id, 'Такой команды не существует! Попробуйте вновь.')
    
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        #print('Произошла ошибка:', e)
        u.logging.info(f'Ошибка polling. ', f'Error: {e}')
        continue
