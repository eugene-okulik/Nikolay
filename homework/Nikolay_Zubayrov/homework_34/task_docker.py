number = 5
while True:
    enter_num = int(input('Enter num: '))
    if enter_num != number:
        print('попробуйте снова')

    elif enter_num == number:
        print('Поздравляю! Вы угадали!')
        break

print('Досвидания!')
