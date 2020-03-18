from flask import Flask 

from .commands import create_tables
from .extensions import db
from .models import Payment

from .routes.main import main

from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView



def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    
    app.register_blueprint(main)
    
    
    app.cli.add_command(create_tables)
    
    with app.app_context():
        app.secret_key = 'development key'
        app.config['DEBUG'] = False
        app.config['TESTING'] = False
        app.config['MAIL_SERVER'] = 'smtp.zoho.eu'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USE_SSL'] = True
        #app.config['MAIL_DEBUG'] = False
        app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
        app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
        app.config['MAIL_DEFAULT_SENDER'] = ('From the website','support@divaexplorer-tvj.co.uk')
        app.config['MAIL_MAX_EMAILS'] = 5
        #app.config['MAIL_SUPPRESS_SEND'] = False
        app.config['MAIL_ASCII_ATTACHMENTS'] = False


    admin = Admin(app)
    admin.add_view(ModelView(Payment, db.session))


    
    return app