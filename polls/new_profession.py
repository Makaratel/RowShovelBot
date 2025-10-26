import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_profession(message):
    bot.send_message(message.chat.id, c.BALANCE_Q1, reply_markup=c.MARKUP_NULL)
    bot.register_next_step_handler(message, get_profession)

def get_profession(message):
    input_res = u.get_input(message, 'str', c.ERROR3, get_profession)
    d.DAO.bd_task(d.DAO.set_profession, message.chat.id, input_res)
    bot.register_next_step_handler(message, get_salary)
    bot.send_message(message.chat.id, c.BALANCE_Q4)

def get_salary(message):
    user = p.Person.get_data(message.chat.id)
    input_res = u.get_input(message, 'int', c.ERROR1, get_salary)
    d.DAO.bd_task(d.DAO.set_salary, message.chat.id, input_res)
    d.DAO.bd_task(d.DAO.set_total_income, message.chat.id, user.total_income + input_res)
    d.DAO.bd_task(d.DAO.set_flow, message.chat.id, user.flow + input_res)
    bot.send_message(message.chat.id, 'Вы устроились на работу!')
    btn.menu_setter(message, btn.set_main_menu)