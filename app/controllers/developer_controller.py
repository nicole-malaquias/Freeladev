from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)

def create_profile():
    ...


@jwt_required()
def get_profile_info():
    ...

@jwt_required()
def update_profile_info():
    ...

@jwt_required()
def delete_profile():
    ...


def get_all_developers():
    ...


    

