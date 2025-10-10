import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def change_active(message):
    change = {}
    user = p.Person.get_data(message.chat.id)
    get_id(message, user, change)

def get_id(message, user, change):
    input_res = u.get_input(message, 'int', c.BUY_5, get_id)
    group_actives = u.find_group_actives(user, input_res)

    if group_actives is not None:
        change['id'] = input_res
        bot.send_message(message.chat.id, 'Введите параметр для изменения')
        bot.register_next_step_handler(message, get_property, group_actives, change)
    else:
        bot.send_message(message.chat.id, c.BUY_5)
        btn.menu_setter(message, btn.set_main_menu)

def get_property(message, group_actives, change):
    input_res = u.get_input(message, 'str', c.ERROR1, get_id)

    if input_res in group_actives['values'][group_actives['index']].keys() and input_res != 'id':
        change['property'] = input_res
        bot.send_message(message.chat.id, 'Введите значение параметра для изменения')
        bot.register_next_step_handler(message, get_value, group_actives, change)
    else:
        bot.send_message(message.chat.id, 'Введенный параметр невозможно изменить')
        btn.menu_setter(message, btn.set_main_menu)

def get_value(message, group_actives, change):
    input_res = u.get_input(message, 'else', c.ERROR1, get_value)
    is_int = isinstance(input_res, int)

    if is_int:
        change['value'] = int(input_res)
    else:
        change['value'] = str(input_res)

    set_value(message, group_actives, change)

def set_value(message, group_actives, change):
    actives = group_actives['values']
    actives[group_actives['index']][change['property']] = change['value']
    new_group_actives = str(actives)
    d.DAO.bd_task(group_actives['setter_str'], message.chat.id, new_group_actives)
    bot.send_message(message.chat.id, c.BUY_6)
    btn.menu_setter(message, btn.set_main_menu)