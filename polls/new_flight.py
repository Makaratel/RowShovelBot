import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_flight(message):
    active = {}
    user = p.Person.get_data(message.chat.id)
    active['id'] = user.id_last_active + 1
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, user.id_last_active + 1)
    bot.send_message(message.chat.id, c.ACTIVE_1, reply_markup=c.MARKUP_NULL)
    bot.register_next_step_handler(message, get_name, user, active)

def get_name(message, user, active):
    input_res = u.get_input(message, 'str', c.ERROR3, get_name)
    input_res = message.text.strip().lower()
    active['название'] = input_res
    bot.register_next_step_handler(message, get_cost, user, active)
    bot.send_message(message.chat.id, c.ACTIVE_2)

def get_cost(message, user, active):
    input_res = u.get_input(message, 'int', c.ERROR1, get_cost)
    active['стоимость'] = input_res
    get_flight(message, user, active)

def get_flight(message, user, active):
    user.flies.append(active)
    d.DAO.bd_task(d.DAO.set_flies, message.chat.id, str(user.flies))
    d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - active['стоимость'])
    bot.send_message(message.chat.id, c.BUY_2)
    btn.menu_setter(message, btn.set_main_menu)