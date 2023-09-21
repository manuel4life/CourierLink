#! /usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from models import Sender
from models import Recipient
from models import ShippingPackage
from connection import session

app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/')
def home():
    return "My API"

@app.route('/add_sender', methods=['GET', 'POST'], strict_slashes=True)   
def add_sender(): 
    senders = session.query(Sender).order_by(Sender.id.desc()).all()
    return render_template('customer.html', senders=senders)

@app.route('/add_recipient', methods=['GET', 'POST'], strict_slashes=True)
def add_recipient():
    recipients = session.query(Recipient).order_by(Recipient.id.desc()).all()
    return render_template('recipient.html', recipients=recipients)

@app.route('/add_package', methods=['GET', 'POST'])
def add_package():
    shipping_packages = session.query(ShippingPackage).order_by(ShippingPackage.id.desc()).all()
    senders = session.query(Sender).order_by(Sender.id.desc()).all()
    recipients = session.query(Recipient).order_by(Recipient.id.desc()).all()

    return render_template('shipping_package.html', shipping_packages=shipping_packages, senders=senders, recipients=recipients)


@app.route('/create_sender_form', methods=['GET', 'POST'])
def customer():
     
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

            return redirect(url_for('add_sender'))
        
        return render_template('add_customer.html')

@app.route('/create_recipient_form', methods=['GET', 'POST'])
def recipient():
         
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
    
                return redirect(url_for('add_recipient'))
            
            return render_template('add_recipient.html')

@app.route('/create_package_form', methods=['GET', 'POST'])
def package():
             
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
        
            return redirect(url_for('add_package'))
                
            return render_template('add_shipping_package.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5050")