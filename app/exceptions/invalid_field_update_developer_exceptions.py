from flask import jsonify, request


class FieldUpdateDeveloperError(Exception):
    
    def __init__(self):
        data = request.json
        data = list(data)
        problem = [ i for i in data if i not in ["name","email","password","birthdate", "technologies"] ]
        
        self.message = {
            "Message": {
                 "available_fields": [
                "name","email","password","birthdate", "technologies"
                ],
            "Wrong_keys_sended": [*problem]
            }
                     
        }
        super().__init__(self.message)