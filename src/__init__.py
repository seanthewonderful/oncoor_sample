from flask import Flask

app = Flask(__name__)

# app.config.from_envvar('APP_SETTINGS')

# if app.config["ENV"] == "production":
#     app.config.from_object("config.ProductionConfig")
# else: 
#     app.config.from_object("config.DevelopmentConfig")
    
from src import models, views, forms

models.connect_to_db(app)


# if __name__ == "__main__":
#     models.connect_to_db(app)
#     app.run()