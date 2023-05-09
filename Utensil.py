class Utensil: 
   

    def __init__(self, type, material):
        self.type == type
        self.material == material

    def cut(self):
        if self.type == "knife":
            print("I am a knife, I will cut.")
        elif self.type == "fork":
            print("I am a fork.")
        else:
            print("I cant cut.")

    def pickup(selfie):
        if selfie.type == "knife":
            print("I am a knife, I pick up by stabbing.")
        elif selfie.type == "fork":
            print("I am a fork, I pick up by poking.")
        else:
            print("I am a spoon, I pick up by scooping.")