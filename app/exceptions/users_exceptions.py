class UserNotFoundError(Exception):
    def __init__(self):
        
        message = 'User not found. Make sure you send the correct email!'
        
        super().__init__(message)
        

class InvalidPasswordError(Exception):
    def __init__(self):
        
        message = 'Make sure you send the correct password!'
        
        super().__init__(message)
        

