import telebot
from telebot import types
import random

token = telebot.TeleBot('6813348990:AAGGigDJlV_KBZ8kESF9DEAAglyokCzAc4w')  # токен от BotFather

# в этом множестве записаны малоизвестные факты о космосе
fact_sp = ['Солнце в 300 000 раз больше, чем наша планета Земля',
           'Солнце полностью проворачивается вокруг своей оси за 25-35 дней',
           'Солнце теряет до 1 000 000 тонн своей массы каждую секунду из-за солнечного ветра',
           'У меркурия и Венеры отсутствуют какие-либо спутники',
           'Вeнeрa являeтся eдинствeннoй плaнeтoй, кoтoрaя врaщaeтся в прoтивoпoлoжнyю стoрoнy oтнoситeльнo дрyгих '
           'плaнeт Сoлнeчнoй систeмы',
           'Ио, спутник Юпитера - самое вулканическое место в солнечной системе',
           'У Юпитера самое большое количество спутников, у него их 67',
           'Сатурн обладает низкой плотностью, и если его положить в воду, то он поплывёт',
           'Уран имеет уникальный наклон, из-за этого одна ночь на нём длится 21 год',
           'Сейчас в Солнечной системе насчитывается 5 карликовых планет: Церера, Плутон, Хаумеа, Эрида и Макемаке',
           'Сoвeтский и рoссийский кoсмoнaвт Сeргeй Кoнстaнтинoвич Крикaлёв являeтся рeкoрдсмeнoм пo врeмeни '
           'нaхoждeния в кoсмoсe: 803 дня, 9 чaсов и 39 минyт, это чуть больше 2х лет',
           'В северной части неба можно увидеть две галактики: галактику Андромеда(М31) и галактику Треугольник(М33)',
           'Прямо сейчас к нам приближается галактика Андромеда',
           'В кoсмoсe нaсчитывaeтся пoрядкa 2^1023 звёзд, этo 200 000 000 000 000 000 000 000 000 000!',
           'Один день на Плутоне равен 6 дням и 9 часам на Земле',
           'Следы, оставленные на Луне, не исчезнут, пока нет ветра',
           'Закат на Марсе синего цвета', 'Земля - единственная планета, не названная в честь Бога',
           'На Юпитере и Сатурне идет алмазный дождь',
           'В космосе звезд больше, чем песчинок в мире', 'Только 5% Вселенной видно с Земли',
           'В любой момент на Земле происходит не менее 2000 гроз',
           'Мы знаем больше о Марсе и нашей Луне, чем о океанах',
           'Астронавты могут вырасти примерно на 5 см в высоту, находясь в космосе',
           'Наша Луна удаляется от Земли со скоростью 4 см в год', 'МКС видна более чем 90% населения Земли',
           'Юпитер спасает Землю от астероидов, он притягивает своей гравитацией большинство астероидов',
           'День на Меркурии равен 58 земным дням',
           'Шариковые ручки не работают в космосе, поэтому космонавтам выдают карандаши',
           'Существует планета, полностью состоящая из алмазов',
           'Масса Солнца составляет 99.86% от массы всей Солнечной системы, оставшиеся 0.14% приходятся на планеты и '
           'астероиды',
           'Человек сможет выжить в открытом космосе без скафандра в течение 90 секунд, если немедленно выдохнет весь'
           'воздух из легких',
           'Магнитное поле Юпитера настолько мощное, что ежедневно обогащает магнитное поле нашей планеты миллиардами '
           'Ватт',
           'Самый большой астероид в Солнечной системе имеет диаметр 525 километров',
           'На Земле деревьев больше, чем звезд в Млечном Пути',
           'Следы лунной посадки, вероятно, все еще будут видны через миллионы лет']


