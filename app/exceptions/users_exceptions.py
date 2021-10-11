class UserNotFoundError(Exception):
    def __init__(self):
        
        message = 'User not found. Make sure you send correct email and password'
        
        super().__init__(message)