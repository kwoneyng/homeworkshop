def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divid(a, b):
    try :
        result = a / b
    except ZeroDivisionError :
        return print('0으로는 나눌 수 없어')
    return result