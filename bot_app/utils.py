from datetime import date, timedelta
from bot_app import messages

from types import CoroutineType

# Получение сегодняшней даты
def returnTodayDate():
    return date.today()

# Получение завтрашней даты
def returnTomorrowDate():
    return date.today() + timedelta(days=1)


def returnWeekNumber():
    week = (date.today().isocalendar()[1]) % 2

    # Если неделя четная, то она в расписании обозначается, как вторая неделя.
    # Иначе первая
    if not week:
        return 2
    return week


def concatString(list: CoroutineType, field_name: str) -> str:
    result = ''
    for j in range(len(list)):
        result += f'{list[j].get(field_name)}, '
    return result[:-2]


def fillLessonsMessage(res: CoroutineType) -> str:
    lessons_message = ''
    for i in range(len(res)):
        teachers = concatString(res[i].get("teacher"), 'name')
        lesson_dates = concatString(res[i].get("lesson_date"), 'date')

        lessons_message += messages.LESSON.substitute(
            lesson_type=res[i].get("lesson_type"),
            auditorium=res[i].get("auditorium"),
            teacher=teachers,
            lesson_time=res[i].get("lesson_time"),
            dates=lesson_dates
        )

    return lessons_message
