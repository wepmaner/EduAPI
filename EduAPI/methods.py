import aiohttp
from .types import Group, Day, Audience
from typing import List
async def method(url,**params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
                print(response.url)
                result = await response.json()
                return result['data']
        

async def listYear() -> list:
    '''Список доступных годов'''
    result = await method(f'https://edu.donstu.ru/api/Rasp/ListYears')
    return result['years']

async def currentYear() -> str:
    '''Текущий год'''
    result = await method(f'https://edu.donstu.ru/api/Rasp/ListYears')
    return result['years'][-1]

async def getGroups(year:str = None) -> List[Group]:
    '''Список групп'''
    if year is None:
        year = await currentYear()
    groups = await method(f'https://edu.donstu.ru/api/raspGrouplist',year=year)
    return [Group(**group) for group in groups]

async def getRaspGroup(idGroup:int, sdate:str='') -> List[Day]:
    '''Расписание группы'''
    rasps = await method(f'https://edu.donstu.ru/api/Rasp', idGroup=idGroup, sdate=sdate)
    return [Day(**rasp) for rasp in rasps['rasp']]

async def getRaspTeacher(idTeacher:int, sdate:str='') -> List[Day]:
    '''Расписание преподавателя'''
    rasps = await method(f'https://edu.donstu.ru/api/Rasp', idTeacher=idTeacher, sdate=sdate)
    return [Day(**rasp) for rasp in rasps['rasp']]

async def getAudlist(year:str = None) -> List[Audience]:
    '''Список аудиторий'''
    if year is None:
        year = await currentYear()
    Audiences = await method(f'https://edu.donstu.ru/api/raspAudlist', year=year)
    return [Audience(**audience) for audience in Audiences]

async def getRaspAudlist(idAudLine:int,sdate:str='') -> List[Day]:
    '''Расписание аудитории'''
    rasps = await method(f'https://edu.donstu.ru/api/Rasp', idAudLine=idAudLine, sdate=sdate)
    return [Day(**rasp) for rasp in rasps['rasp']]





