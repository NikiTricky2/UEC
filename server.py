from flask import Flask
from flask import render_template

# Create the application object
app = Flask(__name__, static_url_path='/static')

# Render index
@app.route("/")
@app.route('/<name>')
def index(name=None):
    return render_template('index.jinja', name=name)

# Start the server with the 'run()' method
if __name__ == "__main__":
    app.run()