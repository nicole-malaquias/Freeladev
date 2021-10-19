class InvalidEmailError(Exception):
    
     def __init__(self):
        
        self.message = 'The format is not valid. Try send an email with @ and .'
        
        super().__init__(self.message)


