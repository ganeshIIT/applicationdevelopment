import os
from flask import Flask, render_template
from flask_restful import Resource, Api
from application import config
from application.config import LocalDevelopmentConfig, StageConfig
from application.database import db
from application import workers
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from application.models import User, Role
from flask_login import LoginManager
from flask_security import utils
from flask_sse import sse

# import logging
# logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app = None
api = None
celery = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    print(os.getenv('ENV', "development"))
    if os.getenv('ENV', "development") == "production":
      app.logger.info("Currently no production config is setup.")
      raise Exception("Currently no production config is setup.")
    elif os.getenv('ENV', "development") == "stage":
      app.logger.info("Staring stage.")
      print("Staring  stage")
      app.config.from_object(StageConfig)
      print("pushed config")
    else:
      app.logger.info("Staring Local Development.")
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
      print("pushed config")
    app.app_context().push()
    print("DB Init")
    db.init_app(app)
    print("DB Init complete")
    app.app_context().push()
    app.logger.info("App setup complete")
    # Setup Flask-Security
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    api = Api(app)
    app.app_context().push()   
    
    # Create celery   
    celery = workers.celery

    # Update with configuration
    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config["CELERY_RESULT_BACKEND"]
    )

    celery.Task = workers.ContextTask
    app.app_context().push()
    print("Create app complete")
    return app, api, celery

app, api, celery = create_app()


# Add all restful controllers
from application.api import ArticleLikesAPI
api.add_resource(ArticleLikesAPI, "/api/article_likes", "/api/article_likes/<int:article_id>")


from application.api import TestAPI
api.add_resource(TestAPI, "/api/test")

# This is for streaming
app.register_blueprint(sse, url_prefix='/stream')

# Import all the controllers so they are loaded
from application.controllers import *

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
