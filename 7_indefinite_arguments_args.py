# Indefinite Arguments (*args) Practice #1
# *args = allows you ti pass multiple non-key argument
#**kwargs= akkws iu ri oass multiple keyword-arguments * unpacking operator
#1. positional 2. efault 3.keyword # ARBITARY

# def add(*args): # you add arg with the little star to make it have unlimited paralaments( did does NOT have to bename "args")
#     total=0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4,5,6,7,8,9,10)) # now you can add several num,ber of arguments


# def display_name(*args):
#     for arg in args:
#         print(arg,end="-") # this will ad 
# display_name("Dr", "Harold", "SQuarepants")

# def print_adress(**kwargs):
#     # pass # you need pass bc it epect omthing in the function
#     for key in kwargs.items():
#         print(f"{key}:{value}")
# print_adress(street="123 fake st",
#              city="chicago",
#              state="IL",
#              zip="456")

######something wrong with the one above 

# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end="")
#     print()
#     for value in kwargs.values():
#         print(value,end="")

# shipping_label("Dr", "spongbob"," squarepnats", "III",
#                street="123 fake st",  
#                  apt="100", 
#                  city="chicago",
#                  state="IL",
#                  zip="456")




# the args are the "names before thne equal sign"(key)

  # the kwargs are the "xxx" part (value) 











# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"