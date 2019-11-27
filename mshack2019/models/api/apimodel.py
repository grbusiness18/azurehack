from flask_restplus import fields
from server.instance import server

sentence_req_model = server.api.model('sentence_req_model', {
    'sentence_id': fields.String(required=True),
    'sentence': fields.String(description='sentence')})


sentence_req_model_single = server.api.model('sentence_req_model_single', {
    'sentence': fields.String(description='sentence')})


intent_req_model = server.api.model('intent_req_model', {
    'intent'   : fields.String(description='intent_name', required=True),
    'sentences': fields.List(fields.String(description='sentences'), required=True)})
