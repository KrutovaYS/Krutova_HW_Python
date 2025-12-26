def month_to_season(month_number):
    if month_number in [1, 2, 12]:
        return 'Зима'
    if month_number in [3, 4, 5]:
        return 'Весна'
    if month_number in [6, 7, 8]:
        return 'Лето'
    if month_number in [9, 10, 11]:
        return 'Осень'
    else:
        return 'Неверный номер месяца'
        
try:
    month_number = int(input('Введите число от 1 до 12: '))
except ValueError:
    print('Ошибка: введите числовое значение от 1 до 12')
else:
    season = month_to_season(month_number)
    print(season)