# функция старта
# с ее помощью бот начинает работу и приветствует пользователя
@token.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Российский космос')
    btn2 = types.KeyboardButton('Новости')
    btn3 = types.KeyboardButton('Проекты и мероприятия')
    btn4 = types.KeyboardButton('Знания')
    btn5 = types.KeyboardButton('Навигация профессий')
    btn6 = types.KeyboardButton('Учителю')
    btn7 = types.KeyboardButton('Поиск')
    btn8 = types.KeyboardButton('Вы точно этого не знали!')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    token.send_message(message.from_user.id, 'Вас приветствует бот для сайта Space4Kids', reply_markup=markup)
    token.send_message(message.from_user.id,
                       'Сайт Space4Kids создан для того, чтобы вы смогли получить актуальную информаци и новые знания '
                       о космосе')
    token.send_message(message.from_user.id, 'Бот поможет вам найти то, что вы хотите за считанные секунды')
    token.send_message(message.from_user.id, 'Выберите интересующий вас раздел')


# в этой функции описаны все кнопки бота и их функции
@token.message_handler(content_types=['text'])
def message_txt(message):
    if message.text == 'Вы точно этого не знали!':
        for i in range(10):
            token.send_message(message.from_user.id, random.choice(fact_sp))
            # после того как пользователь выберет кнопку "Вы точно этого не знали!"
            # программа выведет сообщением 10 фактов о космосе

    elif message.text == 'Российский космос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('История')
        btn2 = types.KeyboardButton('Техника')
        btn3 = types.KeyboardButton('Космодромы')
        btn4 = types.KeyboardButton('Космонавты')
        btn5 = types.KeyboardButton('Следуй за космонавтом')
        btn6 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        token.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)

    elif message.text == 'История':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nИстория\n\nhttps://space4kids.ru/140', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Техника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nТехника\n\nhttps://space4kids.ru/138', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Космодромы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмодромы\n\nhttps://space4kids.ru/139',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Космонавты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмонавты\n\nhttps://space4kids.ru/40', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Следуй за космонавтом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nСледуй за космонавтом\n\nhttps://space4kids.ru/131',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Российский космос')
        btn2 = types.KeyboardButton('Новости')
        btn3 = types.KeyboardButton('Проекты и мероприятия')
        btn4 = types.KeyboardButton('Знания')
        btn5 = types.KeyboardButton('Навигация профессий')
        btn6 = types.KeyboardButton('Учителю')
        btn7 = types.KeyboardButton('Поиск')
        btn8 = types.KeyboardButton('Вы точно этого не знали!')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        token.send_message(message.from_user.id, 'Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Новости':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nНовости\n\nhttps://space4kids.ru/101', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Проекты и мероприятия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('Главное меню')
        btn1 = types.KeyboardButton('Кванториум')
        btn2 = types.KeyboardButton('Сириус')
        btn3 = types.KeyboardButton('Университетская гимназия МГУ')
        btn4 = types.KeyboardButton('Центр космонавтики и авиации')
        btn5 = types.KeyboardButton('Космический класс')
        btn6 = types.KeyboardButton('Космические смены')
        btn7 = types.KeyboardButton('Программа "Универсат"')
        btn8 = types.KeyboardButton('Cansat Russia')
        btn9 = types.KeyboardButton('Проект космический урок')
        btn10 = types.KeyboardButton('World skills Russia')
        btn11 = types.KeyboardButton('Билет в будующее')
        btn12 = types.KeyboardButton('ПроеКТОриЯ')
        btn13 = types.KeyboardButton('Форумная кампания')
        btn14 = types.KeyboardButton('Космофест Восточный')
        btn15 = types.KeyboardButton('КосмоСтарт')
        btn16 = types.KeyboardButton('Олимпиада НТИ')
        btn17 = types.KeyboardButton('Дежурный по планете')
        btn19 = types.KeyboardButton('Nauka 0+')
        btn20 = types.KeyboardButton('Профстажировка.рф 2.0')
        btn21 = types.KeyboardButton('Неделя без турникетов')
        btn22 = types.KeyboardButton('Космос')
        btn23 = types.KeyboardButton('Самбо в школу')
        btn24 = types.KeyboardButton('Лунная одиссея')
        btn25 = types.KeyboardButton('Большая перемена')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14,
                   btn15, btn16, btn17, btn19, btn20, btn21, btn22, btn23, btn24, btn25)
        token.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)

    elif message.text == 'Кванториум':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКванториум\n\nhttps://space4kids.ru/473',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Сириус':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел\nСириус\n\nhttps://space4kids.ru/474', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Университетская гимназия МГУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nУниверситетская гимназия МГУ\n\nhttps://space4kids.ru/475',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Центр космонавтики и авиации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nЦентр космонавтики и авиации\n\nhttps://space4kids.ru/117',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Космический класс':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмический класс\n\nhttps://space4kids.ru/477',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Космические смены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмические смены\n\nhttps://space4kids.ru/478',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Программа "Универсат"':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nПрограмма "Универсат"\n\nhttps://space4kids.ru/482',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Cansat Russia':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nCansat Russia\n\nhttps://space4kids.ru/479',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Проект космический урок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nПроект космический урок\n\nhttps://space4kids.ru/490',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'World skills Russia':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nWorld skills Russia\n\nhttps://space4kids.ru/476',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Билет в будующее':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nБилет в будующее\n\nhttps://space4kids.ru/486',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ПроеКТОриЯ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nПроеКТОриЯ\n\nhttps://space4kids.ru/480',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Форумная кампания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nФорумная кампания\n\nhttps://space4kids.ru/487',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Космофест Восточный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмофест Восточный\n\nhttps://space4kids.ru/483',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'КосмоСтарт':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмоСтарт\n\nhttps://space4kids.ru/484',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Олимпиада НТИ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nОлимпиада НТИ\n\nhttps://space4kids.ru/485',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Дежурный по планете':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nДежурный по планете\n\nhttps://space4kids.ru/488',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Nauka 0+':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nNauka 0+\n\nhttps://space4kids.ru/576', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Профстажировка.рф 2.0':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nПрофстажировка.рф 2.0\n\nhttps://space4kids.ru/481',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Неделя без турникетов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nНеделя без турникетов\n\nhttps://space4kids.ru/573',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Космос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКосмос\n\nhttps://space4kids.ru/489', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Самбо в школу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nСамбо в школу\n\nhttps://space4kids.ru/491',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Лунная одиссея':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nЛунная одиссея\n\nhttps://space4kids.ru/1186',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Большая перемена':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nБольшая перемена\n\nhttps://space4kids.ru/1714',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Знания':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('Главное меню')
        btn1 = types.KeyboardButton('Лекции')
        btn2 = types.KeyboardButton('Книги')
        btn3 = types.KeyboardButton('Документальные фильмы')
        btn4 = types.KeyboardButton('Телепередачи')
        btn5 = types.KeyboardButton('Художественные фильмы')
        btn6 = types.KeyboardButton('Мультфильмы')
        btn7 = types.KeyboardButton('Доступно о космосе')
        btn8 = types.KeyboardButton('Журналы')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        token.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)

    elif message.text == 'Лекции':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nЛекции\n\nhttps://space4kids.ru/118', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Книги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКниги\n\nhttps://space4kids.ru/127', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Документальные фильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nДокументальные фильмы\n\nhttps://space4kids.ru/126',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Телепередачи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nТелепередачи\n\nhttps://space4kids.ru/128',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Художественные фильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nХудожественные фильмы\n\nhttps://space4kids.ru/656',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Мультфильмы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nМультфильмы\n\nhttps://space4kids.ru/1753',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Доступно о космосе':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nДоступно о космосе\n\nhttps://space4kids.ru/125',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Журналы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nЖурналы\n\nhttps://space4kids.ru/980', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Навигация профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('Главное меню')
        btn1 = types.KeyboardButton('Каталог профессий')
        btn2 = types.KeyboardButton('Образовательные организации')
        btn3 = types.KeyboardButton('Организации госкорпарации "Роскосмос"')
        btn4 = types.KeyboardButton('Профориентационное тестирование')
        markup.add(btn01, btn1, btn2, btn3, btn4)
        token.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)

    elif message.text == 'Каталог профессий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nКаталог профессий\n\nhttps://space4kids.ru/108',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Образовательные организации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nОбразовательные организации\n\nhttps://space4kids.ru/110',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Организации госкорпарации "Роскосмос"':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id,
                           'Раздел:\nОрганизации госкорпарации "Роскосмос"\n\nhttps://space4kids.ru/950',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Профориентационное тестирование':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id,
                           'Раздел:\nПрофориентационное тестирование\n\nhttps://space4kids.ru/112', reply_markup=markup,
                           parse_mode='Markdown')

    elif message.text == 'Учителю':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn01 = types.KeyboardButton('Главное меню')
        btn1 = types.KeyboardButton('Концепция программ "Космический класс"')
        btn2 = types.KeyboardButton('Методические материалы')
        btn3 = types.KeyboardButton('Музеи и центры просвещения')
        btn4 = types.KeyboardButton('Олимпиады и конкурсы')
        btn5 = types.KeyboardButton('Проектная деятельность')
        btn6 = types.KeyboardButton('Уроки и эксперименты')
        btn7 = types.KeyboardButton('Плакаты и постеры')
        markup.add(btn01, btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        token.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)

    elif message.text == 'Концепция программ "Космический класс"':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id,
                           'Раздел:\nКонцепция программ "Космический класс"\n\nhttps://space4kids.ru/120',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Методические материалы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nМетодические материалы\n\nhttps://space4kids.ru/121',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Музеи и центры просвещения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nМузеи и центры просвещения\n\nhttps://space4kids.ru/122',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Олимпиады и конкурсы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nОлимпиады и конкурсы\n\nhttps://space4kids.ru/124',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Проектная деятельность':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nПроектная деятельность\n\nhttps://space4kids.ru/880',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Уроки и эксперименты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nУроки и эксперименты\n\nhttps://space4kids.ru/881',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Плакаты и постеры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id, 'Раздел:\nПлакаты и постеры\n\nhttps://space4kids.ru/1707',
                           reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Поиск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        markup.add(btn1)
        token.send_message(message.from_user.id,
                           'Перейдя по [ссылке] https://space4kids.ru/search вы сможете сами найти то, что вам нужно',
                           reply_markup=markup, parse_mode='Markdown')


token.polling(none_stop=True)
