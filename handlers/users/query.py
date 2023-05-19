import json
import psycopg2

from aiogram import F, Router
from aiogram.types import Message
from aiohttp import connector

from models import Admin, User
from keyboards.reply.users import admin, main_panel

user_admin_router = Router(name='user_admin_panel')

password = ['Qazsew112121']
# admins_id = [321312, 412412]
db_host = '127.0.0.1'
db_port = '5432'
db_name = 'boss'
db_user = 'postgres'
db_password = '1121'

conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
cursor = conn.cursor()
query = "SELECT * FROM users"
cursor.execute(query)
# json.dumps(connector.fetchall())

results = cursor.fetchall()


# @user_admin_router.message(F.text == '/admin')
# async def command_admin(message: Message):
#     await message.delete()
#     if await Admin.get(pk=message.from_user.id):
#         await message.answer(text='рад вас видеть😄', reply_markup=admin)
#     else:
#         await message.answer(text='Доступ закрыт', reply_markup=main_panel)
#

@user_admin_router.message(F.text == 'Проверить пользователей🥳')
async def send_start_ikb(message: Message):
    # await message.delete()
    for row in results:
        go = f"{row}"
        await message.answer(
            text=go,
            reply_markup=admin)



# @user_admin_router.message(F.text == '/password')
# async def command_admin(message: Message):
#     await message.delete()
#     if await Admin.get(pk=)

        #
        # else:
        # user = User(id=message.from_user.id, name=message.from_user.full_name, )
        # await user.save()
        # await message.answer(text='ДОБРО ПОЖАЛОВАТЬ! 📸', reply_markup=main_panel)