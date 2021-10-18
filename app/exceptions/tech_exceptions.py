class TechNotFoundError(Exception):
    def __init__(self, avaliable_techs, techs_not_avaliable):
        self.message = {
            'technologies_added': [*avaliable_techs],
            'technologies_not_found': [*techs_not_avaliable]
        }
        
        super().__init__(self.message)