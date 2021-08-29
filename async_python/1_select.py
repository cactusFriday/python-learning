import socket
from select import select

'''
Каждый запущенный процесс в UNIX - тоже файл. При вызове .bind() создается файл сокета.
Select необходима для отслеживания изменений в любых объектах, у которых есть метод: 
.fileno() - номер файла, возвращает файловый дескриптор (номер файла, как бы адрес, выделенный ОС). То есть в любых файлах.
Select мониторит номер файловых объектов, который мы в нее передали
Принимает на вход 3 списка: 
1 - те объекты, за которыми нужно следить, когда они станут доступны для чтения.
2 - ,когда они станут доступны для записи
3 - ,у которых мы ожидаем ошибки
Возвращает те же объекты, НО ПОСЛЕ ТОГО, как они станут доступны
1. Необходимо уменьшить связность всех функций (спроектирвать так, чтобы одна от другой не зависила)

'''

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

def accept_connection(server_socket):
    ''' 
    принимает серверный сокет, и принимает новое подключение, печатает адрес,
    аппендит в список для мониторинга изменений файлов сокетов клиентский сокет (принятое соединение) 
    '''
    # .accept() блокирующая операция - пока не примет соединение, управление не передается дальше по циклу
    client_socket, client_addr = server_socket.accept()
    print(client_addr)
    to_monitor.append(client_socket)

def send_msg(client_socket):
    ''' 
    Принимает клиентский сокет, пытается получить запрос от клиента (4кБ).
    Если запрос от клиента получет, отвечает клиенту, иначе - закрывает сокет.
    '''
    # Блокирующая операция
    request = client_socket.recv(4096)
    if request:
        # Если буфер отправки полный, то .send() так же блокирующая операция
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        # распаковываем кортеж трех списков, возвращаемых селектом
        # как только пользователь начнет писать в сокет, select() сделает выборку из to_monitor и вернет новый список ready_to_read
        ready_to_read, _, _ = select(to_monitor, [], [])    
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_msg(sock)

if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
    # accept_connection(server_socket)
    