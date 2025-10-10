import constants as c
import utilites as u
import polls.new_game as ng
import menu as btn
import clases.Person as p
import clases.DAO as d
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = None
curr_poll = None

def check_menu_game(message):
    #Возврат между меню
    if 'назад' in message.text.lower():
        user = p.Person.get_data(message.chat.id)
        menu_id = btn.check_menu(message, user.menu_id)
        d.DAO.bd_task(d.DAO.set_menu_id, message.chat.id, menu_id)
        #btn.menu_setter(message, btn.check_menu, user.menu_id)

    #Меню игры
    elif 'меню игры' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_game)

    elif 'новая игра' in message.text.lower():
        ng.new_game(message)
        d.DAO.bd_task(d.DAO.set_menu_id, message.chat.id, 0)

    elif 'сообщество' in message.text.lower():
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти в сообщество', url=c.LINK_VK))
        bot.send_message(message.chat.id, 'Переходите и подписывайтесь на нашу группу VK', reply_markup=markup)
        btn.menu_setter(message, btn.set_main_menu)

    elif 'как пользоваться ботом' in message.text.lower():
        global curr_poll
        curr_poll = 3
        curr_poll = about_bot(message, curr_poll)

    elif 'завершить месяц' in message.text.lower():
        end_turn(message)

    elif 'балансовая ведомость' in message.text.lower():
        user = p.Person.get_data(message.chat.id)
        bot.send_message(message.chat.id, user.text_balance(), parse_mode='HTML')

    #Меню перехода в новый мир
    elif 'перейти в новый мир' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_world)

    elif 'мир бедных' in message.text.lower():
        set_world(message, c.WORLD1.lower())
        btn.menu_setter(message, btn.set_main_menu)
        
    elif 'мир среднего класса' in message.text.lower():
        set_world(message, c.WORLD2.lower())
        btn.menu_setter(message, btn.set_main_menu)

    elif 'мир богатых' in message.text.lower():
        set_world(message, c.WORLD3.lower())
        btn.menu_setter(message, btn.set_main_menu)
    
    elif 'главное меню' in message.text.lower():
        btn.menu_setter(message, btn.set_main_menu)

    else:
        return 1

def set_world(message, world):
    #В момент перехода в новый мир меняются только расходы на детей, если они есть. 
    #Все остальные вещи (долги, свадьба) считаюстя в моменте события, они во времени не происходят.
    user = p.Person.get_data(message.chat.id)
    world_ob = world.replace('мир', 'Мире')

    if user.world == world:
        bot.send_message(message.chat.id, f'Вы уже находитесь в {world_ob}')
    else:
        d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome - user.childs * c.WORLDS_KOEFS[user.world] + user.childs * c.WORLDS_KOEFS[world])
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + user.childs * c.WORLDS_KOEFS[user.world] - user.childs * c.WORLDS_KOEFS[world])
        d.DAO.bd_task(d.DAO.set_world, message.chat.id, world)
        bot.send_message(message.chat.id, f'Вы перешли в {world.capitalize()}')

def end_turn(message):
    user = p.Person.get_data(message.chat.id)
    d.DAO.bd_task(d.DAO.set_turn, message.chat.id, user.turn + 1)

    if user.cash + user.flow < 0:
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, 0)
        d.DAO.bd_task(d.DAO.set_debt, message.chat.id, user.debt + (user.cash + user.flow) * -1)
    else:
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + user.flow)
    
    counter_terms(message, user)
    check_world_conditions(message, user)
    bot.send_message(message.chat.id, f'Ход {user.turn + 1} закончен')

    if user.debt > 0:
        bot.send_message(message.chat.id, f'Не забудьте, что у Вас долг {user.debt}!')

def counter_terms(message, user):
    actives = u.get_actives(user)
    actives = {key: value for key, value in actives.items() if key[2:] in ['Облигации', 'Автомобили', 'Квартиры']}

    for key, value in actives.items():
        to_delete = []
        for i, active in enumerate(value[0]):
            if active['срок'] > 0:
                active['срок'] -= 1

            if active['срок'] == 0:
                if 'Облигации' in key:
                    user = p.Person.get_data(message.chat.id)
                    d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + active['стоимость'])
                    d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income - (active['купон'] * active['количество']))
                    d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - (active['купон'] * active['количество']))
                    to_delete.append(i)
                else:
                    d.DAO.bd_task(d.DAO.set_total_outcome, message.chat.id, user.total_outcome - active['платеж'])
                    d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + active['платеж'])
                    active['платеж'] = 0

        for el in to_delete:
            value[0].pop(el)
            bot.send_message(message.chat.id, 'Срок действия облигаций истек, они проданы!')
        
        new_group_actives = str(value[0])
        d.DAO.bd_task(value[1], message.chat.id, new_group_actives)

def check_world_conditions(message, user):
    actives = u.get_actives(user)
    actives = {key: value for key, value in actives.items() if key[2:] in ['Автомобили', 'Квартиры']}
    autos = len(list(actives.values())[0][0])
    flats = len(list(actives.values())[1][0])

    if user.cash >= 100000 and user.flow >= 10000 and user.debt == 0:
        check_world = 'мир среднего класса'
    elif user.cash >= 1000000 and user.flow >= 50000 and user.count_credits() == 0 and autos > 0 and flats > 0 and user.debt == 0:
        check_world = 'мир богатых'
    else:
        check_world = 'мир бедных'
    
    if c.WORLDS_KOEFS[user.world] < c.WORLDS_KOEFS[check_world]:
        bot.send_message(message.chat.id, f'Вы выполнили условия перехода в новый мир. Перейдите в {check_world.capitalize()}!')

    if c.WORLDS_KOEFS[user.world] > c.WORLDS_KOEFS[check_world]:
        bot.send_message(message.chat.id, f'Вы более не выполняете условиям текущего мира. Перейдите в {check_world.capitalize()}!')

def about_bot(message, curr_poll):
    if curr_poll == 3:
        file = open(c.IMG_MENU, 'rb')
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Далее', callback_data='next'))
        bot.send_photo(message.chat.id, file, caption = c.ABOUT_2, parse_mode='HTML', reply_markup=markup)
    elif curr_poll == 2:
        file = open(c.IMG_MAP, 'rb')
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Далее', callback_data='next'))
        bot.send_photo(message.chat.id, file, caption = c.ABOUT_3, parse_mode='HTML', reply_markup=markup)
    elif curr_poll == 1:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('Начать игру', callback_data='new_game'))
        markup.add(InlineKeyboardButton('Продолжить игру', callback_data='continue_game'))
        bot.send_message(message.chat.id, c.ABOUT_1, parse_mode='HTML', reply_markup=markup)
    return curr_poll - 1