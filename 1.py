from analyze import check_time


@check_time
def multiply(number=10, start=1):
    summa = 0
    for i in range(start, number):
        if i % 3 == 0 or i % 5 == 0:
            summa += i
    return summa

@check_time
def multiply1(number=10):
    summa = 0
    for i in range(3, number, 3):
        summa += i

    for i in range(5, number, 5):
        if i % 3 != 0:
            summa += i

    return summa

@check_time
def multiply2(number=10):
    values = {}
    for i in range(3, number, 3):
        values[i] = i

    for i in range(5, number, 5):
        values[i] = i

    return sum(values.values())

@check_time
def multiply3(number=10):
    values = {}
    summa = 0
    for i in range(3, number, 3):
        values[i] = i
        summa += i

    for i in range(5, number, 5):
        if i not in values:
            summa += i

    return summa


def sum_sequence_with_step(step, max_sequence):
    count_numbers = max_sequence // step
    return step*(count_numbers*(count_numbers+1)) // 2


@check_time
def multiply4(number=10):
    number -= 1
    return sum_sequence_with_step(3, number) + sum_sequence_with_step(5, number) - sum_sequence_with_step(15, number)


@check_time
def multiply5(number=10):
    '''Худшая производительность из-за вложенности циклов'''
    m = (3, 5)
    s = 0
    for i in range(1, number):
        for n in m:
            if i % n == 0:
                s += i
                break
    return s


print(multiply(10000000))
print(multiply1(10000000))
print(multiply2(10000000))
print(multiply3(10000000))
print(multiply5(10000000))
print(multiply4(10000000))



