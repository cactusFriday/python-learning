'''
корутины - генераторы, которые могут принимать какие-то данные
from inspect import getgeneratorstate - инспектор генераторов
Первым делом конструкция subgen должна принять None, тогда gen_suspended, после чего можно передавать значение .send() и пробрасывать исключения .throw()
yield может принимать значения через метод .send()
'''

# from inspect import getgeneratorstate as gstate

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

def subgen():
    # При первой итерации (передача None) выполняется все до строки с yield и yield x (справа после '=')
    x = 'Ready to accept message'
    message = yield x
    print('Message: ', message)

@coroutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            # конструкция принимает в х через yield и отдает average через yield
            x = yield average
        except StopIteration:
            print('Done')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
    # вернуть average можно с помощью try: g.throw(StopIteration) except StopIteration as e: print(e.value)    
    return average
