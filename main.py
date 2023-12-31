import asyncio
from EduAPI.methods import *

async def main():
    auds = await getAudlist()
    for aud in auds:
        if aud.name == '1-384':
            rasps = await getRaspAudlist(aud.id) 
    # rasps = await getRaspTeacher(186,'2023-12-15')


if __name__ == '__main__':
    asyncio.run(main())