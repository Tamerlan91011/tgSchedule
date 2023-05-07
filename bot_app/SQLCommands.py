from .helpers import getTodayDate, getTomorrowDate
from .core import groupName

# Запрос на получение всех преподавателей
allPersonnelUser = "SELECT id, name FROM personnel_user"

# Запрос для получения всех данных расписания на сегодня
allTodaySchedule = f"""
    select sl.id, sg.name, auditorium, pu.name, start_time, end_time, sl2.name, sl3.date
    from shedule_lesson sl
    join shedule_lesson_teacher slt on slt.lesson_id=sl.id
    join personnel_user pu on pu.id=slt.user_id
    join shedule_academiccouple sa on sa.id=sl.academic_couple_id
    join shedule_lessontype sl2 on sl.type_name_id=sl2.id
    join shedule_lesson_lesson_date slld on slld.lesson_id=sl.id
    join shedule_lessondate sl3 on sl3.id=slld.lessondate_id
    join shedule_lesson_group slg on sl.id=slg.lesson_id
    join students_group sg on slg.group_id=sg.id
    where sg.name like '{groupName}' and sl3.date like '{getTodayDate()}'
    order by start_time
    """


# Запрос для получения всех данных расписания на завтра
allTomorrowSchedule = f"""
    select sl.id, sg.name, auditorium, pu.name, start_time, end_time, sl2.name, sl3.date
    from shedule_lesson sl
    join shedule_lesson_teacher slt on slt.lesson_id=sl.id
    join personnel_user pu on pu.id=slt.user_id
    join shedule_academiccouple sa on sa.id=sl.academic_couple_id
    join shedule_lessontype sl2 on sl.type_name_id=sl2.id
    join shedule_lesson_lesson_date slld on slld.lesson_id=sl.id
    join shedule_lessondate sl3 on sl3.id=slld.lessondate_id
    join shedule_lesson_group slg on sl.id=slg.lesson_id
    join students_group sg on slg.group_id=sg.id
    where sg.name like '{groupName}' and sl3.date like '{getTomorrowDate()}'
    order by start_time
    """
