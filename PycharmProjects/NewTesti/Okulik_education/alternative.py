nums = [1, 2, 5, 9, 0, 7]

def new_nums(num):

    if num % 2 == 0:
        return True
    else:
        return False

list_nums = filter(new_nums, nums)
print(list(list_nums))

#Дан список чисел (включая отрицательные и ноль). Используя filter(), создайте список, содержащий только положительные числа.
my_string = [1, 2, 5, 9, 0, 7, -1]

def open_string(x):
    if x > -1:
        return True
    else:
        return False

new = filter(open_string, my_string)
print(list(new))



