class InvalidFormatToBirthdateError(Exception):
    
     def __init__(self):
        
        self.message = 'Birthdate must be in this format: dd/mm/yyyy'
        
        super().__init__(self.message)


