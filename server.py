#! /usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from models import Sender
from models import Recipient
from models import ShippingPackage
from models import ShippingPackageStatus
from connection import session

app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    senders_count = len(session.query(Sender).order_by(Sender.id.desc()).all())
    recipients_count = len(session.query(Recipient).order_by(Recipient.id.desc()).all())
    shipping_packages_count = len(session.query(ShippingPackage).order_by(ShippingPackage.id.desc()).all())
    print(senders_count)
    print(recipients_count)
    # print(shipping_packages_count)
    return render_template('dashboard.html', senders_count=senders_count , recipients_count=recipients_count, shipping_packages_count=shipping_packages_count)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_sender', methods=['GET', 'POST'], strict_slashes=True)   
def add_sender(): 
    senders = session.query(Sender).order_by(Sender.id.desc()).all()
    return render_template('customer.html', senders=senders)

@app.route('/add_recipient', methods=['GET', 'POST'], strict_slashes=True)
def add_recipient():
    recipients = session.query(Recipient).order_by(Recipient.id.desc()).all()
    return render_template('recipient.html', recipients=recipients)

@app.route('/add_package', methods=['GET', 'POST'], strict_slashes=True)
def add_package():
    shipping_packages = session.query(ShippingPackage).join(Sender).order_by(ShippingPackage.id.desc()).all()
    for shipping_package in shipping_packages:
        print(shipping_package)
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
            session.close()

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
                session.close()
    
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
            session.close()
            
            return redirect(url_for('add_package')) 

        senders = session.query(Sender).order_by(Sender.id.desc()).all()
        recipients = session.query(Recipient).order_by(Recipient.id.desc()).all()        
        return render_template('add_shipping_package.html', senders=senders, recipients=recipients)



@app.route('/view_package/<int:id>', methods=['GET', 'POST'])
def view_package(id):
    shipping_package = session.query(ShippingPackage).filter(ShippingPackage.id == id).first()
    shipping_package_status = session.query(ShippingPackageStatus).filter(ShippingPackageStatus.shipping_package_id == id).all()
    return render_template('view_package.html', package=shipping_package, shipping_package_status=shipping_package_status, id=id)

@app.route('/edit_package/<int:id>', methods=['GET', 'POST'])
def edit_package(id):
    shipping_package = session.query(ShippingPackage).filter(ShippingPackage.id == id).first()
    senders = session.query(Sender).order_by(Sender.id.desc()).all()
    recipients = session.query(Recipient).order_by(Recipient.id.desc()).all()
    return render_template('edit_package.html', shipping_package=shipping_package, senders=senders, recipients=recipients)


@app.route('/delete_package/<int:id>', methods=['GET', 'POST'])
def delete_package(id):
    shipping_package = session.query(ShippingPackage).filter(ShippingPackage.id == id).first()
    session.delete(shipping_package)
    session.commit()
    return redirect(url_for('add_package'))



@app.route('/update_status/<int:id>', methods=['GET', 'POST'])
def update_status(id):
    if request.method == 'POST':
        shipping_package = ShippingPackageStatus(id,request.form['shipping_status'],request.form['shipping_date'])
        session.add(shipping_package)
        session.commit()
        # session.close()
        return redirect(url_for('view_package', id= id))

    return render_template('update_status.html', id=id)



@app.route('/tracking', methods=['GET', 'POST'])
def tracking():
    if request.method == 'POST':
        tracking_number = request.form['tracking_number']
        shipping_package = session.query(ShippingPackage).filter(ShippingPackage.tracking_number == tracking_number).first()
        shipping_package_status = None
        if shipping_package is not None:
            shipping_package_status = session.query(ShippingPackageStatus).filter(ShippingPackageStatus.shipping_package_id == shipping_package.id).all()
        return render_template('tracking.html', package=shipping_package, shipping_package_status=shipping_package_status, tracking_number=tracking_number)
    return render_template('tracking.html', package=None, shipping_package_status=None, tracking_number=None)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/services')
def services():
    return render_template('services.html')

    














if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5050")