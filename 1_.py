#functions are ways to wap your code into reusable units 
#function= a block of reusable code 
#       place()after te function name to involve it


def happy_birthday(name,age):  #define a functin ad then call function  # added another parameter with a "," 
# the (Name) is the parament/ place holder - there doesn't have to have a place holder for the function to work 
# if you make a parameter when you are calling it you have to add a arugment or else it doesnh't run- saying something missing
    print(f"happy birthday to you {name}!")
    print(f'you are {age} old!')
    print("hapy birthday to you!")
    print()
happy_birthday ("boy",20) # this is where you call/ invoke the function
happy_birthday ("bro",30) #in this situation the "name" could be chnaged with any name you like inside the parathensis 
# ("name")-- is the argument, so you call it # added a new agrument. You also have to have your paramenter and agrument in the same order for it to work correctly
happy_birthday ("gurl",40) 
#above we are calling the function three times and could be called as many time as you qould like as long as yo write the function

def display_invoice(username,amount,due):
    print(f"hello {username}")
    print(f"your bill of ${amount:.2f} is due:{due}")
display_invoice("yep.23",426.7,"01/01")


#################################################

#return = statement used to end a function and send a result back to the caller

def add (x,y):
    z = x +y 
    return z
def subtract (x,y):
    z= x-y
    return z
def mutiply (x,y):
    z = x *y
    return z
def divide (x,y): 
    z= x/y
    return z

print (add(1,2))
print(subtract(1,2))
print(mutiply(1,2))
print(divide(1,2))

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last 

full_name= create_name("flor","jimenez")
print(full_name)