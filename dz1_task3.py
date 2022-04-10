percentages = input('Введите колличество процентов: ')
number = {1,2,3,4}
for i in range(100):
    i = i + 1
    if i in number:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 > 1 and i % 10 < 5:
        print(i, 'процента')
    else:
        print(i, 'процентов')
