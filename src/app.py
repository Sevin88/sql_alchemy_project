from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///School.db', echo=True)
engine.connect()

Base = declarative_base()

class User(Base):

    tablename = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    filed = Column(String)
    gpa = Column(Float)

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
sessionlocal = session()


user1 = User(name = 'Nima', filed='Computer', gpa = 17.36 )
user2 = User(name = 'Asghar', filed='IT', gpa = 16.32 )
# sessionlocal.add(user1)
# sessionlocal.add(user2)
sessionlocal.add_all([user1, user2])
sessionlocal.commit()
###################################################