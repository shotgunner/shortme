from flask import request, redirect, abort
from flask_restful import Resource, Api
from model import URL, app

api = Api(app)


class RedirectURL(Resource):
    def get(self):
        request_url = request.args.get("short")
        urls = URL.query.filter_by(short=request_url).all()
        if urls:
            return redirect(urls[0].url)
        abort(404)


api.add_resource(RedirectURL, '/redirect')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
