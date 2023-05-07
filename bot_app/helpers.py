from datetime import date, timedelta


# Получение сегодняшней даты
def getTodayDate():
    return date.today()


# Получение завтрашней даты
def getTomorrowDate():
    return date.today() + timedelta(days=1)


# Получение дат текущей недели
def getThisWeekDates():
    today = date.today()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)

    return (str(start), str(end))


# Получение дат следующей недели
def getNextWeekDates():
    today = date.today()
    thisWeekStart = today - timedelta(days=today.weekday())
    nextWeekStart = thisWeekStart + timedelta(days=7)
    nexrWeekEnd = nextWeekStart + timedelta(days=6)

    return (str(nextWeekStart), str(nexrWeekEnd))
