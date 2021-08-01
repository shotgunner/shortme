from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from uuid import uuid4
from model import db, URL, app

api = Api(app)


class ShortURL(Resource):
    def get(self):
        request_url = request.args.get("url")
        if request_url:
            url = URL(url=request_url, short=uuid4().hex[:6])
            db.session.add(url)
            db.session.commit()
            response = jsonify({"short": url.short})
            response.status_code = 200
            return response
        return "url must not be empty", 400


api.add_resource(ShortURL, '/short')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
