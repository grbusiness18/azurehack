
import os
import werkzeug
from flask import request
from flask_restplus import Resource, reqparse
from server.instance import server
from flask_restplus import abort
import settings
from processor import VisionProcessor

app, api = server.app, server.api

ns = api.namespace('hack', path='/v1', description='Intent Trainer APIs')

api.add_namespace(ns)

file_upload = reqparse.RequestParser()
file_upload.add_argument('file',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True,
                         help='upload .csv file with sentence,intent format')

@ns.route('/vision')
class VisionUpload(Resource):
    @ns.expect(file_upload)
    def post(self):
        args = file_upload.parse_args()
        print(args)
        if args['file'].mimetype == 'text/csv':
            destination = os.path.join(os.getcwd(), 'blobs/')
            if not os.path.exists(destination):
                os.makedirs(destination)
            csv_file = '%s%s' % (destination, 'dataset.csv')
            args['file'].save(csv_file)
        return {'status': 'Done'}, 201

    def get(self):
        VisionProcessor().process()
        return {}, 200



