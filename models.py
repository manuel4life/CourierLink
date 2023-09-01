from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sender(Base):
    __tablename__ = 'sender'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))
    street_address = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(50))
    country = Column(String(50))

    def __init__(self, first_name, last_name, email, phone_number, street_address, city, state, zipcode, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.phone_number = phone_number
        self.street_address = street_address
        self.city = city   
        self.state = state
        self.zip_code = zipcode
        self.country = country


class Recipient(Base):
    __tablename__ = 'recipient'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(50))
    street_address = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(50))
    country = Column(String(50))

    def __init__(self, first_name, last_name, email, phone_number, street_address, city, state, zipcode, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.phone_number = phone_number
        self.street_address = street_address
        self.city = city   
        self.state = state
        self.zip_code = zipcode
        self.country = country

class ShippingPackage(Base):
    __tablename__ = 'shipping_package'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_id = Column(Integer, ForeignKey('sender.id'))
    recipient_id = Column(Integer, ForeignKey('recipient.id'))
    weight = Column(Integer)
    height = Column(Integer)
    width = Column(Integer)
    length = Column(Integer)
    shipping_carrier = Column(String(50))
    shipping_class = Column(String(50))
    shipping_date = Column(DateTime)
    delivery_date = Column(DateTime)
    tracking_number = Column(String(50))
    shipping_cost = Column(Integer)

    def __init__(self, sender_id, recipient_id, weight, height, width, length, shipping_carrier, shipping_class, shipping_date, delivery_date, tracking_number, shipping_cost):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.shipping_carrier = shipping_carrier
        self.shipping_class = shipping_class
        self.shipping_date = shipping_date
        self.delivery_date = delivery_date
        self.tracking_number = tracking_number
        self.shipping_cost = shipping_cost


class ShippingLabel(Base):
    __tablename__ = 'shipping_label'
    id = Column(Integer, primary_key=True, autoincrement=True)
    shipping_package_id = Column(Integer, ForeignKey('shipping_package.id'))
    label_url = Column(String(50))

    def __init__(self, shipping_package_id, label_url):
        self.shipping_package_id = shipping_package_id
        self.label_url = label_url

class ShippingPackageStatus(Base):
    __tablename__ = 'shipping_package_status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    shipping_package_id = Column(Integer, ForeignKey('shipping_package.id'))
    status = Column(String(50))
    status_date = Column(DateTime)

    def __init__(self, shipping_package_id, status, status_date):
        self.shipping_package_id = shipping_package_id
        self.status = status
        self.status_date = status_date
