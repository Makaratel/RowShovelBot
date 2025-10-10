import constants as c
import clases.DAO as d


class Person:
    def __init__(self, chat_id = 0, user_id = 0):
        self.chat_id = chat_id
        self.user_id = user_id

        self.profession = ''
        self.gender = ''
        self.world = 'Мир бедных'
        self.marriage = False
        self.childs = 0
        self.wishes = 0
        self.turn = 0

        self.salary = 0
        self.salary_extra_name = ''
        self.salary_extra = 0

        self.cost_house = 0
        self.cost_food = 0
        self.cost_transport = 0
        self.cost_cloth = 0
        self.cost_extra_name = ''
        self.cost_extra = 0

        self.total_income = 0
        self.total_outcome = 0
        self.flow = 0
        self.cash = 0

        self.small_business = []
        self.medium_business = []
        self.big_business = []
        self.stocks = []
        self.bonds = []
        self.deposits = []
        self.autos = []
        self.flats = []
        self.lands = []
        self.chalets = []
        self.yachts = []
        self.flies = []
        self.mansions = []

        self.menu_id = 0
        self.id_last_active = 0
        self.debt = 0
    
    def text_balance(self):
        res = f'{c.BALANCE_1} <b><i>{self.profession.capitalize()}</i></b>\n' +\
            f'{c.BALANCE_2} <b><i>{self.gender.capitalize()}</i></b>\n' +\
            f'{c.BALANCE_17} <b><i>{"Да" if self.marriage else "Нет"}</i></b>\n' +\
            f'{c.BALANCE_18} <b><i>{self.childs}</i></b>\n' +\
            f'{c.DELIMETER}\n' +\
            f'{c.BALANCE_14} <b><i>{self.turn}</i></b>\n' +\
            f'{c.BALANCE_15} <b><i>{self.world.capitalize()}</i></b>\n' +\
            f'{c.BALANCE_16} <b><i>{self.wishes}</i></b>\n' +\
            f'{c.DELIMETER}\n' +\
            f'{c.BALANCE_4} <b><i>+{self.salary}</i></b>\n' +\
            f'{c.BALANCE_5} {self.salary_extra_name.capitalize()}: <b><i>+{self.salary_extra}</i></b>\n' +\
            f'{c.BALANCE_6} <b><i>-{self.cost_house}</i></b>\n' +\
            f'{c.BALANCE_7} <b><i>-{self.cost_food}</i></b>\n' +\
            f'{c.BALANCE_8} <b><i>-{self.cost_transport}</i></b>\n' +\
            f'{c.BALANCE_9} <b><i>-{self.cost_cloth}</i></b>\n' +\
            f'{c.BALANCE_10} {self.cost_extra_name.capitalize()}: <b><i>-{self.cost_extra}</i></b>\n' +\
            f'{c.DELIMETER}\n' +\
            f'{c.BALANCE_20} <b><i>{len(self.small_business) + len(self.medium_business) + len(self.big_business)}</i></b>\n' +\
            f'{c.BALANCE_21} <b><i>{len(self.stocks) + len(self.bonds)}</i></b>\n' +\
            f'{c.BALANCE_22} <b><i>{len(self.autos) + len(self.yachts) + len(self.flies)}</i></b>\n' +\
            f'{c.BALANCE_23} <b><i>{len(self.flats) + len(self.mansions) + len(self.chalets) + len(self.lands)}</i></b>\n' +\
            f'{c.BALANCE_24} <b><i>{len(self.deposits)}</i></b>\n' +\
            f'{c.BALANCE_25} <b><i>{self.count_credits()}</i></b>\n' +\
            f'{c.DELIMETER}\n' +\
            f'{c.BALANCE_11} <b><i>+{self.total_income}</i></b>\n' +\
            f'{c.BALANCE_12} <b><i>-{self.total_outcome}</i></b>\n' +\
            f'{c.BALANCE_13} <b><i>{"+" if self.flow >= 0 else ""}{self.flow}</i></b>\n' +\
            f'{c.BALANCE_3} <b><i>{self.cash}</i></b>\n' +\
            f'{c.BALANCE_26} <b><i>-{self.debt}</i></b>'
        return res
    
    def set_params(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36):
        self.profession = p1
        self.gender = p2
        self.world = p3
        self.marriage = p4
        self.childs = int(p5)
        self.wishes = int(p6)
        self.turn = int(p7)

        self.salary = int(p8)
        self.salary_extra_name = p9
        self.salary_extra = int(p10)

        self.cost_house = int(p11)
        self.cost_food = int(p12)
        self.cost_transport = int(p13)
        self.cost_cloth = int(p14)
        self.cost_extra_name = p15
        self.cost_extra = int(p16)

        self.total_income = int(p17)
        self.total_outcome = int(p18)
        self.flow = int(p19)
        self.cash = int(p20)

        self.small_business = eval(p21)
        self.medium_business = eval(p22)
        self.big_business = eval(p23)
        self.stocks = eval(p24)
        self.bonds = eval(p25)
        self.deposits = eval(p26)
        self.autos = eval(p27)
        self.flats = eval(p28)
        self.lands = eval(p29)
        self.chalets = eval(p30)
        self.yachts = eval(p31)
        self.flies = eval(p32)
        self.mansions = eval(p33)

        self.menu_id = p34
        self.id_last_active = p35
        self.debt = p36

    @staticmethod
    def get_data(chat_id):
        data = d.DAO.bd_task(d.DAO.get_user, chat_id)
        user = Person(chat_id)
        user.set_params(*data[2:])
        return user
    
    def count_credits(self):
        res = 0
        actives = [self.autos, self.flats]

        for group in actives:
            for active in group:
                if active['платеж'] > 0:
                    res += 1
        return res
