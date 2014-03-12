class CatDog(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
	
    def age_group(self):
        if self.age<=1:
            return "0-1"
        elif 1<self.age<=3: 
            return "1-3"
        elif 4<self.age<=7:
            return "4-7"
        elif 7<self.age<=11:
            return "7-11"
        else: 
            return "11+"

class CatDogA(CatDog):
    def __init__(self, name, age, gender, breed=xy, color=white):
        self.name = name
        self.age = age
        self.gender = gender
	    self.breed = breed
	    self.color = color

class CatDogB(CatDog):
    def __init__(self, name, age, gender, breed=ab, color=orange):
        self.name = name
        self.age = age
        self.gender = gender
	    
	


if __name__=="__main__":
    AM1 = CatDogA("Max", 1, Male)
    AM2 = CatDogA("Rex", 3, Male)
    AM3 = CatDogA("Johnny", 5, Male)
    AM4 = CatDogA("Rufus," 8, Male)
    AM5 = CatDogA("Sam," 13, Male)
    AF1 = CatDogA("Lady," 0, Female)
    AF2 = CatDogA("Maggie" 2, Female) 
    AF3 = CatDogA("Chelsie," 6, Female) 
    AF4 = CatDogA("Brandy," 9, Female) 
    AF5 = CatDogA("Lassie," 14, Female)
    BM1 = CatDogB("Bear", 1, Male)
    BM2 = CatDogB("Buddy", 2, Male)
    BM3 = CatDogB("Admiral", 6, Male)
    BM4 = CatDogB("Hercules", 10, Male)
    BM5 = CatDogB("Lord James", 16, Male)
    BF1 = CatDogB("Taffy", 0, Female)
    BF2 = CatDogB("Lavender", 2, Female)
    BF3 = CatDogB("Rose", 5, Female)
    BF4 = CatDogB("Lollipop", 9, Female)
    BF5 = CatDogB("Evian", 15, Female)
   