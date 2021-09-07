from time import time

'''
RoundRobin eventLoop

Генераторы - функция, отдающая какой-либо результат. Разница в том, что функцию можно поставить на паузу. (отложить выполнение)
1. При итерации генератора 1 раз, итерировавшись он возвращает контроль в то же место, где была проведена итерация. (next(g))
2. Контроль возвращается именно после yield, значит если существует код после yield, он будет выполнен при следующей итерации
3. Аналогичная ситуация, в случае нескольких yield в одной функции
'''
# def gen_filename():
#     while True:
#         pattern = 'file-{}.jpg'
#         t = int(time() * 1000)
#         yield pattern.format(str(t))
#         print(2 + 3)
# 
# g = gen_filename()

def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('string')
g2 = gen2(7)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
