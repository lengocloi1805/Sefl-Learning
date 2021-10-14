class Person1:
    def __init__(self, ID, Name, DayofBirth, BirthPlace):
        self.ID = ID
        self.Name = Name
        self.DayofBirth = DayofBirth
        self.BirthPlace = BirthPlace

    def printx(self):
        print(self.ID, ' ', self.Name, ' ', self.DayofBirth, ' ', self.BirthPlace)
