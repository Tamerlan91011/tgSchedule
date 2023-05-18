from dataclasses import dataclass
import string
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv('.env')

"""
Настройки для корректной работы чат-бота
"""

@dataclass
class Student:
    student_card_number: int
    group_id: int = 8
    group_name: str = 'СКЗ-2'


connection = mysql.connector.connect(
    host=os.environ.get('HOST'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('PASSWORD'),
    database=os.environ.get('DATABASE'))

API_TOKEN = os.environ.get('API_TOKEN')

HOST = 'http://127.0.0.1:8000'

API_MODULE = 'schedule'

GET_LESSON_BY_DATE = string.Template(
    f'{HOST}/{API_MODULE}/lessons/group/$group_id/date/$date_id')

GET_DATE_ID = string.Template(f'{HOST}/{API_MODULE}/lesson-date/$date')