from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('settings.py')

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    return app
    
from src import models
models.connect_to_db(app)
from src import views, forms


# if __name__ == "__main__":
#     models.connect_to_db(app)
#     app.run()