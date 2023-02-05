from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker

from models import Base, User, Product, Purchase

DB_USER = "gorankov"
DB_PASSWORD = "Olimpiec2012!"
DB_NAME = "gorankov"
DB_ECHO = True

def add_product(name, price, quantity, comment):
    new_product = Product(name=name, price=price, quantity=quantity, comment=comment)
    session.add(new_product)
    session.commit()


def read_products():
    select_all = session.query(Product).select_from(Product).all()
    for user_data in select_all:
        print(user_data.id, user_data.name, user_data.quantity, user_data.price, user_data.comment)


def update_product(id_prod, name, price, quantity, comment):
    session.query(Product).filter_by(id=id_prod).update({"name": f"{name}", "price": f"{price}",
                                                         "quantity": f"{quantity}", "comment": f"{comment}"})
    session.commit()


def delete_product(id_prod):
    session.query(Product).filter_by(id=id_prod).delete()
    session.commit()


def add_purchase(user_id, prod_id):
    purchase = Purchase(user_id=user_id, product_id=prod_id)
    session.add(purchase)
    session.commit()


def select_purchase(user_id):
    selection = session.query(Purchase).filter_by(user_id=user_id).all()
    for user_data in selection:
        print(user_data.id, user_data.user_id, user_data.product_id)


def select_action(n):
    if n == 1:
        name = input('Введите название продукта: ')
        price = float(input('Введите цену продукта: '))
        quantity = int(input('Введите количество продукта'))
        comment = input('Введите комментарий')
        add_product(name, price, quantity, comment)
    elif n == 2:
        read_products()
    elif n == 3:
        id_prod = int(input('Введите id продукта: '))
        name = input('Введите название продукта: ')
        price = float(input('Введите цену продукта: '))
        quantity = int(input('Введите количество продукта'))
        comment = input('Введите комментарий')
        update_product(id_prod, name, price, quantity, comment)
    elif n == 4:
        id_prod = int(input('Введите id продукта: '))
        delete_product(id_prod)
    elif n == 5:
        id_user = int(input('Введите id пользователя: '))
        id_prod = int(input('Введите id продукта: '))
        add_purchase(id_user, id_prod)
    elif n == 6:
        id_user = int(input('Введите id пользователя: '))
        select_purchase(id_user)




if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("""
1 - Добавить продукт
2 - Отобразить все продукты
3 - Обновить продукт
4 - Удалить продукт
5 - Добавить покупку
6 - Отобразить покупки пользователя
    """)

    num = int(input('Введите номер действия: '))
    select_action(num)