class TechNotFoundError(Exception):
    def __init__(self, avaliable_techs, techs_not_avaliable):
        print(avaliable_techs, 'M<<< exception')
        self.message = {
            'message': 'developer created with success',
            'technologies_added': [*avaliable_techs],
            'technologies_not_found': [*techs_not_avaliable]
        }
        
        super().__init__(self.message)