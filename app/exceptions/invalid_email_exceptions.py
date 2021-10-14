class InvalidEmailError(Exception):
    
     def __init__(self, data):
        
        self.message = {
            "Message": "The format is not valid for email adress",
            "Wrong_keys_sended": [data['email']]          
        }
        super().__init__(self.message)


