from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker

from models import Base, User, Profile, Address

DB_USER = "gorankov"
DB_PASSWORD = "Olimpiec2012!"
DB_NAME = "gorankov"
DB_ECHO = True


def add_user(email, password, phone, age, city, address):
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    new_profile = Profile(age=age, phone=phone, user_id=new_user.id)
    new_address = Address(city=city, address=address, user_id=new_user.id)
    session.add(new_profile)
    session.add(new_address)
    session.commit()


def add_new_address(user_id, address, city):
    new_address = Address(user_id=user_id, address=address, city=city)
    session.add(new_address)
    session.commit()


def update_address(user_id, address, city):
    session.query(Address).filter_by(user_id=user_id).update({"city": f"{city}"})
    session.query(Address).filter_by(user_id=user_id).update({"address": f"{address}"})
    session.commit()


def search_by_age(age):
    search_query = session.query(Profile).filter_by(age=age)
    for row in search_query:
        print(row.id, row.age)


if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,)
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # add_user(email='gorankov@nca.by', password='qwerty', phone='+375299262829', age=25, city='Mstislavl',
    #          address='Mira, 12')
    # add_user(email='new_user@gmail.com', password='1234554321', phone='+375291111111', age=20, city='Orsha',
    #          address='Lenina, 1')

    # add_new_address(user_id=1, address='Gorkogo, 4', city='Mogilev')
    # update_address(user_id=4, address='Tolstogo 23', city='Gomel')
    # search_by_age(20)
    query = session.query(User).select_from(User).all()
    print(query)