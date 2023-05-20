import aiohttp
import requests
from .settings import *

def get_date_id(date:str):
    try:
        response = requests.get(GET_DATE_ID.substitute(date=date)).json()['id']
    except requests.RequestException:
        response = 0
        
    print(response)
    return response

def get_group_id(group_name:str):
    try:
        response = requests.get(GET_GROUP_ID.substitute(group_name=group_name)).json()['id']
    except requests.RequestException:
        response = 0
        
    print(response)
    return response
    
async def get_dated_lessons(group_id: int, date_id:int):
    try:
        async with aiohttp.ClientSession() as session:
            request = GET_LESSONS_BY_DATE.substitute(group_id=group_id, date_id=date_id)
            async with session.get(request) as resp:
                print(await resp.json())
                return await resp.json()
    except aiohttp.ClientConnectionError:
        return 0
    
    
async def get_week_lessons(group_id: int, week_number: int):
    try:
        async with aiohttp.ClientSession() as session:
            request = GET_LESSONS_BY_WEEK.substitute(group_id=group_id, week_number=week_number)
            async with session.get(request) as resp:
                return await resp.json()
    except aiohttp.ClientConnectionError:
        return 0