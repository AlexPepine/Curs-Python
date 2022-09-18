# Tema Conditional programming, loops, functions & modularityFile

def calcul(a, b, c, d, e):
    return a + b + c


result = calcul(1, 5, -3, 'abc', [12, 56, 'cad'])
print(result)


def zero(a):
    return a


print(zero(0))


def calcul_second(a, b, c, param_1=2):
    return a+b


result_second = calcul_second(2, 4, 'abc')
print(result_second)


def get_sum(n):
    if n == 0:
        return 0
    return n + get_sum(n-1)


print(get_sum(10))


def get_sum_para(n):
    # print(n)
    if n == 2:
        return 2
    return n + get_sum_para(n-2)



print(get_sum_para(10))


def get_sum_impara(n):
    # print(n)
    if n == 1:
        return 1
    return n + get_sum_impara(n-2)



print(get_sum_impara(11))


val = input("Introdu numar")

print(int(val))
