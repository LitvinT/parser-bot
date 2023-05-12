from models import Start, Category, Brand, Model, Admin


async def main():
    N = ['max']
    for n in N:
        n = Admin(
            id=594555381,
            name=n
        )
        await n.save()


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
