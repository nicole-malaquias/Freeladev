<<<<<<< HEAD:app/exceptions/invalid_field_create_developer_exceptions.py
from flask import jsonify, request
class FieldCreateDeveloperError(Exception):
=======
from flask import request, jsonify
>>>>>>> 5945dfd675c19b3901aaa80c855b3d92d2c29586:app/exceptions/contractor_exceptions.py

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