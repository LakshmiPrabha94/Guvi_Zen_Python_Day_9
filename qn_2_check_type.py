#Name: Lakshmi Prabha
#Program : Write a code Check every element of a list is a string or an integer using lambda function
#Version: 1
#Pragramming language: Python
#Python Version: 3.12.0

def check_elements_type(lst):
    
    # Use a lambda function to print the type of each element
    #result = lambda x: print("Type of element {}: {}".format(x, type(lst[x])))

    result = lambda lst: print("Type of element: ", type(lst))

    # Apply the lambda function to each element in the list
    #list(map(result, range(len(lst))))
    list(map(result, lst))


# Sample list:
my_list = [1, "hello", 42, 7.45, "guvi.in!"]

# Check and print the type of each element
check_elements_type(my_list)

