class animal:
    def __init__(self, diet, name, waterlogged):
        self.diet = diet
        self.name = name
        self.waterlogged = waterlogged

    def breath_air(self):
        if self.waterlogged == True:
            return False
        else:
            return True

class cage:
    def __init__(self, occupant, capacity):
        self.occupant = occupant
        self.capacity = capacity

