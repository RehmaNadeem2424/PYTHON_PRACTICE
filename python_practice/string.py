# INDEXING:
bio = "My name is hayat my age is : 21 currently , i completed my graduation"
print("initial string" , bio)
print(bio[0])
print(bio[3])
print(bio[8])
print(bio[11])
print(bio[17])
print(bio[20])
print(bio[24])
print(bio[29])
print(bio[32])
print(bio[44])
print(bio[46])
print(bio[56])
print(bio[59])

# SLICING:
bio = "My name is hayat.I am 21 years old.and i live in lahore.I have a growing interest in programming and love exploring how technology can solve real world problems.i am passionate about learning new things and spend alot of time improving my coding skills."
print("initial string" , bio)
print(bio[0:17])
print(bio[17:35])
print(bio[35:56])
print(bio[56:161])
print(bio[161:253])

# REVERSE
message = "Every line of code I write is a step closer to turning my dreams into reality"
print("intial string" , message)
print(bio[0:75:2])

# NEGATIVE INDEXEING:
message = "Every line of code I write is a step closer to turning my dreams into reality"
print("intial string" , message)
print(bio[::-1])

# ESCAPE SEQUENCE:
quote1 = "\"Quaid e azam\"said: \n\t\t\tfailure is a word unknow to me."
print(quote1)
quote2 = "\"Quaid e azam Muhammad Ali jinnah\"said :\n\t\t\t\t\t With faith , discipline and selfless devotion to duty, there is nothing worthwhile that you cannot achieve."
print(quote2)
quote3 = "\"Colin powell\" said :\n\t\t\tperpetual optimism is a force multipiler."
print(quote3)
quote4 = "\"Quaid e azam\" said: \n\t\t\t I shall never come to the punjab again;it ia such a hopeless place."
print(quote4)
quote5 = "\"Joe jackson\"said:\n\t\tIf you build it, they will come."
print(quote5)
quote6 = "\"Mark Twain\" said:\n\t\t\t The secret of getting ahead is getting started."
print(quote6)
quote7 ="\"Artin luther king jr\"said:\n\t\t\t In justice anywhere is a threat to justice everywhere."
print(quote7)
quote8 = "\"Mother Teresa\":\n\t\tNot all of us can do great things.but we can do small things with great love"
print(quote8)
quote9 = "\"Helen Keller\"said :\n\t\t\tThe only thing worse than being blind is having sight but no vision."
print(quote9)
quote10 = "\"Franklin D. Roosevelt\" said: \n\t\t\t\tThe only thing we have to fear is fear itself."
print(quote10)

# STRING CHANGE INTO LIST:

name = "Raha"
print(name)
list1 = list(name)
print(list1)
name2 = "Sara"
print(name2)
list2 = list(name2)
print(list2)
message = "Nothing is impossible"
print(message)
list3 = list(message)
print(list3)
fruit = "Apple"
print(fruit)
list4 = list(fruit)
print(list4)
bird = "peacock"
print(bird)
list5 = list(bird)
print(list5)

# STRING CHANGE INTO TUPLE:

name = "Maha"
print(name)
tuple1 = tuple(name)
print(tuple1)
name2 = "Hayat"
print(name2)
tuple2 = tuple(name2)
print(tuple2)
message = "Nothing is impossible"
print(message)
tuple3 = tuple(message)
print(tuple3)
fruit = "Cherry"
print(fruit)
tuple4 = tuple(fruit)
print(tuple4)
bird = "peacock"
print(bird)
tuple5= tuple(bird)
print(tuple5)

# STRING CHANGE INTO SET:

name = "Maha"
print(name)
set1 = set(name)
print(set1)
name2 = "Hayat"
print(name2)
set2 = set(name2)
print(set2)
message = "Nothing is impossible"
print(message)
set3 = set(message)
print(set3)
fruit = "Cherry"
print(fruit)
set4 = set(fruit)
print(set4)
bird = "peacock"
print(bird)
set5= set(bird)
print(set5)