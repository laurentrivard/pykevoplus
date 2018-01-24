class Lock(object):
    def __init__(self, id_: str, name: str, bolt_state: str):
        self.id = id_
        self.name = name
        self.bolt_state = bolt_state

    @classmethod
    def from_json(cls, json: dict):
        return cls(id_=json['id'],
                   name=json['name'],
                   bolt_state=json['bolt_state'])
