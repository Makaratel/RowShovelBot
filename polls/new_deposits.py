import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_deposit(message):
    deposit = {}
    user = p.Person.get_data(message.chat.id)
    deposit['id'] = user.id_last_active + 1
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, user.id_last_active + 1)
    bot.send_message(message.chat.id, c.PAPERS_6, reply_markup=c.MARKUP_NULL)
    bot.register_next_step_handler(message, get_deposit_value, user, deposit)

def get_deposit_value(message, user, deposit):
    input_res = u.get_input(message, 'int', c.ERROR1, get_deposit_value)
    deposit['сумма'] = input_res

    if deposit['сумма'] % 300 == 0 and deposit['сумма'] > 0:
        bot.register_next_step_handler(message, get_deposit_rate, user, deposit)
        bot.send_message(message.chat.id, c.PAPERS_7)
    else:
        bot.send_message(message.chat.id, c.PAPERS_8)
        btn.menu_setter(message, btn.set_main_menu)

def get_deposit_rate(message, user, deposit):
    input_res = u.get_input(message, 'int', c.ERROR1, get_deposit_rate)
    deposit['ставка'] = input_res
    get_deposit(message, user, deposit)

def get_deposit(message, user, deposit):
    if deposit['сумма'] <= user.cash:
        user.deposits.append(deposit)
        d.DAO.bd_task(d.DAO.set_deposits, message.chat.id, str(user.deposits))
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - deposit['сумма'])
        d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income + (deposit['сумма'] * deposit['ставка'] / c.DEPOSIT_KEY_VALUE))
        d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + (deposit['сумма'] * deposit['ставка'] / c.DEPOSIT_KEY_VALUE))
        bot.send_message(message.chat.id, c.BUY_2)
    else:
        bot.send_message(message.chat.id, c.BUY_1)
        
    btn.menu_setter(message, btn.set_main_menu)