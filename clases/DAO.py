import sqlite3
import constants as c
import utilites as u

class DAO:
    def __init__(self):
        self.stack = []

    @staticmethod
    def bd_task(func, chat_id = None, value = None, user_id = None):
        try:
            conn = sqlite3.connect(c.DB_PATH)
            cursor = conn.cursor()

            if chat_id == None:
                func(cursor)
            elif user_id == None and value == None:
                return func(cursor, chat_id)
            elif value == None:
                func(cursor, chat_id, user_id)
            elif user_id == None:
                func(cursor, chat_id, value)

            conn.commit()
            u.logging.info(f'Обмен успешен. Чат: {chat_id}')
        except sqlite3.DatabaseError as e:
            u.logging.error(f'Ошибка обмена с базой. Чат: {chat_id}', f'Error: {e}')
        finally:
            cursor.close()
            conn.close()
    
    def create_table(cursor):
        cursor.execute(f'CREATE TABLE IF NOT EXISTS users ({c.BD_COLUMNS})')
        cursor.execute('SELECT * FROM users WHERE chat_id = 1')
        res = cursor.fetchone()

        if not res:
            cursor.execute(f'INSERT INTO users ({c.BD_COLUMNS}) VALUES ({c.BD_MOK_VALUES})', 
                        (*c.BD_TEST_USER,))
    
    def create_user(cursor, chat_id, user_id):
        cursor.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
        res = cursor.fetchone()

        if not res:
            cursor.execute(f'INSERT INTO users ({c.BD_COLUMNS}) VALUES ({c.BD_MOK_VALUES})',
                        (chat_id, user_id, *c.BD_BLANC_PARAMS))
        else:
            cols = ', '.join([col + ' = ?' for col in c.BD_COLUMNS.split(', ')])
            cursor.execute(f'UPDATE users SET {cols} WHERE chat_id = ?',
                        (chat_id, user_id, *c.BD_BLANC_PARAMS, chat_id))

    def get_user(cursor, chat_id):
        cursor.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
        return cursor.fetchone()
        
    def set_profession(cursor, chat_id, value):
        cursor.execute('UPDATE users SET profession = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_gender(cursor, chat_id, value):
        cursor.execute('UPDATE users SET gender = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_cash(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cash = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_salary(cursor, chat_id, value):
        cursor.execute('UPDATE users SET salary = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_salary_extra_name(cursor, chat_id, value):
        cursor.execute('UPDATE users SET salary_extra_name = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_salary_extra(cursor, chat_id, value):
        cursor.execute('UPDATE users SET salary_extra = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_cost_house(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cost_house = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_cost_food(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cost_food = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_cost_transport(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cost_transport = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_cost_cloth(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cost_cloth = ? WHERE chat_id = ?', (value, chat_id))

    def set_cost_extra_name(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cost_extra_name = ? WHERE chat_id = ?', (value, chat_id))
            
    def set_cost_extra(cursor, chat_id, value):
        cursor.execute('UPDATE users SET cost_extra = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_menu_id(cursor, chat_id, value):
        cursor.execute('UPDATE users SET menu_id = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_marriage(cursor, chat_id, value):
        cursor.execute('UPDATE users SET marriage = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_childs(cursor, chat_id, value):
        cursor.execute('UPDATE users SET childs = ? WHERE chat_id = ?', (value, chat_id))

    def set_turn(cursor, chat_id, value):
        cursor.execute('UPDATE users SET turn = ? WHERE chat_id = ?', (value, chat_id))
            
    def set_world(cursor, chat_id, value):
        cursor.execute('UPDATE users SET world = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_wishes(cursor, chat_id, value):
        cursor.execute('UPDATE users SET wishes = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_id_last_active(cursor, chat_id, value):
        cursor.execute('UPDATE users SET id_last_active = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_small_business(cursor, chat_id, value):
        cursor.execute('UPDATE users SET small_business = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_medium_business(cursor, chat_id, value):
        cursor.execute('UPDATE users SET medium_business = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_big_business(cursor, chat_id, value):
        cursor.execute('UPDATE users SET big_business = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_stocks(cursor, chat_id, value):
        cursor.execute('UPDATE users SET stocks = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_bonds(cursor, chat_id, value):
        cursor.execute('UPDATE users SET bonds = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_deposits(cursor, chat_id, value):
        cursor.execute('UPDATE users SET deposits = ? WHERE chat_id = ?', (value, chat_id))

    def set_autos(cursor, chat_id, value):
        cursor.execute('UPDATE users SET autos = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_flats(cursor, chat_id, value):
        cursor.execute('UPDATE users SET flats = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_lands(cursor, chat_id, value):
        cursor.execute('UPDATE users SET lands = ? WHERE chat_id = ?', (value, chat_id))

    def set_mansions(cursor, chat_id, value):
        cursor.execute('UPDATE users SET mansions = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_chalets(cursor, chat_id, value):
        cursor.execute('UPDATE users SET chalets = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_yachts(cursor, chat_id, value):
        cursor.execute('UPDATE users SET yachts = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_flies(cursor, chat_id, value):
        cursor.execute('UPDATE users SET flies = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_total_income(cursor, chat_id, value):
        cursor.execute('UPDATE users SET total_income = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_total_outcome(cursor, chat_id, value):
        cursor.execute('UPDATE users SET total_outcome = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_flow(cursor, chat_id, value):
        cursor.execute('UPDATE users SET flow = ? WHERE chat_id = ?', (value, chat_id))
    
    def set_debt(cursor, chat_id, value):
        cursor.execute('UPDATE users SET debt = ? WHERE chat_id = ?', (value, chat_id))
