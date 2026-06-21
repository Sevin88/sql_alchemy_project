# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# engine = create_engine('sqlite:///market.db')
# engine.connect()

# Base = declarative_base()

# class Customer(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     address = Column(String)
#     balance = Column(Float)

#     customer_obj = relationship('Order', back_populates='orders_obj')

# class Order(Base):

#     __tablename__ = 'orders'

#     id = Column(Integer, primary_key=True)
#     product_name = Column(Integer)
#     price = Column(Float)

#     customer_id = Column(Integer, ForeignKey('customers.id'))

#     orders_obj = relationship('Customer', back_populates='customer_obj')

# Base.metadata.create_all(bind = engine)

# ---------------------------------------

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engin = create_engine('sqlite:///market.db')
engin.connect()

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    balance = Column(Float)
    
    customers_obj = relationship('Order', back_populates='orders_obj')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=True)
    quantity = Column(Integer)
    price = Column(Float)

    customer_id = Column(Integer, ForeignKey('customers.id'))


    orders_obj = relationship('Customer', back_populates='customers_obj')


Base.metadata.create_all(engin)


Session = sessionmaker(bind=engin)
sessionloacl = Session()

customer1 = Customer(name = 'Alireza Amini', address ='Ahvaz', balance = 1450.0)
customer2 = Customer(name = 'Paniz Haji', address ='Ahvaz', balance = 1740.63)

sessionloacl.add_all([customer1, customer2])
sessionloacl.commit()

order1= Order(product_name = 'Laptop', quantity = 2, price=500.0, customer_id =1)
sessionloacl.add(order1)
sessionloacl.commit()

obj = sessionloacl.query(Customer).filter_by(id=1).first()
print(obj.name)
print(obj.address)
print(obj.balance)
print('*'*30)
print(obj.customers_obj)
print(obj.customers_obj[0].product_name)
print(obj.customers_obj[0].quantity)
print(obj.customers_obj[0].price)

# customer_order = customer_obj.orders_obj