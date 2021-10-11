from flask import jsonify, request
class FieldCreateDeveloperError(Exception):

    
    def __init__(self):
        data = request.json
        data = list(data)
        problem = [ i for i in data if i not in ["name","email","password","birthdate"] ]
        
        self.message = {
            "Message": {
                 "available_fields": [
                "name","email","password","birthdate",
                ],
            "Wrong_keys_sended": [*problem]
            }
                     
        }
        super().__init__(self.message)