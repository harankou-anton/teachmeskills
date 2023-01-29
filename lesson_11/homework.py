"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и вводить необходимые данные.
"""
import sqlite3

fields_names = {1: 'name', 2: 'price', 3: 'quantity', 4: 'comment'}


def add_product():
    print('Введите данные для внесения в таблицу')
    name = input('Название продукта: ')
    price = float(input('Цена: '))
    quantity = int(input('Количество: '))
    comment = input('Комментарий: ')
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
        INSERT INTO products (name, price, quantity, comment)
        VALUES (?, ?, ?, ?);
        """, (name, price, quantity, comment)
        )
        session.commit()


def read_data():
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute("""
        SELECT * FROM products;
        """)
        session.commit()
        print(*cursor.fetchall(), sep='\n')


def update_data():
    id_input = int(input('Введите id записи для обновления: '))
    field_to_update = int(input(
        '''Введите число указывающее на поле для обновления 
1 - Название продукта
2 - Цена
3 - Количество
4 - Комментарий
Значение: '''))
    value_to_update = input('Введите обновлённое значение: ')
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            f'''
            UPDATE products
            SET {fields_names[field_to_update]} = ?
            WHERE id = ?;
            ''', (value_to_update, id_input))
        session.commit()


def delete_data():
    id_input = int(input('Введите id записи для удаления: '))
    with sqlite3.connect("my_database_11.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''
            DELETE FROM products
            WHERE id = ?;
            ''', (id_input,))
        session.commit()


def choose_function():
    print('''
1 - Добавить запись
2 - Посмотреть все записи
3 - Обновить значение
4 - Удалить значение
    ''')
    n = input('Введите номер функции: ')
    if n == '1':
        add_product()
    elif n == '2':
        read_data()
    elif n == '3':
        update_data()
    elif n == '4':
        delete_data()
    else:
        print(f'Значения функции {n} не существует. Введите корректное значение')
        choose_function()


if __name__ == '__main__':
    choose_function()
