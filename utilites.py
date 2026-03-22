from dotenv import load_dotenv
import os
from os.path import join, dirname
import logging
from datetime import date
import config.constants as c
import clases.DAO as d

bot = None

def get_from_env(key):
    path = join(dirname(__file__) + '/env', 'token.env')
    load_dotenv(path)
    return os.environ.get(key)

def get_error(message, error_text, callback):
    bot.send_message(message.chat.id, error_text)
    bot.register_next_step_handler(message, callback)

def get_actives(user):
    actives = {
        '🌭 Малые бизнесы': [user.small_business, d.DAO.set_small_business],
        '🏪 Средние бизнесы': [user.medium_business, d.DAO.set_medium_business],
        '🏗️ Крупные бизнесы': [user.big_business, d.DAO.set_big_business],
        '💹 Акции': [user.stocks, d.DAO.set_stocks],
        '🧾 Облигации': [user.bonds, d.DAO.set_bonds],
        '🪙 Депозиты': [user.deposits, d.DAO.set_deposits],
        '🚗 Автомобили': [user.autos, d.DAO.set_autos],
        '🌆 Квартиры': [user.flats, d.DAO.set_flats],
        '🏘️ Загородные участки': [user.lands, d.DAO.set_lands],
        '🏠 Загородные дома': [user.chalets, d.DAO.set_chalets],
        '⛵ Яхты': [user.yachts, d.DAO.set_yachts],
        '🛩️ Самолеты': [user.flies, d.DAO.set_flies],
        '🏰 Особняки': [user.mansions, d.DAO.set_mansions]
    }
    
    return actives

def get_has_actives(user):
    actives = get_actives(user)
    return {key: value[0] for key, value in actives.items() if value[0]}
        
def find_group_actives(user, id_active):
    res = None
    actives = get_actives(user)

    for key, value in actives.items():
            for i, el in enumerate(value[0]):
                if el['id'] == id_active:
                     res = {'key': key, 'index': i, 'values': value[0], 'setter_str': value[1]}
    return res

def custom_logs():
     # настраиваем вывод логов
    if not os.path.exists('logs'):
        os.mkdir('logs')

    today = date.today()
    file_path = f"logs/{today.strftime('%Y-%m-%d')}.log"
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', filename=file_path, filemode='a', force=True)

def get_input(message, type, text, curr_func):
    try:
        if type == 'int': input_res = abs(int(message.text.strip()))
        if type == 'str': input_res = message.text.strip().lower()
        return input_res
    except ValueError:
        if type == 'int': get_error(message, c.ERROR1, curr_func)
        if type == 'str': get_error(message, c.ERROR3, curr_func)