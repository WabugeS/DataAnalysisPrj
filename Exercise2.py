#1,2,3,4,5
#class student : 
#    def __init__(self,name,age) :
#        self.name= name
#        self.age = age
#student1=student("Duaa",23)
#student2=student("Sarah",22)
#print(student1.name)

#6,7,8
class student : 
    def __init__(self,name,age,grade=None):
        self.name= name
        self.age = age
        self.grade= grade
#9        
    def introduce(self):
         print("Hello my name is ", self.name , " and i am ", self.age ," years old")
#11
    def is_adult(self):
        if self.age>=18:
            print("Adult")
        else:
            print("Minor")
#28
    def IncreaseAge(self):
        self.age+=1
        print("You are", self.age)

student1=student("Ali",21,"B")
print(student1.grade)
student1.grade="A+"
print(student1.grade)
#10
student1.introduce()
#11
student1.is_adult()
#12
student2=student("max",24)
student3=student("Sophie",22)
student4=student("Sarah",20) 
students=[student2,student3,student4]

#13
for a in students: 
    print(a.name)
#14
for i in students:
    i.introduce()
#28
student3.IncreaseAge()

#oop
#15
class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
#17
    def drive(self):
        print("The car is driving at ",self.speed,"km/h")
#29
    def IncreaseSpeed(self,NewSpeed):
        self.speed+=NewSpeed
        print("New Speed is", self.speed,"km/h")
#16
car1=car("Mercedes",80)
car2=car("Toyota",120)
#18
car1.drive()
car2.drive()
car1.IncreaseSpeed(20)
#19 
class BankAccount:
#20
    def __init__(self,balance):
        self.balance= balance
#21
    def Deposit(self,amount):
        self.balance+=amount
        print("Your new balance is ", self.balance)

#22
    def Withdraw(self,amount):
        self.balance=self.balance-amount
        print("Your new balance is ", self.balance)
#23 
BankAccount1=BankAccount(0)
BankAccount1.Deposit(2000)
BankAccount1.Withdraw(200)
#24In your own words, explain what a class is.
#a class is a blueprint for the objects belonging to it.

#25 In your own words, explain what an object is.
#an object is an instance of a class
#it has the attributs defined by the class.

#26 What is the purpose of the __init__ method?
#it setups the data for the objects of the class.

#27What does self represent?
#self identifies the currect object.

class Anime:
    def __init__(self,genre, season):
        self.genre = genre
        self.season = season
    def AnimeInfo(self,name):
        self.name=name
        print("You are watching season",self.season,"of",self.name)
        print(self.name,"is a",self.genre,"anime") 
g1=input("What is the genre of this Anime?")
S1=input("What is the current season")
anime1 = Anime(g1, S1)
g2=input("What is the genre of this Anime?")
S2=input("What is the current season")
anime2 = Anime(g2, S2)

anime1.AnimeInfo("Attack On Titan")
anime2.AnimeInfo("Death Note")