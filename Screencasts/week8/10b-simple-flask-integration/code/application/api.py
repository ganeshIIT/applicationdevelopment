from flask_restful import Resource, Api
from flask_restful import fields, marshal
from flask_restful import reqparse
from application.validation import BusinessValidationError, NotFoundError
from application.models import ArticleLikes
from application.database import db
from flask import current_app as app
import werkzeug
from flask import abort
from flask_security import auth_required, login_required, roles_accepted, roles_required, auth_token_required

article_likes_resource_fields = {
    'user_id':   fields.Integer,
    'article_id':    fields.String,
}

create_article_likes_parser = reqparse.RequestParser()
create_article_likes_parser.add_argument('user_id')
create_article_likes_parser.add_argument('article_id')

class ArticleLikesAPI(Resource):
    @auth_required("token")
    def post(self):
        args = create_article_likes_parser.parse_args()
        article_id = args.get("article_id", None)
        user_id = 1 # current user
        # Do all the validation
        new_like = ArticleLikes(user_id=user_id, article_id=article_id)
        db.session.add(new_like)
        db.session.commit()
        return marshal(new_like, article_likes_resource_fields)


test_api_resource_fields = {
    'msg':    fields.String,
}

class TestAPI(Resource):
    @auth_required("token")
    def get(self):
        return marshall({"msg":"Hello World"}, test_api_resource_fields)
