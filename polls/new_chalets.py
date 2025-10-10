import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_chalets(message):
    active = {}
    user = p.Person.get_data(message.chat.id)
    active['id'] = user.id_last_active + 1
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, user.id_last_active + 1)
    bot.send_message(message.chat.id, c.ACTIVE_1, reply_markup=c.MARKUP_NULL)
    bot.register_next_step_handler(message, get_name, user, active)

def get_name(message, user, active):
    input_res = u.get_input(message, 'str', c.ACTIVE_2, get_name)
    active['название'] = input_res
    bot.register_next_step_handler(message, get_cost, user, active)
    bot.send_message(message.chat.id, c.ACTIVE_2)

def get_cost(message, user, active):
    input_res = u.get_input(message, 'int', c.ERROR1, get_cost)
    active['стоимость'] = input_res
    get_chalets(message, user, active)

def get_chalets(message, user, active):
    user.chalets.append(active)
    d.DAO.bd_task(d.DAO.set_chalets, message.chat.id, str(user.chalets))
    d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - active['стоимость'])
    bot.send_message(message.chat.id, c.BUY_2)
    btn.menu_setter(message, btn.set_main_menu)