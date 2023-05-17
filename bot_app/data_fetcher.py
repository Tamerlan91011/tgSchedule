import aiohttp
import requests
from .config import GET_LESSON_BY_DATE, GET_DATE_ID


def get_date_id(date:str):
    try:
        response = requests.get(GET_DATE_ID.substitute(date=date)).json()['id']
    except:
        response = 0
        
    print(response)
    return response
    
async def get_today_lessons(group_id: int, date_id:int):
    async with aiohttp.ClientSession() as session:
        request = GET_LESSON_BY_DATE.substitute(group_id=group_id, date_id=date_id)
        async with session.get(request) as resp:
            print(await resp.json())
            return await resp.json()