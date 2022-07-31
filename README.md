# final_homework

1. Получать данные с документа при помощи Google API, сделанного в Google Sheets (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Обновите данные так, чтобы большинство дат было в будущем.
3. Данные должны добавляться в БД, в том же виде, что и в файле–источнике, с добавлением колонки «стоимость в грн.». Стоимость в гривнах должна обновляться каждый раз.
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    b. Данные для перевода $ в гривны необходимо получать по курсу НБУ.
4. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).
5. Также необходимо разработать функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
6. Разработка одностраничного web-приложения на основе Django. Простая html таблица + js скрипт, который раз в минуту тащит новые данные с сервера.

