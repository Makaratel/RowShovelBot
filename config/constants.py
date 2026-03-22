import config.settings as s
from telebot.types import ReplyKeyboardRemove

MARKUP_NULL = ReplyKeyboardRemove(True)

#query
BD_COLUMNS = '''chat_id, user_id, profession, gender, world, marriage, childs, wishes, turn, salary, salary_extra_name, salary_extra, 
                    cost_house, cost_food, cost_transport, cost_cloth, cost_extra_name, cost_extra, total_income, total_outcome, flow, cash, 
                    small_business, medium_business, big_business, stocks, bonds, deposits, autos, flats, lands, chalets, yachts, flies, mansions, menu_id, id_last_active, debt'''
BD_MOK_VALUES = '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?'
BD_BLANC_PARAMS = ['', '', 'мир бедных', 0, 0, 0, 0, 0, 'доп. заработок', 0, 0, 0, 0, 0, 'доп. расходы', 0, 0, 0, 0, 0, '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', 0, 0, 0]
BD_TEST_USER = [1, 1, 'повар', 'мужской', 'мир бедных', False, 2, 0, 1, 200, 'ставки', 30, 10, 10, 10, 10, 'бассейн', 10, 230, 50, 100, 20, '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', '[]', 0, 0, 0]

#text constants
TEXT_WELCOME = '🖖Греби лопатой Assistent приветствует Вас, '

TEXT_WELCOME2 = '\n\nЕсли Вы здесь, значит ближайшие несколько часов будут наполнены эмоциями. Надеемся, они будут только положительными! 🎉'

TEXT_WELCOME3 = 'В данной игре важен не только игровой процесс, но и ваши мысли, желания и идеи, возникающие в ходе или после игры 🎲'\
            + '\n\nПоэтому, если Вы хотите получить максимальную пользу и удовольствие от игры, мы рекомендуем после нее провести некоторое время '\
            + 'в состоянии рефлексии, осмысляя свои собственные действия и их причины в спокойной обстановке 💆‍♂️'

TEXT_WELCOME4 = 'Балансовая ведомость создана.\nВыберите дальнейшее действие!'
TEXT_WELCOME5 = 'Пользователь не найден!\nСоздайте новую балансовую ведомость или выберите из стандартных.'
TEXT_WELCOME6 = 'Выберите способ создания балансовой ведомости.'
TEXT_WELCOME7 = 'Выберите уровень дохода стандартной профессии.'
TEXT_WELCOME8 = 'Выберите базовую профессию.'

BALANCE_Q1 = '🔧 Введите вашу профессию'
BALANCE_Q2 = '🚻 Выберите пол персонажа'
BALANCE_Q3 = '💵 Введите количество наличных'
BALANCE_Q4 = '💳 Введите вашу зарплату'
BALANCE_Q5 = '🧮 Введите название статьи ваших дополнительных доходов'
BALANCE_Q6 = '🧮 Введите сумму ваших дополнительных доходов'
BALANCE_Q7 = '🏠 Введите сумму ваших расходов на жилье'
BALANCE_Q8 = '🍤 Введите сумму ваших расходов на питание'
BALANCE_Q9 = '🚕 Введите сумму ваших расходов на проезд'
BALANCE_Q10 = '👕 Введите сумму ваших расходов на одежду'
BALANCE_Q11 = '🪂 Введите название статьи ваших дополнительных расходов'
BALANCE_Q12 = '🪂 Введите сумму ваших дополнительных расходов'

ERROR1 = 'Ошибка⚠️\nВведенное значение должно быть целым числом! Попробуйте снова.'
ERROR2 = 'Ошибка⚠️\nПол должен быть либо "мужской", либо "женский"! Попробуйте снова.'
ERROR3 = 'Ошибка⚠️\nВведенное значение должно быть текстовым значением! Попробуйте снова.'

ACTION1 = 'Выберите действие в меню'

BALANCE_1 = '🔧 Профессия:'
BALANCE_2 = '🚻 Пол:'
BALANCE_3 = '💵 Наличные:'
BALANCE_4 = '💳 Зарплата:'
BALANCE_5 = '🧮'
BALANCE_6 = '🏠 Расходы на жильё:'
BALANCE_7 = '🍤 Расходы на еду:'
BALANCE_8 = '🚕 Расходы на транспорт:'
BALANCE_9 = '👕 Расходы на одежду:'
BALANCE_10 = '🪂'
BALANCE_11 = '📈 Суммарные доходы:'
BALANCE_12 = '📉 Суммарные расходы:'
BALANCE_13 = '💰 Денежный поток:'

