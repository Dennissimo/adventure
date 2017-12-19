#! Python 3

class createCharacter:

    def __init__(self,name,gender,playerClass,playerAgility=0,playerJumpProwess=0,playerSpeed=0):
        self.name = input("Welcome! State your name:")
        createCharacter.determine_name(self)
        self.gender = input("State your gender! Choose between M or F:")
        createCharacter.determine_gender(self)
        self.playerClass = input("Choose your player class! Choose between [A]gile boii, [J]umpy boii or [F]asty boii:")
        self.playerAgility = playerAgility
        self.playerJumpProwess = playerJumpProwess
        self.playerSpeed = playerSpeed
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
                #continue

    def determine_playerClass(self):
        while True:
            if self.playerClass == 'A':
                self.playerAgility += 4
                self.playerJumpProwess += 2
                self.playerSpeed += 2
                print("Your player class is Agile boii")
                createCharacter.print_attributes(self)
                break
            elif self.playerClass == 'J':
                self.playerAgility += 2
                self.playerJumpProwess += 4
                self.playerSpeed += 2
                print("Your player class is Jumpy boii")
                createCharacter.print_attributes(self)
                break
            elif self.playerClass == 'F':
                self.playerAgility += 2
                self.playerJumpProwess += 2
                self.playerSpeed += 4
                print("Your player class is Fasty boii")
                createCharacter.print_attributes(self)
                break
            else:
                print("Error with input. Please choose between A, J or F")
                self.playerClass = input("Choose your player class! Choose between [A]gile boii, [J]umpy boii or [F]asty boii:")


    def print_attributes(self):
        print("Your agility is " + str(self.playerAgility))
        print("Your jump prowess is " + str(self.playerJumpProwess))
        print("Your speed is " + str(self.playerSpeed))

charInit = createCharacter("","","")