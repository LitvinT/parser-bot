from models import Start, Category, Brand, Model, Admin, Image
#
#
# async def main():
#     N = ['screenshot2023.05.18.11.42.24.png']
#     for n in N:
#         n = Image(
#             image=n
#         )
#         await n.save()
# #
#
# async def main():
#     n = Image(
#         image='screenshot2023.05.18.11.40.44.png'
#     )
#     await n.save()
#
#
# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())


#
#
# import psycopg2
# import json
#
# # Установка соединения с базой данных PostgreSQL
# conn = psycopg2.connect(
#     host="хост",
#     port="порт",
#     database="имя_базы_данных",
#     user="пользователь",
#     password="пароль"
# )
#
# # Создание курсора для выполнения SQL-запросов
# cur = conn.cursor()
#
# # Выполнение SQL-запроса
# cur.execute("SELECT * FROM your_table")
#
# # Получение результатов
# rows = cur.fetchall()
#
# # Преобразование результатов в список словарей
# results = []
# for row in rows:
#     results.append(dict(zip(cur.description, row)))
#
# # Преобразование списка словарей в формат JSON
# json_data = json.dumps(results)
#
# # Вывод JSON-данных
# print(json_data)
#
# # Закрытие курсора и соединения с базой данных
# cur.close()
# conn.close()

