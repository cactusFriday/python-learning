#!/usr/bin/python3
# http contains tcp and ip
# ip: IP-adress. Между двумя машинами создается тоннель.
# tcp(transmission control protocol): port. Дополнительная защита к IP: повторные запросы на получение пакетов, удаление дублей. 
# Порты нужны для того, чтобы несколько приложений могли использовать tcp на одной машине не занимая собой весь тоннель.
# Аналогия: адрес улица/дом, порт квартира.
# IP-adress:port == socket (гнездо)
# Сокеты бывают серверные и клиентские


import socket
from views import index, print_page

URLS = {
    '/': index,
    '/print': print_page
}

def parse_request(request)->tuple:
    '''
    parses request and return (method, url)
    '''
    parsed = request.split()
    method = parsed[0]
    url = parsed[1]
    return (method, url)

def generate_headers(method, url)-> tuple:
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)
    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)
    return ('HTTP/1.1 200 OK\n\n', 200)

def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>NOT FOUND</p>'
    if code == 405:
        return '<h1>405</h1><p>METHOD NOT ALLOWED</p>'
    return URLS[url]()


def generate_response(request):
    '''
    Generates response for client socket.
    Parses request (get HTTP method and url)
    '''
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)

    body = generate_content(code, url)

    return (headers + body).encode()

def main():
    # Создаем сокет AF=address family (inet == ipv4), tcp = SOCK_STREAM
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # настройка сокета на переиспользование. Таймаут на полторы минуты нужен для того, чтобы завершить передачу данных, даже если сокет отключен.
    # SOL - socket level SOCKET - именно наш сокет; REUSEADDR - опция на переиспользование адреса, 1 - включить опцию
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    # связываем сервер с определенным адресом и портом
    server_socket.bind(('localhost', 5000))
    # ставим сервер на прослушивание
    server_socket.listen()
    # Бесконечный цикл для постоянной обработки запросов
    while True:
        # возвращает кортеж (сокет, адрес)
        client_socket, addr = server_socket.accept()
        # получение запроса пользователя пакетами по 1024 байта
        request = client_socket.recv(1024)
        print(request)
        print()
        print(addr)
        
        response = generate_response(request.decode('UTF-8'))

        # Отправляем клиенту ответ, кодируя строку в байты
        client_socket.sendall(response)
        # закрываем соединение с клиентом
        client_socket.close()


if __name__ == '__main__':
    main()