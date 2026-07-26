# Додатково для практики створила альтернативну версію task 1,
# яка запитує дату у користувача через input() 
# та повторює введення до отримання коректного формату. 
# Ця версія не є частиною домашнього завдання.

from datetime import datetime

def get_days_from_today():

    now_date = datetime.today()

    while True:
        try:
            user_date = input("Введіть дату (рррр-мм-дд): ")
            specified_date = datetime.strptime(user_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Неправильний формат дати, спробуй ще раз")


    difference_between_dates = now_date - specified_date
    return difference_between_dates.days

print("Різнийя між датами у днях:", get_days_from_today())