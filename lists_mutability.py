# Lecture 10 - Lists and Mutability

# OPERATION ON LIST
"""Append - Add an element in the end of the list with 
L.append(element)"""
L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.append(L4)
L = L1.append(L3)

def make_ordered_list(n):
    mylist = []
    for i in range (0, n+1):
        mylist.append(i)
    return mylist

print(make_ordered_list(3))


def remove_elem(L, e):
    newlist = []
    for i in L:
        if i != e:
            newlist.append(i)
    return newlist


L = [1,2,2,2]
print(remove_elem(L, 2))
L = [1,2,2,2]
print(remove_elem(L, 1))
L = [1,2,2,2]
print(remove_elem(L, 0))

# STRING TO LIST
"""Use s.split(), to split a string on a charachter parameter,
splits on spaces if called without parameter"""
# LIST TO STRING
"""Use ''.join(L) to turn the list of strings into the bigger string"""
def count_words(sen):
    L1 = sen.split(' ')
    return len(L1)

s = "Hello it's me"
print(count_words(s))

# Sort
def sort_words(sen):
    L = sen.split(' ')
    L.sort()
    return L

s = "look at this photograph"
print(sort_words(s))