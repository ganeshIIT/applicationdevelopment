import os
from flask import Flask
from flask_restful import Resource, Api
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from application.models import User, Role
from flask_login import LoginManager
from flask_security import utils

# import logging
# logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      app.logger.info("Currently no production config is setup.")
      raise Exception("Currently no production config is setup.")
    else:
      app.logger.info("Staring Local Development.")
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    app.logger.info("App setup complete")
    # Setup Flask-Security
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    # user_datastore.create_user(username="thejeshgn",email='i@thejeshgn.com', password=utils.hash_password('password'), active=1)
    # db.session.commit()    
    api = Api(app)
    app.app_context().push()      
    return app, api

app,api = create_app()

# Import all the controllers so they are loaded
from application.controllers import *

# Add all restful controllers
from application.api import ArticleLikesAPI
api.add_resource(ArticleLikesAPI, "/api/article_likes", "/api/article_likes/<int:article_id>")


from application.api import TestAPI
api.add_resource(TestAPI, "/api/test")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(403)
def not_authorized(e):
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8080)
