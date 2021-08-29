import socket

'''
в момент соединения с одним клиентом, операции сервера замерзают во внутреннем цикле, где он ожидает сообщения от клиента
В этом случае, если происходит попытка подключения второго клиента, запрос на подключение просто добавляется в очередь
Задача асинхронного программирования состоит в том, чтобы в момент начала ожидания сообщений от клиента_1 передать управление в внешний цикл,
где происходит ожидание подключения клиента_2, к примеру.
Для этого нужен цикл событий eventLoop(), в котором посредством некоторого менеджера, будет распределяться передачи управления/контроля.
Асинхронный код можно писать без использования библиотек тремя способами:
1. с использованием callback
2. с помощью генераторов, корутин
3. с помощью синтаксиса async/await
'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))

server_socket.listen()

while True:
    print('Before accept')
    # .accept() блокирующая операция - пока не примет соединение, управление не передается дальше по циклу
    client_socket, client_addr = server_socket.accept()
    print(client_socket, client_addr)

    while True:
        # Блокирующая операция
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            # Если буфер отправки полный, то .send() так же блокирующая операция
            response = 'Hello world\n'.encode()
            client_socket.send(response)
        
    print('Exit of inner while')
    client_socket.close()
