from models import Dog
from sqlalchemy import (Column, String, Integer)

def create_table(base, engine):
    base.metadata.create_all(engine)
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    dogs = session.query(Dog).filter_by(name=name).first()
    return dogs

def find_by_id(session, id):
    dogs = session.query(Dog).filter_by(id=id).first()
    return dogs

def find_by_name_and_breed(session, name, breed):
    dogs = session.query(Dog).filter_by(name=name, breed=breed).first()
    return dogs

def update_breed(session, dog, breed):
    dogs = session.query(Dog).filter_by(id=dog.id).update({'breed': breed})
    return dogs

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///:memory:')
#     Base.metadata.create_all(engine)

#     # use our engine to configure a 'Session' class
#     Session = sessionmaker(bind=engine)
#     # use 'Session' class to create 'session' object
#     session = Session()