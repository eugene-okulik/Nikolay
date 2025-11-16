# задание 1
number = 5
while True:
    enter_num = int(input('Enter num: '))
    if enter_num != number:
        print('попробуйте снова')
        # continue
    elif enter_num == number:
        print('Поздравляю! Вы угадали!')
        break

print('Досвидания!')
