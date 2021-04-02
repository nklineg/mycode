#!/usr/bin/python3

'''Norm Kline | nklineg@gmail.com 
   Learning to Build OOP
'''

class Dog:
    def __init__(self, name, age):
        self.name = name # Dob.name is not the name passed to our class
        self.age = age   # Dog.age is now the age passed to our class

    def __str__(self):
        return f"Your dog, {self.name}, is {self.age}"

    def aged(self, yearsolder):
        self.age = self.age + yearsolder

def main():
    # create a doge
    d1 = Dog("Larry", 2)
    # display the doge
    print(d1)
    # what are you?
    print(type(d1))
    #what names are within this doge
    print(dir(d1))

    #print just the age attribute
    print(d1.age)
    # print just the name attribute
    print(d1.name)

    # make Larry the dog get 1 year older
    d1.aged(1)

    #larry should now be there
    print(d1)

if __name__ == "__main__":
    main()
