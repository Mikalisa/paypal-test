
from flask import Flask, flash, redirect, render_template, request, session, url_for, g, jsonify, Blueprint, current_app
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from werkzeug.datastructures import ImmutableOrderedMultiDict
import os
import requests
from datetime import datetime, timedelta

from app.extensions import db

from app.models import Payment

from time import ctime

from app.email import send_email


main = Blueprint('main', __name__)




@main.route('/')
def purchase():
	try:
		return render_template("subscribe.html")
	except Exception as e:
		return(str(e))



@main.route('/success/')
def success():
	try:
		return render_template("success.html")
	except Exception as e:
		return(str(e))




@main.route('/ipn', methods=['GET','POST'])
def ipn():

    arg = ''
    request.parameter_storage_class = ImmutableOrderedMultiDict
    values = request.form


    for x, y in values.items():
        arg += "&{x}={y}".format(x=x,y=y)


    validate_url = 'https://www.sandbox.paypal.com' \
					   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
					   .format(arg=arg)

    r = requests.get(validate_url)

    if r.text == 'VERIFIED':

        payer_email =  request.form.get('payer_email')
        unix = ctime()
        payment_date = request.form.get('payment_date')
        username = request.form.get('first_name')
        last_name = request.form.get('last_name')
        payment_gross = request.form.get('mc_gross')
        payment_fee = request.form.get('mc_fee')
        payment_net = float(payment_gross) - float(payment_fee)
        payment_status = request.form.get('payment_status')
        txn_id = request.form.get('txn_id')
        

        payment = Payment(payer_email=payer_email, unix=unix, payment_date=payment_date, username=username, last_name=last_name, payment_gross=payment_gross, payment_fee=payment_fee, payment_net=payment_net, payment_status=payment_status, txn_id=txn_id)
        db.session.add(payment)
        db.session.commit()


        
        
        
        send_email("Payment from the website", 'support@divaexplorer-tvj.co.uk', ['mekalissa68@gmail.com', 'divaexplorer58@gmail.com'],

         """Payment recieved form customer. 
        name: %s
        email: <%s>
        payment_status: %s
        Price paid: %s
        """ % (username, payer_email, payment_status, payment_gross)
        
        )
    

        with open('/tmp/ipnout.txt','a') as f:
            data = 'SUCCESS\n'+str(values)+'\n'
            f.write(data)

        

        

    else:
        with open('/tmp/ipnout.txt','a') as f:
            data = 'FAILURE\n'+str(values)+'\n'
            f.write(data)

    return r.text