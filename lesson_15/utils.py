from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from models import Base
from models import User, Profile, Address, Product, Purchase


def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def create_user(session, email: str, password: str, phone: str, age: int) -> User:
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    new_profile = Profile(phone=phone, age=age, user_id=new_user.id)
    session.add(new_profile)
    session.commit()
    return new_user


def find_user(session, ids: int):
    query = session.query(User).filter_by(id=ids).first()
    return query.id, query.email


def add_address(session, new_address: str, new_city: str, user_id: int):
    address = Address(city=new_city, address=new_address, user_id=user_id)
    session.add(address)
    session.commit()


def update_address(session, old_address: str, old_city: str, new_address: str, new_city: str, user_id: int):
    session.query(Address).filter(and_(Address.address == old_address, Address.city == old_city,
                                       Address.user_id == user_id)).update({'city': f'{new_city}',
                                                                            'address': f'{new_address}'})
    session.commit()


def add_product(session, name: str, price: float, quantity: int, comment: str):
    new_product = Product(name=name, price=price, quantity=quantity, comment=comment)
    session.add(new_product)
    session.commit()


def read_products(session) -> list:
    select_all = session.query(Product).select_from(Product).all()
    return select_all


def update_product(session, id_prod: int, name: str, price: float, quantity: int, comment: str):
    session.query(Product).filter_by(id=id_prod).update({"name": f"{name}", "price": f"{price}",
                                                         "quantity": f"{quantity}", "comment": f"{comment}"})
    session.commit()


def delete_product(session, id_prod: int):
    session.query(Product).filter_by(id=id_prod).delete()
    session.commit()


def add_purchase(session, user_id: int, prod_id: int, quantity: int):
    purchase = Purchase(user_id=user_id, product_id=prod_id, quantity=quantity)
    session.add(purchase)
    session.commit()


def search_purchase_by_user(session, user_id: int) -> list:
    query = session.query(Purchase).filter(Purchase.user_id == user_id).all()
    return query


def search_users_by_purchase_price(session, price:float) -> list:
    query = session.query(User.email, Product.price * Purchase.quantity, Product.name).select_from(User) \
        .join(Purchase).join(Product).where((Product.price * Purchase.quantity) > price).all()
    return query


def search_users_by_purchase_product(session, product_name: str) -> list:
    query = session.query(User.email).distinct(User.email)\
        .join(Purchase).join(Product).filter(Product.name == product_name).all()
    return query
