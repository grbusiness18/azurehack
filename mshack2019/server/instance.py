from flask import Flask, Blueprint
from flask_restplus import Api
from flask_cors import CORS
import settings
from werkzeug.contrib.fixers import ProxyFix


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(blueprint,
            version='1.0',
            title=settings.APP_TITLE,
            description=settings.APP_DESCRIPTION,
            doc = '',
            contact_email='Gokulraj.Ramdass@sap.com'
        )
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)
        CORS(self.app)
        self.app.register_blueprint(blueprint)

    def run(self):
        self.app.run(
                debug = False,
                port = settings.PORT,
                host = settings.HOST
            )


server = Server()