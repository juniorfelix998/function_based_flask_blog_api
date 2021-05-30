from flask import Blueprint, request
from core.utils.responses import response_with
from core.utils import responses as resp
from posts.model import Posts
from posts.shema import PostSchema

post_routes = Blueprint('post_routes', __name__)


@post_routes.route('/', methods=['GET'])
def get_post_list():
    fetched = Posts.query.all()
    post_schema = PostSchema(many=True)
    posts = post_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'posts': posts})


@post_routes.route('/', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        post_schema = PostSchema()
        post = post_schema.load(data)
        result = post_schema.dump(post.create())
        return response_with(resp.SUCCESS_201, value={'post': result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
