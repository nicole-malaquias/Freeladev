class InvalidPasswordError(Exception):
    
     def __init__(self, data):
        
        self.message = {
            "Message": "The format is not valid and is not secury",
            "Wrong_keys_sended": [data['password']]          
        }
        super().__init__(self.message)


