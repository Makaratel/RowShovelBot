from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import constants as c
import clases.DAO as d

bot = None

def menu_setter(message, func):
    menu_id = func(message)
    d.DAO.bd_task(d.DAO.set_menu_id, message.chat.id, menu_id)

def check_menu(message, menu_id):
    match(menu_id):
        case 1: res = set_main_menu(message)
        case 2: res = set_main_menu(message)
        case 3: res = set_menu_game(message)
        case 4: res = set_menu_actives(message)
        case 5: res = set_menu_buy(message)
        case 6: res = set_menu_buy(message)
        case 7: res = set_main_menu(message)
        case 8: res = set_main_menu(message)
        case 9: res = set_main_menu(message)
        case 10: res = set_menu_buy(message)
    return res

def set_buttons(row_width, buttons, message):
    markup = ReplyKeyboardMarkup(row_width=row_width, input_field_placeholder='Выберите действие', resize_keyboard=True)
    for btn in buttons:
        markup.add(KeyboardButton(btn))
    bot.send_message(message.chat.id, c.ACTION1, reply_markup=markup)
    
def set_main_menu(message):
    markup = ReplyKeyboardMarkup(row_width=2, input_field_placeholder='Выберите действие')
    btn1 = KeyboardButton('🎲 Меню игры ☰')
    btn2 = KeyboardButton('💸 Операции с наличкой ☰')
    btn3 = KeyboardButton('🗂️ Операции с активами ☰')
    btn4 = KeyboardButton('🔮 Жизненные ситуации ☰')
    btn5 = KeyboardButton('⌛ Завершить месяц')
    btn6 = KeyboardButton('💹 Мои активы')
    btn7 = KeyboardButton('📝 Балансовая ведомость')

    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    markup.row(btn6, btn7)
    bot.send_message(message.chat.id, c.ACTION1, reply_markup=markup)
    return 1

def set_menu_game(message):
    btns = ['Новая игра', 'Перейти в новый мир ☰', 'Сообщество', 'Как пользоваться ботом?', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 2

def set_menu_world(message):
    btns = ['Мир бедных', 'Мир среднего класса', 'Мир богатых', '⬅️ Назад']
    set_buttons(3, btns, message)
    return 3

def set_menu_buy(message):
    btns = ['Бизнес ☰', 'Биржа ☰', 'Вклад', 'Крупные покупки ☰', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 4

def set_menu_business(message):
    btns = ['Малый бизнес', 'Средний бизнес', 'Крупный бизнес', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 5

def set_menu_trade(message):
    btns = ['Акции', 'Облигации', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 6

def set_menu_cash(message):
    btns = ['Получить деньги', 'Потратить деньги', 'Вернуть долг', 'Причуды', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 7

def set_menu_situations(message):
    btns = ['Любовь', 'Развод', 'Ребенок', 'Уволиться / Найти работу', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 8

def set_menu_actives(message):
    btns = ['Купить актив ☰', 'Продать актив', 'Изменить актив', 'Банкротство', '⬅️ Назад']
    set_buttons(1, btns, message)
    return 9

def set_menu_big_buy(message):
    markup = ReplyKeyboardMarkup(row_width=2, input_field_placeholder='Выберите действие')
    btn1 = KeyboardButton('Купить авто')
    btn2 = KeyboardButton('Купить квартиру')
    btn3 = KeyboardButton('Купить землю')
    btn4 = KeyboardButton('Купить загородный дом')
    btn5 = KeyboardButton('Купить особняк')
    btn6 = KeyboardButton('Купить яхту')
    btn7 = KeyboardButton('Купить самолет')
    btn8 = KeyboardButton('⬅️ Назад')

    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5, btn6)
    markup.row(btn7, btn8)
    bot.send_message(message.chat.id, c.ACTION1, reply_markup=markup)
    return 10