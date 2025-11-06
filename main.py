# app.py
from flask import Flask

app = Flask(__name__)

# Маршрут 1: Главная страница
@app.route('/')
def home():
    return 'Добро пожаловать на главную страницу!'

# Маршрут 2: Приветствие
@app.route('/hello')
def hello():
    return 'Привет! Это маршрут /hello.'

# Маршрут 3: Информация о сервере
@app.route('/about')
def about():
    return 'Это простое Flask-приложение с несколькими маршрутами.'

# Маршрут 4: Тестовый маршрут с параметром
@app.route('/user/<name>')
def user(name):
    return f'Привет, {name}! Ты на маршруте /user/<name>.'

# Маршрут 5: Статус
@app.route('/status')
def status():
    return 'Сервер работает нормально. Статус: OK.'

if __name__ == '__main__':
    app.run(debug=True)# app.py
from flask import Flask

app = Flask(__name__)

# Маршрут 1: Главная страница
@app.route('/')
def home():
    return 'Добро пожаловать на главную страницу!'

# Маршрут 2: Приветствие
@app.route('/hello')
def hello():
    return 'Привет! Это маршрут /hello.'

# Маршрут 3: Информация о сервере
@app.route('/about')
def about():
    return 'Это простое Flask-приложение с несколькими маршрутами.'

# Маршрут 4: Тестовый маршрут с параметром
@app.route('/user/<name>')
def user(name):
    return f'Привет, {name}! Ты на маршруте /user/<name>.'

# Маршрут 5: Статус
@app.route('/status')
def status():
    return 'Сервер работает нормально. Статус: OK.'

if __name__ == '__main__':
    app.run(debug=True)# app.py
from flask import Flask

app = Flask(__name__)

# Маршрут 1: Главная страница
@app.route('/')
def home():
    return 'Добро пожаловать на главную страницу!'

# Маршрут 2: Приветствие
@app.route('/hello')
def hello():
    return 'Привет! Это маршрут /hello.'

# Маршрут 3: Информация о сервере
@app.route('/about')
def about():
    return 'Это простое Flask-приложение с несколькими маршрутами.'

# Маршрут 4: Тестовый маршрут с параметром
@app.route('/user/<name>')
def user(name):
    return f'Привет, {name}! Ты на маршруте /user/<name>.'

# Маршрут 5: Статус
@app.route('/status')
def status():
    return 'Сервер работает нормально. Статус: OK.'

if __name__ == '__main__':
    app.run(debug=True)# app.py
from flask import Flask

app = Flask(__name__)

# Маршрут 1: Главная страница
@app.route('/')
def home():
    return 'Добро пожаловать на главную страницу!'

# Маршрут 2: Приветствие
@app.route('/hello')
def hello():
    return 'Привет! Это маршрут /hello.'

# Маршрут 3: Информация о сервере
@app.route('/about')
def about():
    return 'Это простое Flask-приложение с несколькими маршрутами.'

# Маршрут 4: Тестовый маршрут с параметром
@app.route('/user/<name>')
def user(name):
    return f'Привет, {name}! Ты на маршруте /user/<name>.'

# Маршрут 5: Статус
@app.route('/status')
def status():
    return 'Сервер работает нормально. Статус: OK.'

if __name__ == '__main__':
    app.run(debug=True)