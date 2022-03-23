import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher
from aiogram.types import ReplyKeyboardRemove
from keyboard import *
from main import get_vacancies


class FSMJobInfo(StatesGroup):
    published_all = State()
    keyword = State()
    period = State()
    payment_from = State()
    no_agreement = State()
    town = State()
    experience = State()


async def get_keyword(message: types.Message):
    await FSMJobInfo.keyword.set()
    await message.answer(f'Привет,{message.from_user.first_name}')
    await asyncio.sleep(1)
    await message.answer(f'Ключевые слова для поиска вакансий:')


async def load_keyword(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['keyword'] = message.text
    await FSMJobInfo.next()
    await message.answer('За какой период сделать поиск:', reply_markup=get_period_keyboard())


async def load_period(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == '24 часа':
            data['period'] = 1
        elif message.text == '3 дня':
            data['period'] = 3
        elif message.text == 'Неделя':
            data['period'] = 7
        elif message.text == 'За все время':
            data['period'] = 0
    await FSMJobInfo.next()
    await message.answer('Зарплата от(только число):', reply_markup=ReplyKeyboardRemove())


async def load_payment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['payment_from'] = int(message.text)
    await FSMJobInfo.next()
    await message.answer('Показывать зарплату по договоренности', reply_markup=get_agreement_keyboard())


async def load_agreement(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Да':
            data['no_agreement'] = 0
        elif message.text == 'Нет':
            data['no_agreement'] = 1
    await FSMJobInfo.next()
    await message.answer('В каком городе искать:', reply_markup=ReplyKeyboardRemove())


async def load_town(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['town'] = message.text
    await FSMJobInfo.next()
    await message.answer('Ваш опыт работы', reply_markup=get_experience_keyboard())


async def load_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Без опыта':
            data['experience'] = 1
        elif message.text == 'От 1 года':
            data['experience'] = 2
        elif message.text == 'От 3 лет':
            data['experience'] = 3
        elif message.text == 'От 6 лет':
            data['experience'] = 4
    async with state.proxy() as data:
        await message.answer(f'Ожидайте, идет подборка вакансий', reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(1.5)
        params = {'published_all': True,
                  'keyword': data['keyword'],
                  'period': data['period'],
                  'payment_from': data['payment_from'],
                  'no_agreement': data['no_agreement'],
                  'town': data['town'],
                  'experience': data['experience']
                  }
        for vacancy in get_vacancies(params):
            await message.answer(vacancy, disable_web_page_preview=True)
            await asyncio.sleep(1.5)
    await state.finish()


def register_handler_state(dp: Dispatcher):
    dp.register_message_handler(get_keyword, commands=['start'], state=None)
    dp.register_message_handler(load_keyword, state=FSMJobInfo.keyword)
    dp.register_message_handler(load_period, state=FSMJobInfo.period)
    dp.register_message_handler(load_payment, state=FSMJobInfo.payment_from)
    dp.register_message_handler(load_agreement, state=FSMJobInfo.no_agreement)
    dp.register_message_handler(load_town, state=FSMJobInfo.town)
    dp.register_message_handler(load_experience, state=FSMJobInfo.experience)
