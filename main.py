# from models import Start, Category, Brand, Model, Admin
#
#
# async def main():
#     N = ['max']
#     for n in N:
#         n = Admin(
#             id=594555381,
#             name=n
#         )
#         await n.save()
#
#
# if __name__ == '__main__':
#     import asyncio
#     asyncio.run(main())
#
#
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

