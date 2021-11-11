from flask import render_template
from forms import *

def addRoutes(app, db, dbc):
    # Render index
    @app.route("/")
    @app.route('/<name>')
    def index(name=None):
        return render_template('index.jinja', name=name)

    # Database test
    @app.route("/database")
    def database():
        return render_template('database.jinja', data=dbc.User.query.all())
    
    # Forms example
    @app.route("/register", methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = dbc.User(username=form.username.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        return render_template('register.jinja', form=form)