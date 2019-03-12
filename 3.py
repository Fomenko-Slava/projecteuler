from analyze import check_time


def is_simple_number(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


@check_time
def simple_div(number):
    start = number // 3 # минимальное число которое может быть, с него начинаем и идём вниз
    for i in range(start, 3, -1):
        if number % i == 0: # если число кратно i
            if is_simple_number(i):
                return i

    return 'нет простого делителя'


@check_time
def simple_div1(number):
    for i in range(3, number // 2, 2):
        factor = number / i
        if factor.is_integer():  # если число кратно i
            if is_simple_number(int(factor)):
                return int(factor)

    return 'нет простого делителя'

#print(simple_div(600851475143)) # очень долго работает
#print(simple_div(1319511211))
#print(simple_div(13195))
print(simple_div1(6008514751431))