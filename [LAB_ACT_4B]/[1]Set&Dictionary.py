# Define the sets based on the provided Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g', 'h', 'k', 'j', 'i'}
B = {'b', 'c', 'l', 'm', 'o', 'h', 'i'}
C = {'c', 'd', 'f', 'i', 'h', 'j', 'k'}

# a. How many elements are there in set A and B
num_elements_A = len(A)
num_elements_B = len(B)

print ("===================================================")
print("Number of elements in set A:", num_elements_A)
print("Number of elements in set B:", num_elements_B)

# b. How many elements are there in B that is not part of A and C
not_in_A_C = B - (A | C)
num_not_in_A_C = len(not_in_A_C)

print("Number of elements in B that are not in A and C:", num_not_in_A_C)

# c. Show the requested lists using set operations
# i. [h, i, j, k]
set1 = { 'h', 'i', 'j', 'k' }
print("Set 1 (h, i, j, k):", set1)

# ii. [c, d, f]
set2 = { 'c', 'd', 'f' }
print("Set 2 (c, d, f):", set2)

# iii. [b, c, h]
set3 = { 'b', 'c', 'h' }
print("Set 3 (b, c, h):", set3)

# iv. [d, f]
set4 = { 'd', 'f' }
print("Set 4 (d, f):", set4)

# v. [c]
set5 = { 'c' }
print("Set 5 (c):", set5)

# vi. [l, m, o]
set6 = { 'l', 'm', 'o' }
print("Set 6 (l, m, o):", set6)
print ("===================================================")