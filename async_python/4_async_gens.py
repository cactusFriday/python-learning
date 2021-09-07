import socket
from select import select
'''
David Beazley
2015 pyCon "Concurrency from the Ground up Live"
'''

'''
Алгоритм
        yield ('read', client_socket)
        request = client_socket.recv(4096)
1.  Данная конструкция перед выполнением блокирующей операции возвращает контроль в событийный цикл.
    В событийном цикле мы всегда проверяем есть ли доступный к чтению сокет.
2.  И когда сокет будет готов к чтению, т.е. можно выполнить socket.recv(), мы можем вернуть контроль, вызвав у этого же генератора next()
3.  В свою очередь:
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)
    Функция продолжит выполнение после чтения, сформирует ответ, и опять вернет контроль перед блокирующей функцией отправки.
    Потому что сокет, куда нужно отправить ответ может быть отключен, буфер может быть заполнен и т.д. (невозможность отправить в сокет)
4.  И только когда он будет готов, он появится в выборке функции select(), как для записи, тогда мы опять вызываем next()
    Тогда он опять дойдет до первой конструкции и вернет сокет.
'''

# можно использовать deque из collections
tasks = []

# Словарь {сокет доступный для чтения: генератор}
to_read = {}
# Словарь {сокет доступный для записи: генератор}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield ('read', server_socket)
        # передаем контроль управления обратно в цикл, перед зависанием и ожиданием подключения клиентского сокета
        client_socket, client_addr = server_socket.accept()     # read
        print('[CONNECTION]: ', *client_addr)
        # После установления соединения, необходимо передать в список задач генератор клиентского сокета, который будет принимать и отправлять
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096)                      # read
        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)                        # write
    
    client_socket.close()

def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])    #select соберет ключи (итерация по словарю)

            for sock in ready_to_read:
                # извлекаем генератор, который лежит под ключем готового к чтению сокета и добавляем его в список заданий
                tasks.append(to_read.pop(sock))     # generator obj
            
            for sock in ready_to_write:
                # извлекаем готовый к записи генератор (value), который лежит под ключем (key) сокет и добавляем его в список заданий
                tasks.append(to_write.pop(sock))
        
        try:
            task = tasks.pop(0)         # pop -> generator
            token, sock = next(task)    # ('read/write', socket)

            if token == 'read':
                to_read[sock] = task
                print(to_read)
            if token == 'write':
                to_write[sock] = task
        except StopIteration:
            print('[Done!]')


if __name__ == "__main__":
    tasks.append(server())
    print(tasks)
    event_loop()