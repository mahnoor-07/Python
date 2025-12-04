# Lecture 11 - Aliasing & Cloning

# Making a copy of the list
"""Lcopy = L[:]
Equivalent to looping over L and apprnding each element to Lcopy
This does not make a copy of elements that are lists"""
def remove_all(L, e):
    # make a copy
    Lnew = L[:]
    # clear the list
    L.clear()
    # add back elements that do not equal in e
    for n in Lnew:
        if e != n:
            L.append(n)

Lin = [1,2,2,2]
remove_all(Lin,2)
print(Lin)

# Operation on list - remove 
"""delete element at the specific index with del(L[index])
remove the element at the end of the list with L.pop()
remove a specific element with L.remove(element)"""
def remove_all(L, e):
    for elem in L:
        if elem == e:
            L.remove(e)

Lin = [1,2,2,2]
remove_all(Lin,2)
print(Lin)

def remove_dup(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

L1 = [10,20,30,40]
L2 = [10,20,50,60]
remove_dup(L1,L2)
print(L1)