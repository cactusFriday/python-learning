# from inspect import getgeneratorstate as gstate
'''
Делегирующий генератор - тот, который вызывает другой генератор.
Подгенератор - вызываемый.

yield from заменяет представленный ниже бесконечный цикл, передает значения, пробрасывает исключения, 
позволяет вернуть через return у подгенератора значение (к примеру для последующей обработки)
yield from в других языках - await
'''


class MockException(Exception):
    pass

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

# def subgen():
#     for i in 'generator':
#         yield i

# def delegator(g):
#     for i in g:
#         yield i

# @coroutine - не нужен, так как конструкция yield from инициализирует генератор
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('[StopIteration Exception]')
            break
        else:
            print('....', message)
    return 'Returned from subgen()'

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except MockException as e:
    #         g.throw(e)
    result = yield from g
    print(result)