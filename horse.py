class Horse():
    def __init__(self, name, breed, rider, kicks):
        self.name = name
        self.breed = breed
        self.rider = rider
        self.kicks = kicks

class Rider():
    def __init__(self, name, mask):
        self.name = name
        self.mask = mask
        

ranger = Rider("The Lone Ranger", "Who was that masked man?")
silver = Horse("Silver", "Stallion", ranger, "yes")

print(silver.rider.mask)
print(silver.rider.name)
