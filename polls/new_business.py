import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_business(message, size):
    business = {}
    user = p.Person.get_data(message.chat.id)
    business['id'] = user.id_last_active + 1
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, user.id_last_active + 1)
    
    match(size):
        case 'малый бизнес': 
            cnt = len(user.medium_business) + len(user.big_business)        
        case 'средний бизнес': 
            cnt = len(user.small_business) + len(user.big_business)
        case 'крупный бизнес': 
            cnt = len(user.small_business) + len(user.medium_business)

    if cnt == 0:
        bot.register_next_step_handler(message, get_business_name, user, size, business)
        bot.send_message(message.chat.id, c.BUSINESS_2, reply_markup=c.MARKUP_NULL)
    else:
        bot.send_message(message.chat.id, c.BUSINESS_1)
        btn.menu_setter(message, btn.set_main_menu)

def get_business_name(message, user, size, business):
    input_res = u.get_input(message, 'str', c.BUSINESS_3, get_business_name)
    business['название'] = input_res
    bot.register_next_step_handler(message, get_business_cost, user, size, business)
    bot.send_message(message.chat.id, c.BUSINESS_3)

def get_business_cost(message, user, size, business):
    input_res = u.get_input(message, 'int', c.BUSINESS_4, get_business_cost)
    business['стоимость'] = input_res
    
    if input_res <= user.cash:
        bot.register_next_step_handler(message, get_business_profit, user, size, business)
        bot.send_message(message.chat.id, c.BUSINESS_4)
    else:
        bot.send_message(message.chat.id, c.BUY_1)
        btn.menu_setter(message, btn.set_main_menu)

def get_business_profit(message, user, size, business):
    input_res = u.get_input(message, 'int', c.ERROR1, get_business_profit)
    business['прибыль'] = input_res
    get_business(message, user, size, business)

def get_business(message, user, size, business):
    match(size):
        case 'малый бизнес': 
            user.small_business.append(business)
            d.DAO.bd_task(d.DAO.set_small_business, message.chat.id, str(user.small_business))
        case 'средний бизнес':
            user.medium_business.append(business)
            d.DAO.bd_task(d.DAO.set_medium_business, message.chat.id, str(user.medium_business))
        case 'крупный бизнес':
            user.big_business.append(business)
            d.DAO.bd_task(d.DAO.set_big_business, message.chat.id, str(user.big_business))

    d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - business['стоимость'])
    d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income + business['прибыль'])
    d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + business['прибыль'])
    bot.send_message(message.chat.id, c.BUY_2)
    btn.menu_setter(message, btn.set_main_menu)
