import json
import psycopg2

from aiogram import F, Router
from aiogram.types import Message
from aiohttp import connector

from models import Admin, User
from keyboards.reply.users import admin, main_panel, pass_panel

user_password_router = Router(name='user_password_router')

key = ['1121']
url='https://www.google.com/imgres?imgurl=https%3A%2F%2Fpythonru.com%2Fwp-content%2Fuploads%2F2021%2F02%2Finline-klaviatura.png&tbnid=L4cO0_Iny9AZoM&vet=12ahUKEwjL3LGrjvr-AhVDtioKHVOVBh4QMygSegUIARC-AQ..i&imgrefurl=https%3A%2F%2Fpythonru.com%2Fprimery%2Ffunkcionalnost-telegram-bota&docid=3p8MH0mJORijEM&w=383&h=190&q=пользователь%20вводит%20в%20боте%20aiogram%203&client=safari&ved=2ahUKEwjL3LGrjvr-AhVDtioKHVOVBh4QMygSegUIARC-AQ'


# @user_password_router.message(F.text == '/password')
# async def password_command(message: Message):
#     await message.answer(f'Приятно видеть тебя{message.from_user.first_name}')
#

@user_password_router.message(F.text == '/password')
async def get_text_message(message: Message):
    await message.answer('Привет нажми на кнопку', reply_markup=pass_panel)
    # else:
    #     await message.answer('кто ты воин?', reply_markup=main_panel)


@user_password_router.message(F.text == 'Проверим кто ты?')
async def proporty(message: Message):
    await message.delete()
    if await Admin.get(pk=message.from_user.id):
        await message.answer(text=f'Снова зравствуйте {message.from_user.full_name}😎', reply_markup=admin)
    else:
        user = Admin(id=message.from_user.id, name=message.from_user.full_name)
        await user.save()
        await message.answer(text=f'ДОБРО ПОЖАЛОВАТЬ!, {message.from_user.full_name} Вы новый админ нашей команды 📸', reply_markup=admin)







# await message.answer(text='А скажи-ка мне пароль')
#     # if "1121" in message.text.lower():

# @dp.message_handler(content_types=['text'])
# async def get_text_messages(msg: types.Message):
#     if msg.text.lower() == 'привет':
#         await msg.answer('Привет!')
#     else:
#         await msg.answer('Не понимаю, что это значит.')
    # await message.delete()
    # if await Admin.get(pk=message.from_user.id):
    #     await message.answer(text='hi admin', reply_markup=admin)
    # else:
    #     password = 'usdt'
    #     await message.answer(text='Введите пароль')
    #     await message.from_user.text
    #     if message.text == password:
    #         user = Admin(id=message.from_user.id, name=message.from_user.full_name)
    #         await user.save()
    #         await message.answer(text='ДОБРО ПОЖАЛОВАТЬ! 📸', reply_markup=admin)
    #     else:
    #         await message.answer(text='hello', reply_markup=main_panel)

#
    #     if message.text == 1121:
    #         await message.answer(text='добро', reply_markup=admin)
    #     else:
    #         await message.answer(text='вам сюда нельзя')
    # else:
    #     await message.answer(reply_markup=main_panel)

    # await message.answer(text='Введите пароль')
    # if message.text == password:
    #     ad = Admin(pk=message.from_user.id, name=message.from_user.full_name)
    #     await ad.save()
    #     await message.answer(text='hi', reply_markup=admin)
    # else:
    #     await message.answer(text='no')


        # if message.text == '1121':
        #     ad = Admin(pk=message.from_user.id, name=message.from_user.full_name)
        #     await ad.save()
        #     await message.answer(text='hi', reply_markup=admin)
        # else:
        #     await message.answer('no hi', reply_markup=main_panel)
        #


        # if message.text == '1121':
        #     ad = Admin(pk=message.from_user.id, name=message.from_user.full_name)
        #     await ad.save()
        #     await message.answer('Добро', reply_markup=admin)
        # else:
        #     await message.answer('не добро', reply_markup=main_panel)





    #     elif await message.answer(text='пароль?'):
    #     await message.text == '1121':
    #     admin = Admin(id=message.from_user.id, name=message.from_user.full_name)
    #     await admin.save()
    #     await message.answer('hi', reply_markup=admin)
    # else:
    #     await message.answer('пошел нахер', reply_markup=main_panel)


    #     admin = Admin(id=message.from_user.id, name=message.from_user.full_name)
    #     await admin.save()
    #     await message.answer('hi', reply_markup=admin)
    # else:
    #     await message.answer('None')


