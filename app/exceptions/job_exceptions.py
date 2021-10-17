from flask import request

class FieldCreateJobError(Exception):
    def __init__(self):
        
        data = request.json
        data = list(data)

        problem = [ i for i in data if i not in ["name","description","price","difficulty_level", "expiration_date", "contractor_id", "developer_id"] ]
        
        self.message = {
            "Message": {
                 "available_fields": [
                "name","email","password","cnpj",
                ],
            "Wrong_keys_sended": [*problem]
            }
        }
        super().__init__(self.message)
        