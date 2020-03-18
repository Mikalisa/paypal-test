from flask import Flask 

from .commands import create_tables
from .extensions import db
from .models import Payment

from .routes.main import main

from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

from flask_mail import Mail


mail = Mail()


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    
    db.init_app(app)

    mail.init_app(app)
    
    app.register_blueprint(main)
    
    
    app.cli.add_command(create_tables)

    


    admin = Admin(app)
    admin.add_view(ModelView(Payment, db.session))


    
    return app