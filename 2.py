from analyze import check_time

@check_time
def fibonachi(limit):
    prev_val = 1
    next_val = 1
    summa = 0
    while next_val < limit:
        if next_val % 2 == 0:
            summa += next_val

        prev_val, next_val = next_val, (prev_val + next_val)

    return summa

@check_time
def fibonachi1(limit):
    a = 1
    b = 1
    c = a + b
    summa = 0
    while c < limit:
        #print(c)
        summa += c
        a = b + c
        b = c + a
        c = a + b

    return summa


print(fibonachi(4000000))
print(fibonachi1(4000000))
