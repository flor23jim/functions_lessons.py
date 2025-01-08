# def check_3_digits(numbers):
#     return numbers in range( 100,1000)
# result=check_3_digits(105)
# print(result)

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             pass # it will keep passing to nothing/ if not its "nonetype"
# result=check_3_digits([55,99,6000])
# print(type(result))

# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#            return False
# result=check_3_digits([55,99,600]) # it will return false unless the first and last number are true
# print(result)

# def check_3_digits(list1):
#     three_digit_list=[]
#     for n in list1:
#         if n in range(100,1000):
#             three_digit_list.append(n)
#         else:
#            pass
#     return False
# result=check_3_digits([55,99,600])
# print(result)

# coffee_prices= [('cappuccino',1.5),('espresso',1.2),('mocha',1.9)]

# def most_expensive_coffee(list_of_prices):
#     highest_price=0
#     my_most_expensive_coffee =''
#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price=price 
#             my_most_expensive_coffee = coffee 
#         else:
#             pass
#     return (my_most_expensive_coffee, highest_price)
# print(most_expensive_coffee(coffee_prices)) 



# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
# number=[1,2,3] # list of number 
# def all_positive(number): # the function 
#     for n in number: # created to see what number are inside 
#         if n < 0:  # if they are less than 0 they negative 
#             return False
#     return False






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
# num= [300,50,500] # list of number 
# def sum_less(num): # create function 
#     total=0 
#     for n in num: # defining function 
#         if n> 0 and n <1000:
#             total +=n
#     return total 
# print(sum_less(num))




# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

# def count_even(first):

# def count_even(numbers):
#     even_numbers=0
#     for n in numbers:
#         if n%2 ==0:
#             even_numbers = even_numbers+1
#         else:
#             pass
#     return even_numbers
# variable= [124,43,5343]