import constants as c
import menu as btn
import utilites as u
import clases.Person as p
import clases.DAO as d

bot = None

def check_menu_cash(message):
    if 'операции с наличкой' in message.text.lower():
        btn.menu_setter(message, btn.set_menu_cash)

    elif 'получить деньги' in message.text.lower():
        bot.register_next_step_handler(message, get_money)
        bot.send_message(message.chat.id, 'Введите сумму денег', reply_markup=c.MARKUP_NULL)

    elif 'потратить деньги' in message.text.lower():
        bot.register_next_step_handler(message, away_money)
        bot.send_message(message.chat.id, 'Введите сумму денег', reply_markup=c.MARKUP_NULL)

    elif 'вернуть долг' in message.text.lower():
        bot.register_next_step_handler(message, debt_money)
        bot.send_message(message.chat.id, 'Введите сумму денег', reply_markup=c.MARKUP_NULL)

    elif 'причуды' in message.text.lower():
        bot.register_next_step_handler(message, get_wish)
        bot.send_message(message.chat.id, 'Введите стоимость причуды', reply_markup=c.MARKUP_NULL)

    else:
        return 1

def get_money(message):
    input_res = u.get_input(message, 'int', c.ERROR1, get_money)
    user = p.Person.get_data(message.chat.id)
    d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash + input_res)

    bot.send_message(message.chat.id, 'Операция выполнена')
    btn.menu_setter(message, btn.set_main_menu)

def away_money(message):
    input_res = u.get_input(message, 'int', c.ERROR1, away_money)
    user = p.Person.get_data(message.chat.id)
    
    if user.cash < input_res:
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, 0)
        d.DAO.bd_task(d.DAO.set_debt, message.chat.id, user.debt + input_res - user.cash)
    else:
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - input_res)

    bot.send_message(message.chat.id, 'Операция выполнена')
    btn.menu_setter(message, btn.set_main_menu)

def get_wish(message):
    input_res = u.get_input(message, 'int', c.ERROR1, get_wish)
    user = p.Person.get_data(message.chat.id)

    if user.cash >= input_res:
        d.DAO.bd_task(d.DAO.set_wishes, message.chat.id, user.wishes + 1)
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - input_res)
        bot.send_message(message.chat.id, c.BUY_2)
    else:
        bot.send_message(message.chat.id, c.BUY_1)

    btn.menu_setter(message, btn.set_main_menu)

def debt_money(message):
    input_res = u.get_input(message, 'int', c.ERROR1, debt_money)
    user = p.Person.get_data(message.chat.id)

    if user.debt == 0:
        bot.send_message(message.chat.id, 'У Вас нет долгов!')
    elif input_res > user.cash:
        bot.send_message(message.chat.id, 'У Вас недостаточно наличных!')
    else:
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - input_res)
        d.DAO.bd_task(d.DAO.set_debt, message.chat.id, user.debt - input_res)
        bot.send_message(message.chat.id, 'Операция выполнена')
    btn.menu_setter(message, btn.set_main_menu)