from dataclasses import dataclass
import string
from dotenv import load_dotenv
import os

load_dotenv('.env')

"""
Настройки для корректной работы чат-бота
"""

@dataclass
class Student:
    student_card_number: int = 0
    password: str = 'admin'
    group_id: int = 0
    group_name: str = 'Админ'
    username: str = 'Админ'

API_TOKEN = os.environ.get('API_TOKEN')

HOST = 'http://127.0.0.1:8000'

SCHEDULE_API = 'schedule'

STUDENTS_API = 'students'

GET_LESSONS_BY_DATE = string.Template(
    f'{HOST}/{SCHEDULE_API}/lessons/group/$group_id/date/$date_id')

GET_LESSONS_BY_WEEK = string.Template(
    f'{HOST}/{SCHEDULE_API}/lessons/group/$group_id/week/$week_number')

GET_DATE_ID = string.Template(f'{HOST}/{SCHEDULE_API}/lesson-date/$date')

GET_GROUP_ID = string.Template(
    f'{HOST}/{STUDENTS_API}/group-name/$group_name')

GET_STUDENT_TELEGRAM_ID = string.Template(
    f'{HOST}/{STUDENTS_API}/telegram/$telegram_id')