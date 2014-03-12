class CatDog(object):
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
	    self.weight = weight
	
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
    def __init__(self, name, age, gender, weight, breed=xy, color=white):
        self.name = name
        self.age = age
        self.gender = gender
	    self.weight = weight
	    self.breed = breed
	    self.color = color

class CatDogB(CatDog):
    def __init__(self, name, age, gender, weight, breed=ab, color=orange):
        self.name = name
        self.age = age
        self.gender = gender
	    self.weight = weight
	


if __name__=="__main__":
    a = CatDogA("Michele", 1, Female, 8)
    b = CatDogB("Rex", 7, Male, 17)
    c = CatDogA("Johnny", 11, Male, 14)
    d = CatDogB("Kelly," 14, Female, 11)

   