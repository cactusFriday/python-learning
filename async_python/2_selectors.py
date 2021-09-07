import socket
import selectors

'''
Асинхронность на колбеках.
1.  Мы создаем сокет и ставим его на прослушивание
    Регистрируем в селекторе серверный сокет и передаем ассоциированную с ним функцию(объект функции). У сервера: accept_connection.

2.  В функции accept_connection мы регестрируем клиентский сокет и передаем в регистратор объект функции send_msg.

3.  В событийном цикле бесконечно проверяем файл на изменение (ранее EVENT_READ)
    Возвращаем с помощью select() кортеж, содержащий (key: SelectorKey, events)
    SelectorKey: NamedTuple, у которого есть поля fileobj, events, data
    В поле data лежит ассоциированная функция к сокету fileobj
    
4.  Вызываем функцию, полученную из зарегестрированного сокета

Selectors выполняет тот же мониторинг что и функция select()
'''

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # Регистрируем на чтение сервер сокет и связываем с ним функцию accept_connection()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    # .accept() блокирующая операция
    client_socket, client_addr = server_socket.accept()
    print(client_addr)

    # Регистрируем клиентский сокет на чтение и связываем с ним функцию send_msg()
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_msg)

def send_msg(client_socket):
    # Блокирующая операция
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        # удаляем из регистрации сокет
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        
        events = selector.select()      #(key, events) -> возвращает по одному кортежу на каждый зарегестрированный объект
        # key - SelectorKey: NamedTuple
        # поля : fileobj, events, data
        for key, _ in events:
            callback = key.data
            print("fileobj:\t", key.fileobj)
            print("events:\t\t", key.events)
            print("data:\t\t", key.data)
            print()
            callback(key.fileobj)

if __name__ == '__main__':
    server()
    event_loop()
    