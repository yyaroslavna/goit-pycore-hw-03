from datetime import datetime

def get_days_from_today(date):

    now_date = datetime.today().date() 
    # Не знаю чи варто додавати date(), бо і без цього воно показуватиме просто дні 

    try:
        specified_date = datetime.strptime(date, "%Y-%m-%d").date()
        #Тут те саме питання до date()
    except ValueError:
        return "Неправильний формат дати, спробуй ще раз"


    difference_between_dates = now_date - specified_date
    return difference_between_dates.days

print(get_days_from_today("2021-10-09"))
