from flask import request, jsonify

class FieldCreateContractorError(Exception):
    def __init__(self):
        data = request.json
        data = list(data)
        problem = [ i for i in data if i not in ["name","email","password","cnpj"] ]
        self.message = {
            "Message": {
                 "available_fields": [
                "name","email","password","cnpj",
                ],
            "Wrong_keys_sended": [*problem]
            }
        }
        super().__init__(self.message)