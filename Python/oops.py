"creating class is same as creating function and inside a class if we initialize a variable"
" that variable is called attributes and similarly if we initialize a function inside the class then"
" that function will be called as method"

# class Factory:
#     a = 12 #attribute

#     def hello(self): #method
#         print("method")

# "this is a normal variable and if we initialize a class in it then it will become object which has all the access to class"
# obj = Factory()

# print(obj.a)
# obj.hello()

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# "Constructor"
# class Factory:

#     "Here the self is a loaction it will find the location in the RAM where the objects are stored and"
#     "it will fetch the value of the objects which are initialized inside the parameter of a method"
#     def __init__(self,material,pockets,chain):
#         self.material = material #this means fetch the material value which are stored in the location rebook and similary next ones as well
#         self.pockets = pockets
#         self.chain = chain
    
#     "this method will show all the values initiazed for the parameter"
#     def show(self):
#         print(f"Your object details are {self.material}, {self.pockets}, {self.chain}")

# rebook = Factory('Leather',2,1)
# nike = Factory('Pure leather',3,1)

# rebook.show()
# nike.show()

"Types of attributes and method"
# class Animal:

#     def __init__(self,age):
#         self.age = age  #intance attribute because it is defined with self which targets objects

#     def show(self): #instance method that targets object location and it passes self parameter
#         print(f"Your age is {self.age}")

#     @classmethod
#     def hello(cls): #this is a class method meaning it targests directly class 
#         print("Accessing class data")
    
#     @staticmethod
#     def static(): #works as a normal method it cannot access class nor object.
#         print("static method")

# obj = Animal(26)

# obj.show()
# obj.hello()
# obj.static()

"Multilevel inheritance"
# class Factory: #Grandparent
#     def __init__(self,material,pockets):
#         self.material = material
#         self.pockets = pockets

# class ChicagoFactory(Factory): #Parent
#     def __init__(self, material, pockets,color):
#         super().__init__(material,pockets)
#         self.color = color

# class ParisFactory(ChicagoFactory): #child
#     def __init__(self, material, pockets, color,zips):
#         super().__init__(material, pockets, color)
#         self.zips = zips

# obj = ChicagoFactory() #only fetch the attributes which are defined inside the method


"Lambda function"

result = lambda x : x*2
print(result(2))


a = [2,3,4,5]

add = map(lambda x : x + 1,a)

print(list(add))