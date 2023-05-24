def create_an_empty_list():
    return []

# This function should use the literal constructor to create a new list, just like we did above. 
# This time, however, create a list that contains four elements. 
# The four elements can be any elements of your choosing, as long as there are only four of them.
def create_a_list():
    new_list = ['peach', 'flower', 'clock', 'shoe']
    return new_list
# print(create_a_list())

# This function takes in two arguments, a list and the element we want to add to it. 
# Use the append() to add that element to the end of the new list.
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

# print(add_element_to_end_of_list(['peach', 'flower', 'clock', 'shoe'], "cup"))

# This function takes in two arguments, a list and the element we want to add to it. 
# Use the insert() method to add that element to the start of that list.
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

# This function takes in one argument, the list on which we want to operate. 
# Use the pop()method to remove the last item from the list.
def remove_element_from_end_of_list(l):
    l.pop()
    return l
# This function takes in one argument, the list on which we want to operate. 
# Use the del keyword to remove the first item from the list.
def remove_element_from_start_of_list(l):
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    last = len(l)-1
    return l[last]
