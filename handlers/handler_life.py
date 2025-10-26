import menu as btn
import clases.Person as p
import clases.DAO as d
import random
import math
import constants as c
import utilites as u
import polls.new_profession as np

bot = None

#Меню жизненных ситуаций
def check_menu_life(message):
    if 'жизненные ситуации' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_situations)
    elif 'любовь' in message.text.lower():
        to_love(message)
    elif 'развод' in message.text.lower():
        to_devorce(message)
    elif 'ребенок' in message.text.lower():
        to_child(message)
    elif 'уволиться / найти работу' in message.text.lower():
        to_work(message)
    else:
        return 1

def to_love(message):
    user = p.Person.get_data(message.chat.id)

    if user.marriage == True:
        bot.send_message(message.chat.id, 'Вы уже женаты! У нас тут не многоженство как бы.')
    elif user.gender == 'мужской':
        world_koef = c.WORLDS_KOEFS[user.world]
        d.DAO.bd_task(d.DAO.set_marriage, message.chat.id, True)
        bot.send_message(message.chat.id, 'Теперь вы женаты. Поздравляем!')

        if user.cash < c.COST_WEDDING * world_koef:
            d.DAO.bd_task(d.DAO.set_cash, message.chat.id, 0)
            d.DAO.bd_task(d.DAO.set_debt, message.chat.id, user.debt + c.COST_WEDDING * world_koef - user.cash)
        else:
            d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - c.COST_WEDDING * world_koef)
    else:
        world_koef = c.WORLDS_KOEFS[user.world]
        d.DAO.bd_task(d.DAO.set_marriage, message.chat.id, True)
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome - c.COST_CHILD * world_koef * user.childs)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + c.COST_CHILD * world_koef * user.childs)
        bot.send_message(message.chat.id, 'Теперь вы женаты. Поздравляем!')
    
    btn.menu_setter(message, btn.set_main_menu)

def to_child(message):
    user = p.Person.get_data(message.chat.id)
    world_koef = c.WORLDS_KOEFS[user.world.lower()]

    if user.gender == 'мужской' and user.marriage == False:
        bot.send_message(message.chat.id, 'Вы еще не женаты!')
    elif user.gender == 'мужской' and user.marriage == True:
        d.DAO.bd_task(d.DAO.set_childs, message.chat.id, user.childs + 1)
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome + c.COST_CHILD * world_koef)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - c.COST_CHILD * world_koef)
        child = random.choice(['мальчик', 'девочка'])
        bot.send_message(message.chat.id, f'Поздравляем! У вас {child}!')
    elif user.gender == 'женский' and user.marriage == False:
        d.DAO.bd_task(d.DAO.set_childs, message.chat.id, user.childs + 1)
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome + c.COST_CHILD * world_koef)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - c.COST_CHILD * world_koef)
        child = random.choice(['мальчик', 'девочка'])
        bot.send_message(message.chat.id, f'Поздравляем! У вас {child}!')
    elif user.gender == 'женский' and user.marriage == True:
        d.DAO.bd_task(d.DAO.set_childs, message.chat.id, user.childs + 1)
        child = random.choice(['мальчик', 'девочка'])
        bot.send_message(message.chat.id, f'Поздравляем! У вас {child}!')

    btn.menu_setter(message, btn.set_main_menu)

def to_devorce(message):
    user = p.Person.get_data(message.chat.id)

    if user.marriage == False:
        bot.send_message(message.chat.id, 'Вы еще не женаты!')
    elif user.gender == 'мужской':
        world_koef = c.WORLDS_KOEFS[user.world]
        d.DAO.bd_task(d.DAO.set_marriage, message.chat.id, False)
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome - c.COST_CHILD * world_koef * user.childs)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + c.COST_CHILD * world_koef * user.childs)
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, round(math.floor(user.cash / 2), -1))
        d.DAO.bd_task(d.DAO.set_childs, message.chat.id, 0)
        bot.send_message(message.chat.id, 'Теперь вы разведены!')
    else:
        world_koef = c.WORLDS_KOEFS[user.world]
        d.DAO.bd_task(d.DAO.set_marriage, message.chat.id, False)
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome + c.COST_CHILD * world_koef * user.childs)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - c.COST_CHILD * world_koef * user.childs)
        bot.send_message(message.chat.id, 'Теперь вы разведены!')

    btn.menu_setter(message, btn.set_main_menu)

def to_work(message):
    user = p.Person.get_data(message.chat.id)

    if user.profession == '-':
        np.new_profession(message)
    else:
        d.DAO.bd_task(d.DAO.set_profession, message.chat.id, '-')
        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income - user.salary)
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - user.salary)
        d.DAO.bd_task(d.DAO.set_salary, message.chat.id, 0)
        bot.send_message(message.chat.id, f'Вы уволены!')
