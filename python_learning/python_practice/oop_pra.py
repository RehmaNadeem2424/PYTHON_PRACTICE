#class Car:
    # class variable or static variable:
    #tire = 4
   # def __init__(self, color,model,company_n):
        # class instance or dynamic variables:
        #self.color = color
        #self.model = model
        #self.company_n = company_n
   # def driving(self):
       # print('the car is driving')
   # def loading(self,material):
       # print(f"the car is loading {material}")
   

#Car1 = Car("red" , 2023 , "honda")
#print(Car1.color)
#print(Car1.model)
#print(Car1.company_n)
#Car1.driving()
#Car1.loading("food")
#print()
#Car2 = Car("white",2022 , "tesla")
#print(Car2.color)
#print(Car2.model)
#print(Car2.company_n)
#Car2.driving()
#Car2.loading("mirror")
#print()



#INHERITANCE:


#
#class Animal:
    #def __init__(self, name, age):
       # self.name = name
       # self.age = age
    
   # def speak(self):
       # print("animal can speak")

#class Dog(Animal):
    #def bark(self):
        #print("dog bark")

#d1 = Dog('tommy',4)
#print(d1.age)
#d1.bark()
#d1.speak()

# multiple inheritance

#class Father(object):
   # def Display(self):
        #print("this is father class")
   # def Guide(self):
       # print("this is guide method of father class")

#class Mother(object):
    #def Display(self):
       # print("this is mother class")
    #def Guide(self):
       # print("this is guide method of mother class")

#class Son(Father,Mother):
   # def print(self):
       # print("this is son class")
   # def play(self):
       # print("this is play method of child class")
      

#s1 = Son()
#s1.print()
#s1.play()
#print()
#print("father function")
#s1.Display()
#s1.Guide()
#print()
#print("mother function")
#s1.Display()
#s1.Guide()

# MULTILEVEL INHERITANCE:

 
# class Father(object):
#     def Display(self):
#         print("this is father class")
#     def Guide(self):
#         print("this is guide method of father class")

# class Mother(object):
#     def Display(self):
#         print("this is mother class")
#     def Guide(self):
#         print("this is guide method of mother class")

# class Son(Father,Mother):
#     def print(self):
#         print("this is son class")
#     def play(self):
#         print("this is play method of child class")
      

# s1 = Son()
# s1.print()
# s1.play()
# print()
# print("father function")
# s1.Display()
# s1.Guide()
# print()
# print("mother function")
# s1.Display()
# s1.Guide()


# HIERARCHICAL INHERITANCE:

