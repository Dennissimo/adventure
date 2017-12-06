#! Python 3

class createCharacter:

    def __init__(self,name,gender,playerClass):
        self.name = input("Welcome! State your name:")
        createCharacter.determine_name(self)
        self.gender = input("State your gender! Choose between M or F:")
        createCharacter.determine_gender(self)
        self.playerClass = input("Choose your player class:")
        createCharacter.determine_playerClass(self)

    def determine_name(self):
        # self.name = input("Welcome! State your name:")
        print("The name you've entered is:" + self.name)

    def determine_gender(self):
        # self.gender = input("State your gender! Choose between M or F:")
        while True:
            if self.gender == 'M' or self.gender == 'F':
                print("Your gender is " + self.gender)
                break
            else:
                print("Error with input. Please choose between M or F")
                self.gender = input("State your gender! Choose between M or F:")
                continue

    def determine_playerClass(self):
        print("Your player class is " + self.playerClass)

charInit = createCharacter("","","")