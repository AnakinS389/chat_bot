from aiogram import types
from create_bot import bot, Dispatcher
from bot_source.keyboards import keyboard_start, keyboard_remove, keyboard_faculty, keyboard_course
from bot_source.keyboards import keyboard_group_1, keyboard_group_2, keyboard_group_3, keyboard_group_4, keyboard_group_5
from bot_source.other.utilities import get_coinflip_util, get_prediction_util
from microservice import database_read
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from bot_source.filters.filters import date_filter
from bot_source.database import database_schedule
from aiogram.types import WebAppInfo, WebAppData, MenuButtonWebApp, InlineKeyboardButton, InlineKeyboardMarkup


'''*************** Клиентская часть ***************'''


class FSMClient(StatesGroup):
    faculty_name = State()
    course = State()
    group_name = State()
    date = State()


# @dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, f'Добро пожаловать, {msg.from_user.username}\nДанный бот - это упрощенная версия личного кабинета СамГТУ',
                           reply_markup=keyboard_start)
    '''await bot.set_chat_menu_button(chat_id=msg.from_user.id, menu_button=MenuButtonWebApp(type='web_app', text='Открыть',
                                                                    web_app=WebAppInfo(url='https://yandex.ru/maps/?um=constructor%3Ab6bcbe3077bdc2c667464c0950a1d98ef9ba7d8a2e4118e7bcbb3f3bdbb56c24&source=constructorLink')))'''
#https://simpleunidomain.ru/start_Page.html
# @dp.message_handler(commands=['Подбросить монетку'])
async def get_coinflip(msg: types.Message):
    await bot.send_message(msg.from_user.id, get_coinflip_util())


    async def get_route(msg: types.Message):
        inline_start_button = InlineKeyboardButton("Перейти",
                                                       web_app=WebAppInfo(url='https://simpleunidomain.ru/start_Page.html')) #https://simpleunidomain.ru/start_Page.html
        inline_start_keyb = InlineKeyboardMarkup().add(inline_start_button)

        await bot.send_message(msg.from_user.id, 'Нажми на кнопку, чтобы построить маршрут', reply_markup=inline_start_keyb)


# @dp.message_handler(commands=['Получить педсказание'])
async def get_prediction(msg: types.Message):
    await bot.send_message(msg.from_user.id, get_prediction_util())


# @dp.message_handler(commands=['Узнать расписание'], state=None)
async def get_schedule(msg: types.Message):
    await FSMClient.faculty_name.set()
    await msg.reply('Выберите ваш факультет:\nВ данный момент поддерживается только ИАИТ, в будущем мы подключим и другие факультеты:\nДля отмены введите "cancel"', reply_markup=keyboard_faculty)


# @dp.message_handler(content_types=['text'], state=FSMClient.faculty)
async def input_faculty(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['faculty_name'] = msg.text
    await FSMClient.course.set()
    await msg.reply('Отлично, теперь выберите курс', reply_markup=keyboard_course)


# @dp.message_handler(content_types=['text'], state=FSMClient.month)
async def input_month(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['course'] = msg.text
        await FSMClient.group_name.set()
        if data['course'] == '1':
            await bot.send_message(msg.from_user.id, 'Превосходно, теперь выберите вашу группу',
                                   reply_markup=keyboard_group_1)
        elif data['course'] == '2':
            await bot.send_message(msg.from_user.id, 'Превосходно, теперь выберите вашу группу',
                                   reply_markup=keyboard_group_2)
        elif data['course'] == '3':
            await bot.send_message(msg.from_user.id, 'Превосходно, теперь выберите вашу группу',
                                   reply_markup=keyboard_group_3)
        elif data['course'] == '4':
            await bot.send_message(msg.from_user.id, 'Превосходно, теперь выберите вашу группу',
                                   reply_markup=keyboard_group_4)
        else:
            await bot.send_message(msg.from_user.id, 'Превосходно, теперь выберите вашу группу',
                                   reply_markup=keyboard_group_5)


async def input_date_point(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group_name'] = msg.text
    await FSMClient.date.set()
    await msg.reply('Теперь внимательно введите дату, в формате xx.xx.xxxx\n Например: 01.09.2023')


# @dp.message_handler(content_types=['text'], state=FSMClient.date)
async def input_date(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = msg.text

        await state.update_data(data)
        try:
            result = await database_read.main(state)
            await bot.send_message(msg.from_user.id, 'Расписание:', reply_markup=keyboard_start)
            for record in result:
                await bot.send_message(msg.from_user.id, f'Предмет: {record["discipline_name"]}: {record["plan_time_name"]} - {record["date"]} - {record["time"]} - '
                                                         f'{record["building_name"]} - {record["auditorium_name"]} - {record["teacher_names"]}')
        except Exception as err:
            await bot.send_message(msg.from_user.id, 'На данный день расписания не нашлось', reply_markup=keyboard_start)
        await state.finish()


# @dp.message_handler(state="*", commands=['Cancel'])
# @dp.message_handler(Text(equals='Cancel', ignore_case=True), state="*")
async def cancel_handler(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Ok', reply_markup=keyboard_start)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_coinflip, text=['Подбросить монетку'])
    dp.register_message_handler(get_route, text=['Навигация'])
    dp.register_message_handler(get_prediction, text=['Получить предсказание'])
    dp.register_message_handler(cancel_handler, state="*", commands=['Cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state="*")
    dp.register_message_handler(get_schedule, text=['Узнать расписание'], state=None)
    dp.register_message_handler(input_faculty, content_types=['text'], state=FSMClient.faculty_name)
    dp.register_message_handler(input_month, content_types=['text'], state=FSMClient.course)
    dp.register_message_handler(input_date_point, content_types=['text'], state=FSMClient.group_name)
    dp.register_message_handler(input_date, content_types=['text'], state=FSMClient.date)

