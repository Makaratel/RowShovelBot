import constants as c
import utilites as u
import clases.DAO as d
import clases.Person as p
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = None

def set_property(message, type, bd_callback, next_step = '', text = '', is_end = False, curr_func = ''):
    input_res = u.get_input(message, type, text, curr_func)
    d.DAO.bd_task(bd_callback, message.chat.id, input_res)

    if is_end == False: 
        bot.register_next_step_handler(message, next_step)
        bot.send_message(message.chat.id, text)

def new_game_choise(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Выбрать базовую ведомость', callback_data='new_game_base'))
    markup.add(InlineKeyboardButton('Создать новую ведомость', callback_data='new_game_blanc'))
    bot.send_message(message.chat.id, c.TEXT_WELCOME6, reply_markup=markup)

def new_game(message, isBase = False):
    d.DAO.bd_task(d.DAO.create_user, message.chat.id, user_id = message.from_user.id)
    d.DAO.bd_task(d.DAO.set_world, message.chat.id, c.WORLD1.lower())
    d.DAO.bd_task(d.DAO.set_marriage, message.chat.id, False)
    d.DAO.bd_task(d.DAO.set_childs, message.chat.id, 0)
    d.DAO.bd_task(d.DAO.set_wishes, message.chat.id, 0)
    d.DAO.bd_task(d.DAO.set_turn, message.chat.id, 0)
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, 0)
    d.DAO.bd_task(d.DAO.set_debt, message.chat.id, 0)
    d.DAO.bd_task(d.DAO.set_small_business, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_medium_business, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_big_business, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_stocks, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_bonds, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_deposits, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_autos, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_flats, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_lands, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_chalets, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_yachts, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_flies, message.chat.id, '[]')
    d.DAO.bd_task(d.DAO.set_mansions, message.chat.id, '[]')
    
    if isBase == False: 
        bot.register_next_step_handler(message, set_profession)
        bot.send_message(message.chat.id, c.BALANCE_Q1, reply_markup=c.MARKUP_NULL)
    if isBase == True: 
        bot.register_next_step_handler(message, set_gender, isBase)
        bot.send_message(message.chat.id, c.BALANCE_Q2, reply_markup=c.MARKUP_NULL)
    
def set_profession(message):
    set_property(message, 'str', d.DAO.set_profession, set_gender, c.BALANCE_Q2, False, set_profession)

def set_gender(message, isBase = False):
    input_res = message.text.strip().lower()
    
    if input_res in ['мужской', 'женский']:
        d.DAO.bd_task(d.DAO.set_gender, message.chat.id, input_res)

        if isBase == False:
            bot.register_next_step_handler(message, set_cash)
            bot.send_message(message.chat.id, c.BALANCE_Q3)
        if isBase == True:
            new_game_base(message)
    else:
        u.get_error(message, c.ERROR2, set_gender)

def set_cash(message):
    set_property(message, 'int', d.DAO.set_cash, set_salary, c.BALANCE_Q4, False, set_cash)
    
def set_salary(message):
    set_property(message, 'int', d.DAO.set_salary, set_salary_extra_name, c.BALANCE_Q5, False, set_salary)

def set_salary_extra_name(message):
    set_property(message, 'str', d.DAO.set_salary_extra_name, set_salary_extra, c.BALANCE_Q6, False, set_salary_extra_name)

def set_salary_extra(message):
    set_property(message, 'int', d.DAO.set_salary_extra, set_cost_house, c.BALANCE_Q7, False, set_salary_extra)

def set_cost_house(message):
    set_property(message, 'int', d.DAO.set_cost_house, set_cost_food, c.BALANCE_Q8, False, set_cost_house)

def set_cost_food(message):
    set_property(message, 'int', d.DAO.set_cost_food, set_cost_transport, c.BALANCE_Q9, False, set_cost_food) 
    
def set_cost_transport(message):
    set_property(message, 'int', d.DAO.set_cost_transport, set_cost_cloth, c.BALANCE_Q10, False, set_cost_transport) 
    
def set_cost_cloth(message):
    set_property(message, 'int', d.DAO.set_cost_cloth, set_cost_extra_name, c.BALANCE_Q11, False, set_cost_cloth) 

def set_cost_extra_name(message):
    set_property(message, 'str', d.DAO.set_cost_extra_name, set_cost_extra, c.BALANCE_Q12, False, set_cost_extra_name) 

def set_cost_extra(message):
    set_property(message, 'int', d.DAO.set_cost_extra, is_end = True, curr_func=set_cost_extra)
    get_balance(message)

def get_balance(message, is_new = True):
    if is_new:
        user = p.Person.get_data(message.chat.id) 
        total_income = user.salary + user.salary_extra
        total_outcome = user.cost_cloth + user.cost_extra + user.cost_food + user.cost_house + user.cost_transport

        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, total_income)
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, total_outcome)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, total_income - total_outcome)

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Вывести балансовую ведомость', callback_data='set_balance'))
    bot.send_message(message.chat.id, c.TEXT_WELCOME4, reply_markup=markup)

def new_game_base(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Профессии 1-го уровня', callback_data='new_game_list1'))
    markup.add(InlineKeyboardButton('Профессии 2-го уровня', callback_data='new_game_list2'))
    markup.add(InlineKeyboardButton('Профессии 3-го уровня', callback_data='new_game_list3'))
    bot.send_message(message.chat.id, c.TEXT_WELCOME7, reply_markup=markup)

def new_game_list(message, level):
    markup = InlineKeyboardMarkup()

    for el in sorted(c.PROFESSIONS[level], key=lambda x: x['name']):
        markup.add(InlineKeyboardButton(el['name'], callback_data=el['name']))
    bot.send_message(message.chat.id, c.TEXT_WELCOME8, reply_markup=markup)

def new_game_setup(message, profession_name):
    profession = [el for lvl in c.PROFESSIONS.items() for el in lvl[1] if el['name'] == profession_name][0]
    d.DAO.bd_task(d.DAO.set_profession, message.chat.id, profession['name'])
    d.DAO.bd_task(d.DAO.set_cash, message.chat.id, profession['cash'])
    d.DAO.bd_task(d.DAO.set_salary, message.chat.id, profession['salary'])
    d.DAO.bd_task(d.DAO.set_salary_extra_name, message.chat.id, profession['salary_extra_name'])
    d.DAO.bd_task(d.DAO.set_salary_extra, message.chat.id, profession['salary_extra'])
    d.DAO.bd_task(d.DAO.set_cost_house, message.chat.id, profession['cost_house'])
    d.DAO.bd_task(d.DAO.set_cost_food, message.chat.id, profession['cost_food'])
    d.DAO.bd_task(d.DAO.set_cost_transport, message.chat.id, profession['cost_transport'])
    d.DAO.bd_task(d.DAO.set_cost_cloth, message.chat.id, profession['cost_cloth'])
    d.DAO.bd_task(d.DAO.set_cost_extra_name, message.chat.id, profession['cost_extra_name'])
    d.DAO.bd_task(d.DAO.set_cost_extra, message.chat.id, profession['cost_extra'])
    get_balance(message)