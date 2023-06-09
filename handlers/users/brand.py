from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.users import brand_paginator_ikb, all_list_ikb
from keyboards.inline.users.general import UserCallbackData
from keyboards.reply.users import walet_panel
from models.models import Asic
from parser.test_par import parse_and_save, connect_to_db

user_brand_router = Router(name='user_brand')


@user_brand_router.callback_query(UserCallbackData.filter((F.target == 'brand') & (F.action == 'get')))
async def get_brand(callback: CallbackQuery, callback_data: UserCallbackData):
    connect_to_db()

    user = callback.from_user.id
    category = callback_data.category_id

    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute(f"""UPDATE users SET category_id = (%s) WHERE id = (%s)""", (category, user))
    conn.commit()

    cur.close()
    conn.close()

    if callback_data.videocard_id != 0 and callback_data.videocard_id != None:
        await callback.message.edit_text(
            text='Отлично, теперь ты точно знаешь, какое оборудование тебе необходимо. Перейдем к следующему шагу.'
        )
        await callback.message.answer(
            text='Нужен ли вам хостинг?',
            reply_markup=await brand_paginator_ikb(callback_data=callback_data)
        )
    elif callback_data.category_id == 1:
        await callback.message.answer('выберете валюту ', reply_markup=walet_panel)

    elif callback_data.category_id == 2:
        await callback.message.edit_text(
            text='Спасибо за ответ! К вам подключится специалист для обсуждения всех условий ☺',
        )
    else:
        await callback.message.edit_text(
            text='Нужен ли вам хостинг?',
            reply_markup=await brand_paginator_ikb(callback_data=callback_data)
        )