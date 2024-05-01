from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, \
    InlineKeyboardMarkup

menu_buttons = [ 

]

buttons_start = ['Навигация',
    'Подбросить монетку',
    'Узнать расписание',
    'Получить предсказание']

keyboard_start = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_start.add(*buttons_start)

buttons_faculty = ['Институт автоматики и информационных технологий']
keyboard_faculty = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_faculty.add(*buttons_faculty)


buttons_course = ['1',
                  '2',
                  '3',
                  '4',
                  '5']
keyboard_course = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_course.add(*buttons_course)

buttons_group_1 = ['23ИАИТ–101',
                   '23ИАИТ-102',
                   '23ИАИТ-103',
                   '23ИАИТ-104',
                   '23ИАИТ-105',
                   '23ИАИТ-106',
                   '23ИАИТ-107',
                   '23ИАИТ-108',
                   '23ИАИТ-109',
                   '23ИАИТ-110',
                   '23ИАИТ-111',
                   '23ИАИТ-112',
                   '23ИАИТ-119',
                   '23ИАИТ-129',
                   '23ИАИТ-309',
                   '23ИАИТ-315']

keyboard_group_1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_group_1.add(*buttons_group_1)

buttons_group_2 = ['22ИАИТ-101',
                   '22ИАИТ-102',
                   '22ИАИТ-103',
                   '22ИАИТ-104',
                   '22ИАИТ-105',
                   '22ИАИТ-106',
                   '22ИАИТ-107',
                   '22ИАИТ-108',
                   '22ИАИТ-109',
                   '22ИАИТ-110',
                   '22ИАИТ-111',
                   '22ИАИТ-112',
                   '22ИАИТ-113',
                   '22ИАИТ-114',
                   '22ИАИТ-117',
                   '22ИАИТ-119',
                   '22ИАИТ-309',
                   '22ИАИТ-315']

keyboard_group_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_group_2.add(*buttons_group_2)

buttons_group_3 = ['21ИАИТ-101',
                   '21ИАИТ-102',
                   '21ИАИТ-103',
                   '21ИАИТ-104',
                   '21ИАИТ-105',
                   '21ИАИТ-106',
                   '21ИАИТ-107',
                   '21ИАИТ-108',
                   '21ИАИТ-109',
                   '21ИАИТ-110',
                   '21ИАИТ-111',
                   '21ИАИТ-112',
                   '21ИАИТ-113',
                   '21ИАИТ-114',
                   '21ИАИТ-117',
                   '21ИАИТ-119',
                   '21ИАИТ-309',
                   '21ИАИТ-315']
keyboard_group_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_group_3.add(*buttons_group_3)

buttons_group_4 =['20фаит-1',
                  '20фаит-2',
                  '20фаит-3',
                  '20фаит-4',
                  '20фаит-5',
                  '20фаит-6',
                  '20фаит-7',
                  '20фаит-8',
                  '20фаит-9',
                  '20фаит-10',
                  '20фаит-11',
                  '20фаит-12']
keyboard_group_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_group_4.add(*buttons_group_4)

buttons_group_5 = ['ЗФ-Д41',
                   'ЗФ-Д44']
keyboard_group_5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_group_5.add(*buttons_group_5)

keyboard_remove = ReplyKeyboardRemove()
