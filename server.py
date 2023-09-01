#! /usr/bin/python3

from flask import Flask, render_template, request
from models import Sender
from models import Recipient
from models import ShippingPackage
from connection import session

app = Flask(__name__)

@app.route('/')
def home():
    return "My API"

@app.route('/add_sender', methods=['GET', 'POST'])   
def add_sender():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        street_address = request.form['street_address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        country = request.form['country']

        sender = Sender(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, street_address=street_address, city=city, state=state, zipcode=zip_code, country=country)  
        session.add(sender)
        session.commit()

    
    senders = session.query(Sender).all()

    return render_template('customer.html', senders=senders)

@app.route('/add_recipient', methods=['GET', 'POST'])
def add_recipient():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        street_address = request.form['street_address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        country = request.form['country']

        recipient = Recipient(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, street_address=street_address, city=city, state=state, zipcode=zip_code, country=country)  
        session.add(recipient)
        session.commit()

    
    recipients = session.query(Recipient).all()

    return render_template('recipient.html', recipients=recipients)

@app.route('/add_package', methods=['GET', 'POST'])
def add_package():
    if request.method == 'POST':
        sender_id = request.form['sender_id']
        recipient_id = request.form['recipient_id']
        weight = request.form['weight']
        height = request.form['height']
        width = request.form['width']
        length = request.form['length']
        shipping_carrier = request.form['shipping_carrier']
        shipping_class = request.form['shipping_class']
        shipping_date = request.form['shipping_date']
        delivery_date = request.form['delivery_date']
        tracking_number = request.form['tracking_number']
        shipping_cost = request.form['shipping_cost']


        shipping_package = ShippingPackage(sender_id=sender_id, recipient_id=recipient_id, weight=weight, height=height, width=width , length=length , shipping_carrier=shipping_carrier, shipping_class=shipping_class, shipping_date=shipping_date, delivery_date=delivery_date, tracking_number=tracking_number, shipping_cost=shipping_cost)  
        session.add(shipping_package)
        session.commit()

    
    shipping_packages = session.query(ShippingPackage).all()
    senders = session.query(Sender).all()
    recipients = session.query(Recipient).all()

    return render_template('shipping_package.html', shipping_packages=shipping_packages, senders=senders, recipients=recipients)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5050")