BALANCE_14 = '👣 Ход:'
BALANCE_15 = '🌍 Мир:'
BALANCE_16 = '🎁 Исполненных причуд:'
BALANCE_17 = '👫 Брак:'
BALANCE_18 = '🚼 Дети:'

BALANCE_19 = 'Активы'
BALANCE_20 = '💼 Бизнесы:'
BALANCE_21 = '🧾 Ценные бумаги:'
BALANCE_22 = '🚁 Движимое имущество:'
BALANCE_23 = '🏭 Недвижимое имущество:'
BALANCE_24 = '🪙 Депозиты:'
BALANCE_25 = '💳 Кредиты:'
BALANCE_26 = '⭕ Долги:'
DELIMETER = '-----------------------------------'

BUSINESS_1 = 'Сначала продайте бизнесы другого уровня!'
BUSINESS_2 = 'Введите название бизнеса'
BUSINESS_3 = 'Введите стоимость бизнеса'
BUSINESS_4 = 'Введите доход от бизнеса'
BUSINESS_5 = 'У вас нет бизнесов!'
BUSINESS_6 = 'Вы лишились последнего купленного бизнеса!'

BUY_1 = 'У вас недостаточно средств!'
BUY_2 = 'Поздравляем с покупкой!'
BUY_3 = 'Поздравляем с продажей!'
BUY_4 = 'Введите порядковый номер актива'
BUY_5 = 'Актива с таким порядковым номером не существует!'
BUY_6 = 'Значение актива изменено'
BUY_7 = 'Введите цену продажи актива'

PAPERS_1 = 'Введите тикер бумаги'
PAPERS_2 = 'Введите цену покупки бумаги'
PAPERS_3 = 'Введите количество покупаемых бумаг'
PAPERS_4 = 'Введите купон облигации'
PAPERS_5 = 'Введите срок действия'
PAPERS_6 = f'Введите сумму вклада (кратную {s.DEPOSIT_KEY_VALUE})'
PAPERS_7 = 'Введите ставку по вкладу'
PAPERS_8 = f'Сумма депозита не кратна {s.DEPOSIT_KEY_VALUE}'

ACTIVE_1 = 'Введите название актива'
ACTIVE_2 = 'Введите стоимость актива'
ACTIVE_3 = 'Вы оформляете кредит? Да/Нет'
ACTIVE_4 = 'Введите срок кредита'
ACTIVE_5 = 'Введите ежемесячный платеж'

ABOUT_1 = f'''
    Вот несколько советов по использованию данного бота-ассистента, которые помогут Вам в дальнейшей игре:
{DELIMETER}
<b>№1</b> - прежде чем начинать играть, ознакомтесь с базовыми правилами, которые Вы найдете в коробке с игрой.
{DELIMETER}
<b>№2</b> - в зависимости от количества игроков и их опыта игра может занять длительное время (не менее 4 часов). Поэтому запаситесь временем и терпением. 
{DELIMETER}
<b>№3</b> - обязательно используйте кнопку "Завершить месяц", когда попадаете или пересекаете сектор "Прибыль" или сектор "Старт". Так Вы ничего не упустите и получите все что Вам полагается.
{DELIMETER}
<b>№4</b> - при изменении или продаже актива на вопрос ассистента Вам будет необходимо ввести ID актива, который Вы увидите самым первым параметром у любого из активов в таблице в появившемся списке.
{DELIMETER}
<b>№5</b> - если при выполнении операции что-то пошло не так и Вы не знаете как вернуться в главное меню - отправьте в чат сообщение "Главное меню" или очистите историю чата и затем в начале диалога выберите кнопку "Продолжить игру".
{DELIMETER}
<b>№6</b> - в случае возникновения технических неполадок Вы можете обратиться в службу поддержки в нашем сообществе, перейдя по кнопке "Сообщество".
'''

