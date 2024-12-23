import time
import redis
from flask import Flask, request
import mysql.connector
from mysql.connector import Error

# Настройка MySQL
db_config = {
    'host': 'localhost',
    'database': 'myDBName',
    'user': 'root',
    'password': 'root'
}

# Подключение к Redis
app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379)


# Получения значения счетчика из Redis
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


# Запись информации в MySQL
def log_request_to_db(datetime, client_info):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO table_Counter (datetime, client_info) 
        VALUES (%s, %s)
        """

        record = (datetime, client_info)

        cursor.execute(insert_query, record)
        connection.commit()

        print("Запись успешно добавлена в таблицу")

    except Error as e:
        print(f"Ошибка при работе с MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL соединение закрыто")


# Главная страница
@app.route('/')
def hello():
    count = get_hit_count()  # Получаем текущее значение счетчика из Redis

    # Логируем запрос в базу данных MySQL
    from datetime import datetime
    current_time = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    user_agent = request.headers.get('User-Agent')
    log_request_to_db(current_time, user_agent)

    return f'Hello World! I have been seen {count} times.\n'


if __name__ == '__main__':
    app.run(debug=True)
