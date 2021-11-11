from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from util import dbutil

# Create the application and add the database
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Get the database objects
dbc = dbutil.getDBclasses(db)

# Initialize the database and add dummy data, if none is found
import os.path
if not os.path.isfile("site.db"):
    db.create_all()
    db.session.add(dbc.User(username="admin", email="admin@mail.com"))
    db.session.add(dbc.User(username="user", email="user@mail.com"))
    db.session.commit()

# Add the routes
import routing
routing.addRoutes(app, db, dbc)


# Start the server with the 'run()' method
if __name__ == "__main__":
    app.run(debug=True)