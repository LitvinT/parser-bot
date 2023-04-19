from models import Start, Text


async def main():
    N = ['👋 Привет, Мы компания Interhash, Занимаемся предоставлением комплексных услуг для майнинга. Мы на рынке с 2017 года и являемся официальным представителями майнинг-пула ViaBTC в Европе и странах СНГ.']
    for n in N:
        n = Text(
            text=n,
        )
        await n.save()





if __name__ == '__main__':
    import asyncio
    asyncio.run(main())