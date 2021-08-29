def index():
    try:
        with open('templates/index.html') as template:
            return template.read()
    except FileNotFoundError:
        print('[ERROR]: FileNotFound')

def print_page():
    with open('templates/print.html') as template:
        return template.read()