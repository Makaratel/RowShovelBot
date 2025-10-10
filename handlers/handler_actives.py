import prettytable as pt
import constants as c
import menu as btn
import utilites as u

import clases.Person as p
import clases.DAO as d

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

bot = None

#реакции на пункты меню с активами
def check_menu_actives(message):
    if 'операции с активами' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_actives)

    elif 'купить актив' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_buy)

    elif 'продать актив' in message.text.lower():
        actives = print_actives(message)
        if actives:
            bot.register_next_step_handler(message, sell_active)
            bot.send_message(message.chat.id, c.BUY_4, reply_markup=c.MARKUP_NULL)

    elif 'изменить актив' in message.text.lower():
        actives = print_actives(message)
        if actives:
            bot.register_next_step_handler(message, ca.change_active)
            bot.send_message(message.chat.id, c.BUY_4, reply_markup=c.MARKUP_NULL)

    elif 'мои активы' in message.text.lower():
        print_actives(message)
        btn.menu_setter(message, btn.set_main_menu)

    #Меню покупки актива
    elif 'бизнес' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_business)

    elif 'малый бизнес' in message.text.lower():
        nb.new_business(message, 'малый бизнес')

    elif 'средний бизнес' in message.text.lower():
        nb.new_business(message, 'средний бизнес')

    elif 'крупный бизнес' in message.text.lower():
        nb.new_business(message, 'крупный бизнес')

    elif 'биржа' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_trade)

    elif 'акции' in message.text.lower():
        ns.new_stocks(message)

    elif 'облигации' in message.text.lower():
        nbnds.new_bonds(message)

    elif 'вклад' in message.text.lower():
        nd.new_deposit(message)

    elif 'крупные покупки' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_big_buy)

    elif 'купить авто' in message.text.lower():
        na.new_auto(message)

    elif 'купить квартиру' in message.text.lower():
        nfl.new_flats(message)

    elif 'купить землю' in message.text.lower():
        nl.new_lands(message)

    elif 'купить загородный дом' in message.text.lower():
        nc.new_chalets(message)

    elif 'купить особняк' in message.text.lower():
        nm.new_mansion(message)

    elif 'купить яхту' in message.text.lower():
        ny.new_yacht(message)

    elif 'купить самолет' in message.text.lower():
        nf.new_flight(message)

    elif 'банкротство' in message.text.lower():
        bankruptcy(message)

    else:
        return 1

def print_actives(message):
    res = ''
    user = p.Person.get_data(message.chat.id)
    actives = u.get_has_actives(user)

    for key, value in actives.items():
        title = f'{key}: \n'

        table = pt.PrettyTable(value[0].keys())
        table.padding_width = 0

        for el in value:
            table.add_row([*el.values()])
        res += f'{title}<pre>{table}</pre>'

    if res != '': bot.send_message(message.chat.id, res, parse_mode='HTML')
    if res == '': bot.send_message(message.chat.id, 'У вас еще нет активов!')
    return res

def sell_active(message):
    input_res = u.get_input(message, 'int', c.BUY_5, sell_active)
    user = p.Person.get_data(message.chat.id)
    group_actives = u.find_group_actives(user, input_res)

    if group_actives and group_actives['values']:
        my_active = group_actives['values'][group_actives['index']]
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + int(my_active.get('стоимость', 0)))
        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income - my_active.get('прибыль', 0))
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - my_active.get('прибыль', 0))
        group_actives['values'].pop(group_actives['index'])
        new_group_actives = str(group_actives['values'])
        d.DAO.bd_task(group_actives['setter_str'], message.chat.id, new_group_actives)
        bot.send_message(message.chat.id, c.BUY_3)
        btn.menu_setter(message, btn.set_main_menu)

def bankruptcy(message):
    user = p.Person.get_data(message.chat.id)
    
    if len(user.small_business) == 0 and len(user.medium_business) == 0 and len(user.big_business) == 0:
        bot.send_message(message.chat.id, c.BUSINESS_5)
    elif len(user.small_business) > 0:
        business = user.small_business.pop()
        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income - business['прибыль'])
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - business['прибыль'])
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + business['стоимость'])
        d.DAO.bd_task(d.DAO.set_small_business, message.chat.id, str(user.small_business))
        bot.send_message(message.chat.id, c.BUSINESS_6)
    elif len(user.medium_business) > 0:
        business = user.medium_business.pop()
        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income - business['прибыль'])
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - business['прибыль'])
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + business['стоимость'])
        d.DAO.bd_task(d.DAO.set_medium_business, message.chat.id, str(user.medium_business))
        bot.send_message(message.chat.id, c.BUSINESS_6)
    elif len(user.big_business) > 0:
        business = user.big_business.pop()
        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income - business['прибыль'])
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow - business['прибыль'])
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + business['стоимость'])
        d.DAO.bd_task(d.DAO.set_big_business, message.chat.id, str(user.big_business))
        bot.send_message(message.chat.id, c.BUSINESS_6)
