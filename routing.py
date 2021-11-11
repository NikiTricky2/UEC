from flask import render_template

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