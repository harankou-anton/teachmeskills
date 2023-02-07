import logging
from sqlalchemy import create_engine, and_
from sqlalchemy_utils import create_database, database_exists
from utils import create_tables

from models import User, Profile, Address, Product, Purchase

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)

DB_USER = "gorankov"
DB_PASSWORD = "Olimpiec2012!"
DB_NAME = "les_13"


def create_user(session, email, password, phone, age):
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    new_profile = Profile(phone=phone, age=age, user_id=new_user.id)
    session.add(new_profile)
    session.commit()
    return new_user


def find_user(session, email):
    query = session.query(User).filter_by(email=email).first()
    return query


def add_address(session, new_address, new_city, user_id):
    address = Address(city=new_city, address=new_address, user_id=user_id)
    session.add(address)
    session.commit()


def update_address(session, old_address, old_city, new_address, new_city, user_id):
    session.query(Address).filter(and_(Address.address == old_address, Address.city == old_city,
                                       Address.user_id == user_id)).update({'city': f'{new_city}',
                                                                            'address': f'{new_address}'})
    session.commit()


def add_product(session, name, price, quantity, comment):
    new_product = Product(name=name, price=price, quantity=quantity, comment=comment)
    session.add(new_product)
    session.commit()


def read_products(session):
    select_all = session.query(Product).select_from(Product).all()
    return select_all


def update_product(session, id_prod, name, price, quantity, comment):
    session.query(Product).filter_by(id=id_prod).update({"name": f"{name}", "price": f"{price}",
                                                         "quantity": f"{quantity}", "comment": f"{comment}"})
    session.commit()


def delete_product(session, id_prod):
    session.query(Product).filter_by(id=id_prod).delete()
    session.commit()


def add_purchase(session, user_id, prod_id, quantity):
    purchase = Purchase(user_id=user_id, product_id=prod_id, quantity=quantity)
    session.add(purchase)
    session.commit()


def search_purchase_by_user(session, user_id):
    query = session.query(Purchase).filter(Purchase.user_id == user_id).all()
    return query


if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
    if not database_exists(engine.url):
        create_database(engine.url)



    session = create_tables(engine)

    # query = session.query(User).filter_by(id=2).all()
    # print(query[0].addresses)


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
            user = create_user(session=session, email=email, password=password, phone=phone, age=age)
            loger.info(f'Пользователь {user.id} создан')
        elif choice == '2':
            email = input('Введите email пользователя: ')
            get_user = find_user(session=session, email=email)
            if get_user is not None:
                loger.info(f'id: {get_user.id}, email: {get_user.email}, password: {get_user.password}, '
                           f'age: {get_user.profile.age}, phone: {get_user.profile.phone}')
            else:
                loger.info(f'Пользователя с email - {email} не существует.')
        elif choice == '3':
            city = input('Введите город: ')
            address = input('Введите адрес: ')
            email = input('Введите email пользователя: ')
            get_user = find_user(session=session, email=email)
            if get_user is None:
                loger.info(f'Пользователя с email - {email} не существует.')
            elif len(get_user.addresses) == 0:
                add_address(session=session, new_city=city, new_address=address, user_id=get_user.id)
                loger.info(f'Адрес для пользователя {email} добавлен.')
            else:
                loger.info(address_action)
                action = input('Выберите действие: ')
                if action == '1':
                    add_address(session=session, new_city=city, new_address=address, user_id=get_user.id)
                    loger.info(f'Адрес для пользователя {email} добавлен.')
                elif action == '2':
                    if len(get_user.addresses) == 1:
                        update_address(session=session, old_address=get_user.addresses[0].address,
                                       old_city=get_user.addresses[0].city, new_city=city, new_address=address,
                                       user_id=get_user.id)
                        loger.info(f'Адрес для пользователя {email} обновлен.')
                    else:
                        all_addresses = ''''''
                        for pos, addr in enumerate(get_user.addresses):
                            all_addresses += f'{pos} address: {addr.address}, city: {addr.city}\n'
                        loger.info(f'\n{all_addresses}')
                        choice_addr = int(input('Выберите адрес для обновления: '))
                        update_address(session=session, old_address=get_user.addresses[choice_addr].address,
                                       old_city=get_user.addresses[choice_addr].city, new_city=city,
                                       new_address=address, user_id=get_user.id)
                        loger.info(f'Адрес для пользователя {email} обновлен.')
        elif choice == '4':
            name = input('Название продукта: ')
            price = input('Цена продутка: ')
            quantity = input('Количество продукта: ')
            comment = input('Комментарий: ')
            add_product(session=session, name=name, price=price, quantity=quantity, comment=comment)
            loger.info('Новый продукт добавлен.')
        elif choice == '5':
            all_products = ''''''
            list_prods = read_products(session=session)
            for el in list_prods:
                item = f'ID: {el.id}, Name: {el.name}, Quantity: {el.quantity}, Price: {el.price}, Comment: {el.comment}'
                all_products += f'{item}\n'
            loger.info(f'\n{all_products}')
        elif choice == '6':
            id_prod = int(input('ID продукта: '))
            name = input('Название продукта: ')
            price = input('Цена продутка: ')
            quantity = input('Количество продукта: ')
            comment = input('Комментарий: ')
            update_product(session=session, id_prod=id_prod, name=name, price=price, quantity=quantity, comment=comment)
            loger.info(f'Продукт ID={id_prod} обновлен')
        elif choice == '7':
            id_prod = int(input('ID продукта: '))
            delete_product(session=session, id_prod=id_prod)
            loger.info(f'Продукт ID={id_prod} удалён.')
        elif choice == '8':
            id_prod = int(input('ID продукта: '))
            id_user = int(input('ID пользователя: '))
            quantity = int(input('Количество: '))
            add_purchase(session=session, user_id=id_user, prod_id=id_prod, quantity=quantity)
            loger.info('Покупка добавлена.')
        elif choice == '9':
            id_user = int(input('ID пользователя: '))
            search_purchase_by_user(session=session, user_id=id_user)
            all_purchase = ''''''
            list_purchase  = search_purchase_by_user(session=session, user_id=id_user)
            for el in list_purchase:
                item = f'ID: {el.id}, Name: {el.name}, Quantity: {el.quantity}, Price: {el.price}, Comment: {el.comment}'
                all_purchase += f'{item}\n'
            loger.info(f'\n{all_purchase}')








