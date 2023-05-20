import string
import emoji

"""
Текст сообщений, используемый в ответах чат-бота на запросы пользователя
"""

INFO_EMOJI = emoji.emojize(":information:")

# Сообщения кнопок для пользователя
TODAY = "Занятия сегодня"
TOMOROW = "Занятия завтра"
THIS_WEEK = "Занятия на этой неделе"
NEXT_WEEK = "Занятия на следующей неделе"
GREETINGS = "Привет!\nВведи число и получишь фамилию одного из преподавателей"

START_SCHEDULE = f'''
Выберите один из 4-х представленных ниже вариантов.\n
{INFO_EMOJI} Расписание на неделю показывает занятия в принципе,
даже когда фактически они уже закончились.\n
{INFO_EMOJI} Расписание на сегодня и завтра показывают фактические занятия, опираясь на даты.'''


# Сообщение об ошибке запроса
SOMETHING_BROKEN = "Упс, что-то сломалось, повторите запрос"


# Сообщения об отсутствии занятий
NO_TODAY = "Сегодня занятий нет"
NO_TOMORROW = "Завтра занятий нет"
NO_THIS_WEEK = "На этой неделе занятий нет"
NO_NEXT_WEEK = "На следующей неделе занятий нет"

NO_LESSONS = "Занятий в расписании нет"

# Шаблоны для занятий
LESSON = string.Template(f'''
$lesson_type
$lesson_time
$auditorium
Проводит: $teacher
Даты: $dates
''')
