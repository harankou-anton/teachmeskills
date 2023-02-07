from sqlalchemy.orm import sessionmaker
from models import Base


def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()