from flask_restful import fields

lock_fields = {
    'id': fields.String(),
    'name': fields.String(),
    'boltState': fields.String(attribute='bolt_state')
}