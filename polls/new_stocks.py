import constants as c
import utilites as u
import menu as btn
import clases.DAO as d
import clases.Person as p

bot = None

def new_stocks(message):
    papers = {}
    user = p.Person.get_data(message.chat.id)
    papers['id'] = user.id_last_active + 1
    d.DAO.bd_task(d.DAO.set_id_last_active, message.chat.id, user.id_last_active + 1)
    bot.send_message(message.chat.id, c.PAPERS_1, reply_markup=c.MARKUP_NULL)
    bot.register_next_step_handler(message, get_ticker, user, papers)

def get_ticker(message, user, papers):
    input_res = u.get_input(message, 'str', c.ERROR3, get_ticker)
    papers['тикер'] = input_res
    bot.register_next_step_handler(message, get_paper_cost, user, papers)
    bot.send_message(message.chat.id, c.PAPERS_2)

def get_paper_cost(message, user, papers):
    input_res = u.get_input(message, 'int', c.ERROR1, get_paper_cost)
    papers['цена'] = input_res
    bot.register_next_step_handler(message, get_paper_quantity, user, papers)
    bot.send_message(message.chat.id, c.PAPERS_3)

def get_paper_quantity(message, user, papers):
    input_res = u.get_input(message, 'int', c.ERROR1, get_paper_quantity)
    papers['количество'] = input_res
    get_paper(message, user, papers)

def get_paper(message, user, papers):
    papers['стоимость'] = papers['цена'] * papers['количество']

    if papers['стоимость'] <= user.cash:
        user.stocks.append(papers)
        d.DAO.bd_task(d.DAO.set_stocks, message.chat.id, str(user.stocks))
        d.DAO.bd_task(d.DAO.set_cash, message.chat.id, user.cash - papers['стоимость'])
        bot.send_message(message.chat.id, c.BUY_2)
    else:
        bot.send_message(message.chat.id, c.BUY_1)
        
    btn.menu_setter(message, btn.set_main_menu)