duration = int(input('Введите время в секундах: '))
day = (duration // (24 * 60 * 60))
hours = (duration // (60 * 60) - 24 * day)
minutes = (duration // 60 % 60)
seconds = duration % 60
print(day, 'дн', hours, 'час(ов)', minutes, 'мин', seconds, 'сек')