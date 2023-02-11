import logging
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
import utils

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)

DB_USER = "gorankov"
DB_PASSWORD = "Olimpiec2012!"
DB_NAME = "les_13"


if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
    if not database_exists(engine.url):
        create_database(engine.url)

    session = utils.create_tables(engine)
#
    menu = """
1 - Создать пользователя
2 - Найти пользователя
3 - Редактировать адрес пользователя
4 - Добавить продукт
5 - Посмотреть все продукты
6 - Обновить продукт
7 - Удалить продукт
8 - Добавить покупку
9 - Поиск покупок польльзователя
10 - Фильтр покупок пользователей по цене
11 - Поиск пользователей по купленному товару
0 - Выйти
    """

    address_action = """
1 - Добавить адрес
2 - Обновить адрес
    """

    while True:
        loger.info(menu)
        choice = input('Выберите действие: ')
        if choice == '0':
            exit()
        elif choice == '1':
            email = input('Введите email: ')
            password = input('Введите пароль: ')
            age = int(input('Введите возраст: '))
            phone = input('Введите номер телефона: ')
            user = utils.create_user(session=session, email=email, password=password, phone=phone, age=age)
            loger.info(f'Пользователь {user.id} создан')
        elif choice == '2':
            email = input('Введите email пользователя: ')
            get_user = utils.find_user(session=session, email=email)
            if get_user is not None:
                loger.info(f'id: {get_user.id}, email: {get_user.email}, password: {get_user.password}, '
                           f'age: {get_user.profile.age}, phone: {get_user.profile.phone}')
            else:
                loger.info(f'Пользователя с email - {email} не существует.')
        elif choice == '3':
            city = input('Введите город: ')
            address = input('Введите адрес: ')
            email = input('Введите email пользователя: ')
            get_user = utils.find_user(session=session, email=email)
            if get_user is None:
                loger.info(f'Пользователя с email - {email} не существует.')
            elif len(get_user.addresses) == 0:
                utils.add_address(session=session, new_city=city, new_address=address, user_id=get_user.id)
                loger.info(f'Адрес для пользователя {email} добавлен.')
            else:
                loger.info(address_action)
                action = input('Выберите действие: ')
                if action == '1':
                    utils.add_address(session=session, new_city=city, new_address=address, user_id=get_user.id)
                    loger.info(f'Адрес для пользователя {email} добавлен.')
                elif action == '2':
                    if len(get_user.addresses) == 1:
                        utils.update_address(session=session, old_address=get_user.addresses[0].address,
                                             old_city=get_user.addresses[0].city, new_city=city, new_address=address,
                                             user_id=get_user.id)
                        loger.info(f'Адрес для пользователя {email} обновлен.')
                    else:
                        all_addresses = ''''''
                        for pos, addr in enumerate(get_user.addresses):
                            all_addresses += f'{pos} address: {addr.address}, city: {addr.city}\n'
                        loger.info(f'\n{all_addresses}')
                        choice_addr = int(input('Выберите адрес для обновления: '))
                        utils.update_address(session=session, old_address=get_user.addresses[choice_addr].address,
                                             old_city=get_user.addresses[choice_addr].city, new_city=city,
                                             new_address=address, user_id=get_user.id)
                        loger.info(f'Адрес для пользователя {email} обновлен.')
        elif choice == '4':
            name = input('Название продукта: ')
            price = input('Цена продутка: ')
            quantity = input('Количество продукта: ')
            comment = input('Комментарий: ')
            utils.add_product(session=session, name=name, price=price, quantity=quantity, comment=comment)
            loger.info('Новый продукт добавлен.')
        elif choice == '5':
            all_products = ''''''
            list_prods = utils.read_products(session=session)
            for el in list_prods:
                item = f'ID: {el.id}, Name: {el.name}, Quantity: {el.quantity}, Price: {el.price}, ' \
                       f'Comment: {el.comment}'
                all_products += f'{item}\n'
            loger.info(f'\n{all_products}')
        elif choice == '6':
            id_prod = int(input('ID продукта: '))
            name = input('Название продукта: ')
            price = input('Цена продутка: ')
            quantity = input('Количество продукта: ')
            comment = input('Комментарий: ')
            utils.update_product(session=session, id_prod=id_prod, name=name, price=price, quantity=quantity,
                                 comment=comment)
            loger.info(f'Продукт ID={id_prod} обновлен')
        elif choice == '7':
            id_prod = int(input('ID продукта: '))
            utils.delete_product(session=session, id_prod=id_prod)
            loger.info(f'Продукт ID={id_prod} удалён.')
        elif choice == '8':
            id_prod = int(input('ID продукта: '))
            id_user = int(input('ID пользователя: '))
            quantity = int(input('Количество: '))
            utils.add_purchase(session=session, user_id=id_user, prod_id=id_prod, quantity=quantity)
            loger.info('Покупка добавлена.')
        elif choice == '9':
            id_user = int(input('ID пользователя: '))
            utils.search_purchase_by_user(session=session, user_id=id_user)
            all_purchase = ''''''
            list_purchase = utils.search_purchase_by_user(session=session, user_id=id_user)
            for el in list_purchase:
                item = f'Name: {el.product.name}, Quantity: {el.quantity}'
                all_purchase += f'{item}\n'
            loger.info(f'\n{all_purchase}')
        elif choice == '10':
            price_more = int(input('Введите цену для фильтра: '))
            result = utils.search_users_by_purchase_price(session, price_more)
            for item in result:
                loger.info(f'User email: {item[0]}, Product name: {item[2]}, Price: {item[1]}')
        elif choice == '11':
            product_name = input('Введите название продукта: ')
            result = utils.search_users_by_purchase_product(session, product_name)
            for item in result:
                loger.info(f'User: {item[0]}')
