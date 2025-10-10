import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_auto(message):
    active = {}
    user = p.Person.get_data(message.chat.id)
    active['id'] = user.id_last_active + 1
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, user.id_last_active + 1)
    bot.send_message(message.chat.id, c.ACTIVE_1, reply_markup=c.MARKUP_NULL)
    bot.register_next_step_handler(message, get_name, user, active)

def get_name(message, user, active):
    input_res = u.get_input(message, 'str', c.ERROR3, get_name)
    active['название'] = input_res
    bot.register_next_step_handler(message, get_cost, user, active)
    bot.send_message(message.chat.id, c.ACTIVE_2)

def get_cost(message, user, active):
    input_res = u.get_input(message, 'int', c.ERROR1, get_cost)
    active['стоимость'] = input_res

    if input_res <= user.cash:
        bot.register_next_step_handler(message, get_credit, user, active)
        bot.send_message(message.chat.id, c.ACTIVE_3)
    else:
        bot.send_message(message.chat.id, c.BUY_1)
        menu_id = btn.set_main_menu(message)
        d.DAO.bd_task(d.DAO.set_menu_id, message.chat.id, menu_id)

def get_credit(message, user, active):
    input_res = u.get_input(message, 'str', c.ERROR3, get_credit)

    if input_res == 'да':
        bot.register_next_step_handler(message, get_time, user, active)
        bot.send_message(message.chat.id, c.ACTIVE_4)
    elif input_res == 'нет':
        active['срок'] = 0
        active['платеж'] = 0
        get_auto(message, user, active)
    else:
        u.get_error(message, c.ERROR1, get_credit)

def get_time(message, user, active):
    input_res = u.get_input(message, 'int', c.ERROR1, get_time)
    active['срок'] = input_res
    bot.register_next_step_handler(message, get_pay, user, active)
    bot.send_message(message.chat.id, c.ACTIVE_5)

def get_pay(message, user, active):
    input_res = u.get_input(message, 'int', c.ERROR1, get_pay)
    active['платеж'] = input_res
    get_auto(message, user, active)

def get_auto(message, user, active):
    user.autos.append(active)
    d.DAO.bd_task(d.DAO.set_autos, message.chat.id, str(user.autos))

    if active['срок'] == 0:
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - active['стоимость'])
        bot.send_message(message.chat.id, c.BUY_2)
    else:
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome + active['платеж'])
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - active['платеж'])
        bot.send_message(message.chat.id, c.BUY_2)

    btn.menu_setter(message, btn.set_main_menu)