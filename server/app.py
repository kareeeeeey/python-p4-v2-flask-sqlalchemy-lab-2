from flask import Flask
from flask_migrate import Migrate

from models import db  # no dot here since we’re in server/ when running
# alternatively: from .models import db — only if you run from project root

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "<h1>Flask-SQLAlchemy Lab 2 Running</h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)

