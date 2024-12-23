# Отчет

## Шаги:

### 1. Создал БД в MySQL
CREATE DATABASE IF NOT EXISTS myDBName;

USE myDBName;

CREATE TABLE IF NOT EXISTS table_Counter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datetime VARCHAR(255) NOT NULL,
    client_info VARCHAR(255) NOT NULL
);

В идеале конечно использовать в datetime DATETIME тип, но мне было немного лень ковыряться с datetime в python, поэтому я сделал строчкой

### 2. Поставил на Windows Redis через Docker
docker run -d -p 6379:6379 redis
устанавливает и запускает Redis

![Изображение](https://sun9-76.userapi.com/impg/L3tXrKQ-LayqiY6yDZCmXH8Io8CgcsBqp2u0oA/LmtG3wDoPH4.jpg?size=1026x654&quality=95&sign=e530499f1b99f34fdfa6bf6ab49721ab&type=album)

### 3. app.py
добавил взаимодействие с БД - конфигурация и запись данных в таблицу

### 4. requirements.txt
Добавлена mysql-connector-python

### 5. docker-compose.yml
- web: контейнер для веб-приложения
- db: контейнер для MySQL
- redis: контейнер для кеша Redis.


После всего команда создаст и запустит все необходимое
### docker-compose up -d


Записи в БД
![Изображение](https://sun9-60.userapi.com/impg/gLtPWiOvmtRsnHleXFMZdmlzTIiThWiyzWDFQQ/2KHvnB9o2L4.jpg?size=985x297&quality=95&sign=8cbdbf204a8eed68e68f6788cab1b105&type=album)

Изначально из-за DATETIME выбивало ошибку, я поменял на VARCHAR и ошибки перестало сыпать. Поэтому записей в бд меньше, чем выдает Redis

![Изображение](https://sun9-29.userapi.com/impg/eRSmxg6Ljr5SC2eMxlx2ltgXXtYU8OUPZJCpmA/EGRKlcS_-6M.jpg?size=385x112&quality=95&sign=50bb7d337d8fc4998cdb2267dfc6385d&type=album)