ABOUT_2 = '''
        Основным элементом взаимодействия с ассистентом является меню.\n
В меню игры содержаться вспомогательные функции, а также кнопки перехода в другой мир этой "фантасмагоричной" игры.\n
Затем Вы встретите блок функций по работе с наличными деньгами и большой блок функций по работе с вашими активами, собственностью и прочим. В нем Вы сможете купить или продать вашу собственность, и даже изменить ее характеристики в случае необходимости (а она точно появится).\n
И последний крупный блок - жизненные ситуации, которые не обойдут Вас стороной и в этой игре.\n
Отдельно Вы увидите в меню 3 самые частые кнопки, которыми Вам предстоит пользоваться: кнопка окончания отчетного периода (месяца), кнопка вывода всех ваших активов на текущий момент и общая сводка вашей текущей жизни.\n
<b>Не забывайте ими пользоваться - они друзья!</b>\n
'''

ABOUT_3 = '''
У некоторых кнопок Вы увидите символ "☰". 
Он означает, что при нажатии на эту кнопку Вам откроется новое подменю для выбора.
Карту кнопок меню и их взаимное положение Вы можете увидеть на картинке.
'''

PROFESSIONS = {
    'lvl1': [
        {'name': 'Охранник', 'cash': 100, 'salary': 250, 'salary_extra_name': 'Левак с остатков', 'salary_extra': 50, 'cost_house': 100, 'cost_food': 60, 'cost_transport': 10, 'cost_cloth': 20, 'cost_extra_name': 'Кроссоврды', 'cost_extra': 10},
        {'name': 'Кладовщик', 'cash': 110, 'salary': 270, 'salary_extra_name': 'Неучтенка', 'salary_extra': 40, 'cost_house': 100, 'cost_food': 60, 'cost_transport': 20, 'cost_cloth': 10, 'cost_extra_name': 'Пазлы', 'cost_extra': 10},
        {'name': 'Участковый', 'cash': 120, 'salary': 370, 'salary_extra_name': 'Все время в работе', 'salary_extra': 0, 'cost_house': 100, 'cost_food': 80, 'cost_transport': 20, 'cost_cloth': 10, 'cost_extra_name': 'Рыбалка', 'cost_extra': 40},
        {'name': 'Продавец-кассир', 'cash': 130, 'salary': 300, 'salary_extra_name': 'Неучтенка', 'salary_extra': 30, 'cost_house': 110, 'cost_food': 60, 'cost_transport': 10, 'cost_cloth': 10, 'cost_extra_name': 'Любовные романы', 'cost_extra': 10},
        {'name': 'Продавец-консультант', 'cash': 140, 'salary': 330, 'salary_extra_name': 'Процент от продаж', 'salary_extra': 60, 'cost_house': 120, 'cost_food': 60, 'cost_transport': 10, 'cost_cloth': 30, 'cost_extra_name': 'Мини-футбол', 'cost_extra': 30},
        {'name': 'Кондуктор', 'cash': 150, 'salary': 290, 'salary_extra_name': 'Гид на выходные', 'salary_extra': 60, 'cost_house': 100, 'cost_food': 60, 'cost_transport': 10, 'cost_cloth': 10, 'cost_extra_name': 'Судоку', 'cost_extra': 20},
        {'name': 'Водитель троллейбуса', 'cash': 160, 'salary': 360, 'salary_extra_name': 'Видеоблог', 'salary_extra': 50, 'cost_house': 110, 'cost_food': 80, 'cost_transport': 30, 'cost_cloth': 20, 'cost_extra_name': 'Детективные романы', 'cost_extra': 10},
        {'name': 'Няня', 'cash': 170, 'salary': 400, 'salary_extra_name': 'Аниматор', 'salary_extra': 70, 'cost_house': 130, 'cost_food': 30, 'cost_transport': 20, 'cost_cloth': 70, 'cost_extra_name': 'Танцы на пилоне', 'cost_extra': 50},
        {'name': 'Официант', 'cash': 180, 'salary': 280, 'salary_extra_name': 'Чаевые', 'salary_extra': 100, 'cost_house': 100, 'cost_food': 40, 'cost_transport': 20, 'cost_cloth': 20, 'cost_extra_name': 'Походы', 'cost_extra': 20},
        {'name': 'Фармацевт', 'cash': 190, 'salary': 380, 'salary_extra_name': 'Спирт из-под полы', 'salary_extra': 60, 'cost_house': 120, 'cost_food': 80, 'cost_transport': 10, 'cost_cloth': 30, 'cost_extra_name': 'Ночные клубы', 'cost_extra': 10},
        {'name': 'Учитель', 'cash': 200, 'salary': 400, 'salary_extra_name': 'Репетиторство', 'salary_extra': 100, 'cost_house': 100, 'cost_food': 100, 'cost_transport': 30, 'cost_cloth': 30, 'cost_extra_name': 'Театр', 'cost_extra': 40},
        {'name': 'Сантехник', 'cash': 210, 'salary': 370, 'salary_extra_name': 'Муж на час', 'salary_extra': 90, 'cost_house': 100, 'cost_food': 60, 'cost_transport': 20, 'cost_cloth': 20, 'cost_extra_name': 'Скалолазание', 'cost_extra': 50},
        {'name': 'Парикмахер', 'cash': 220, 'salary': 430, 'salary_extra_name': 'Макияж к прическам', 'salary_extra': 140, 'cost_house': 130, 'cost_food': 100, 'cost_transport': 60, 'cost_cloth': 20, 'cost_extra_name': 'Разведение фиалок', 'cost_extra': 40},
        {'name': 'Крановщик', 'cash': 230, 'salary': 520, 'salary_extra_name': 'Видеоблог', 'salary_extra': 60, 'cost_house': 160, 'cost_food': 80, 'cost_transport': 50, 'cost_cloth': 40, 'cost_extra_name': 'Фотография', 'cost_extra': 20},
        {'name': 'Сварщик', 'cash': 240, 'salary': 510, 'salary_extra_name': 'Прямые заказы', 'salary_extra': 80, 'cost_house': 140, 'cost_food': 80, 'cost_transport': 40, 'cost_cloth': 50, 'cost_extra_name': 'Конные прогулки', 'cost_extra': 40}
    ],

    'lvl2': [
        {'name': 'Мастер маникюра', 'cash': 250, 'salary': 550, 'salary_extra_name': 'Постоянные клиенты', 'salary_extra': 100, 'cost_house': 170, 'cost_food': 110, 'cost_transport': 40, 'cost_cloth': 40, 'cost_extra_name': 'Караоке', 'cost_extra': 40},
        {'name': 'Тренер по фитнесу', 'cash': 260, 'salary': 520, 'salary_extra_name': 'Продажа БАДов', 'salary_extra': 90, 'cost_house': 140, 'cost_food': 100, 'cost_transport': 40, 'cost_cloth': 40, 'cost_extra_name': 'Бассейн', 'cost_extra': 30},
        {'name': 'Медработник', 'cash': 270, 'salary': 510, 'salary_extra_name': 'Уколы на дому', 'salary_extra': 60, 'cost_house': 120, 'cost_food': 70, 'cost_transport': 20, 'cost_cloth': 30, 'cost_extra_name': 'Рыбалка', 'cost_extra': 60},
        {'name': 'Секретарь', 'cash': 280, 'salary': 500, 'salary_extra_name': 'Ручные поделки', 'salary_extra': 180, 'cost_house': 140, 'cost_food': 100, 'cost_transport': 60, 'cost_cloth': 70, 'cost_extra_name': 'Бисероплетение', 'cost_extra': 30},
        {'name': 'Косметолог', 'cash': 290, 'salary': 590, 'salary_extra_name': 'Брови, массаж', 'salary_extra': 200, 'cost_house': 190, 'cost_food': 140, 'cost_transport': 50, 'cost_cloth': 70, 'cost_extra_name': 'Фотография', 'cost_extra': 50},
        {'name': 'Тракторист', 'cash': 300, 'salary': 300, 'salary_extra_name': 'Калым', 'salary_extra': 300, 'cost_house': 130, 'cost_food': 100, 'cost_transport': 10, 'cost_cloth': 30, 'cost_extra_name': 'Чтение газет', 'cost_extra': 30},
        {'name': 'Следователь', 'cash': 310, 'salary': 760, 'salary_extra_name': 'Честный человек', 'salary_extra': 0, 'cost_house': 160, 'cost_food': 130, 'cost_transport': 80, 'cost_cloth': 60, 'cost_extra_name': 'Игра на гитаре', 'cost_extra': 20},
        {'name': 'Стоматолог', 'cash': 320, 'salary': 690, 'salary_extra_name': 'Мимо кассы', 'salary_extra': 130, 'cost_house': 260, 'cost_food': 170, 'cost_transport': 20, 'cost_cloth': 30, 'cost_extra_name': 'Скетчинг', 'cost_extra': 20},
        {'name': 'Журналист', 'cash': 330, 'salary': 650, 'salary_extra_name': 'Блог о путешествиях', 'salary_extra': 80, 'cost_house': 100, 'cost_food': 150, 'cost_transport': 70, 'cost_cloth': 40, 'cost_extra_name': 'Нумизматика', 'cost_extra': 40},
        {'name': 'Переводчик', 'cash': 340, 'salary': 340, 'salary_extra_name': 'Репетиторство', 'salary_extra': 300, 'cost_house': 100, 'cost_food': 100, 'cost_transport': 50, 'cost_cloth': 30, 'cost_extra_name': 'Вязание', 'cost_extra': 20},
        {'name': 'Водитель фуры', 'cash': 350, 'salary': 750, 'salary_extra_name': 'Подвезти попутчика', 'salary_extra': 50, 'cost_house': 190, 'cost_food': 160, 'cost_transport': 20, 'cost_cloth': 50, 'cost_extra_name': 'Чтение фантастики', 'cost_extra': 30},
        {'name': 'Дизайнер', 'cash': 360, 'salary': 670, 'salary_extra_name': 'Фриланс', 'salary_extra': 190, 'cost_house': 280, 'cost_food': 150, 'cost_transport': 20, 'cost_cloth': 30, 'cost_extra_name': 'Фитнес', 'cost_extra': 20},
        {'name': 'Бухгалтер', 'cash': 370, 'salary': 770, 'salary_extra_name': 'Забот хватает', 'salary_extra': 0, 'cost_house': 100, 'cost_food': 150, 'cost_transport': 70, 'cost_cloth': 40, 'cost_extra_name': 'Бар по пятницам', 'cost_extra': 40},
        {'name': 'Кондитер', 'cash': 380, 'salary': 650, 'salary_extra_name': 'Торты на заказ', 'salary_extra': 180, 'cost_house': 130, 'cost_food': 150, 'cost_transport': 50, 'cost_cloth': 50, 'cost_extra_name': 'Трекинг по горам', 'cost_extra': 70},
        {'name': 'Прораб', 'cash': 390, 'salary': 670, 'salary_extra_name': 'Сбыт цемента', 'salary_extra': 70, 'cost_house': 170, 'cost_food': 120, 'cost_transport': 20, 'cost_cloth': 30, 'cost_extra_name': 'Чтение журналов', 'cost_extra': 10},
        {'name': 'Инженер', 'cash': 400, 'salary': 800, 'salary_extra_name': 'Фриланс', 'salary_extra': 100, 'cost_house': 190, 'cost_food': 160, 'cost_transport': 50, 'cost_cloth': 50, 'cost_extra_name': 'Настольные игры', 'cost_extra': 50},
        {'name': 'Таксист', 'cash': 410, 'salary': 790, 'salary_extra_name': 'Доставка еды', 'salary_extra': 120, 'cost_house': 150, 'cost_food': 140, 'cost_transport': 130, 'cost_cloth': 30, 'cost_extra_name': 'Компьютерные игры', 'cost_extra': 50}
    ],

    'lvl3': [
        {'name': 'Редактор журнала', 'cash': 420, 'salary': 780, 'salary_extra_name': 'Каналы в соцсетях', 'salary_extra': 190, 'cost_house': 230, 'cost_food': 140, 'cost_transport': 110, 'cost_cloth': 30, 'cost_extra_name': 'Фитнес', 'cost_extra': 40},
        {'name': 'Маркетолог', 'cash': 430, 'salary': 770, 'salary_extra_name': 'Реклама в соцсетях', 'salary_extra': 160, 'cost_house': 240, 'cost_food': 140, 'cost_transport': 80, 'cost_cloth': 40, 'cost_extra_name': 'Прогулки по парку', 'cost_extra': 0},
        {'name': 'Инспектор ГАИ', 'cash': 440, 'salary': 640, 'salary_extra_name': 'Взятки', 'salary_extra': 300, 'cost_house': 250, 'cost_food': 170, 'cost_transport': 40, 'cost_cloth': 30, 'cost_extra_name': 'Кроссоврды', 'cost_extra': 10},
        {'name': 'Пилот авиалиний', 'cash': 450, 'salary': 800, 'salary_extra_name': 'Билеты по блату', 'salary_extra': 200, 'cost_house': 300, 'cost_food': 120, 'cost_transport': 40, 'cost_cloth': 60, 'cost_extra_name': 'Мини-футбол', 'cost_extra': 30},
        {'name': 'Хирург', 'cash': 460, 'salary': 1060, 'salary_extra_name': 'Была бы возможность', 'salary_extra': 0, 'cost_house': 280, 'cost_food': 120, 'cost_transport': 60, 'cost_cloth': 60, 'cost_extra_name': 'Подледная рыбалка', 'cost_extra': 80},
        {'name': 'Шеф-повар', 'cash': 470, 'salary': 770, 'salary_extra_name': 'Фуд-тренинги', 'salary_extra': 250, 'cost_house': 310, 'cost_food': 130, 'cost_transport': 30, 'cost_cloth': 40, 'cost_extra_name': 'Астрономия', 'cost_extra': 40},
        {'name': 'Риэлтор', 'cash': 480, 'salary': 480, 'salary_extra_name': 'Продажа щенков', 'salary_extra': 600, 'cost_house': 290, 'cost_food': 120, 'cost_transport': 100, 'cost_cloth': 50, 'cost_extra_name': 'Кино', 'cost_extra': 40},
        {'name': 'Прокурор', 'cash': 490, 'salary': 890, 'salary_extra_name': 'Домашняя пасека', 'salary_extra': 250, 'cost_house': 270, 'cost_food': 160, 'cost_transport': 50, 'cost_cloth': 70, 'cost_extra_name': 'Пейнтбол', 'cost_extra': 100},
        {'name': 'Военный', 'cash': 500, 'salary': 850, 'salary_extra_name': 'Было бы время', 'salary_extra': 0, 'cost_house': 50, 'cost_food': 100, 'cost_transport': 50, 'cost_cloth': 50, 'cost_extra_name': 'Охота', 'cost_extra': 100},
        {'name': 'Разработчик видеоигр', 'cash': 600, 'salary': 850, 'salary_extra_name': 'Ремонт компьютеров', 'salary_extra': 250, 'cost_house': 100, 'cost_food': 200, 'cost_transport': 30, 'cost_cloth': 30, 'cost_extra_name': 'Видеогры', 'cost_extra': 140},
        {'name': 'Адвокат', 'cash': 700, 'salary': 1000, 'salary_extra_name': 'Частные консультации', 'salary_extra': 300, 'cost_house': 300, 'cost_food': 150, 'cost_transport': 30, 'cost_cloth': 100, 'cost_extra_name': 'Картинг', 'cost_extra': 20},
        {'name': 'Технический директор', 'cash': 800, 'salary': 1450, 'salary_extra_name': 'Дел невпроворот', 'salary_extra': 0, 'cost_house': 300, 'cost_food': 150, 'cost_transport': 30, 'cost_cloth': 150, 'cost_extra_name': 'Что? Где? Когда?', 'cost_extra': 20},
        {'name': 'Брокер ', 'cash': 900, 'salary': 1100, 'salary_extra_name': 'Реклама в соцсетях', 'salary_extra': 300, 'cost_house': 200, 'cost_food': 120, 'cost_transport': 90, 'cost_cloth': 80, 'cost_extra_name': 'Рафтинг', 'cost_extra': 10},
        {'name': 'Программист', 'cash': 1000, 'salary': 1050, 'salary_extra_name': 'Фриланс', 'salary_extra': 500, 'cost_house': 150, 'cost_food': 170, 'cost_transport': 60, 'cost_cloth': 70, 'cost_extra_name': 'Альпинизм', 'cost_extra': 100},
        {'name': 'Банкир', 'cash': 1100, 'salary': 1000, 'salary_extra_name': 'Все хотели бы знать', 'salary_extra': 750, 'cost_house': 200, 'cost_food': 150, 'cost_transport': 30, 'cost_cloth': 70, 'cost_extra_name': 'Покер', 'cost_extra': 200},
        {'name': 'Проститутка', 'cash': 1200, 'salary': 1000, 'salary_extra_name': 'Курсы сексолога', 'salary_extra': 600, 'cost_house': 130, 'cost_food': 100, 'cost_transport': 20, 'cost_cloth': 70, 'cost_extra_name': 'Кулинарные шедевры', 'cost_extra': 80}
    ]
}