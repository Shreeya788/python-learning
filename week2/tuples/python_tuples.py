'''
Tuples can accept anu mix of data types and can range from integer like one, to string, to double, to boolean.

We can access tuples using Index or count function.

we could also declare tuple without the parenthesis whereas using parenthesis is considered best practice for tuples.

One difference between tuples and lists is that tuples are immutable.that means they cannot be changed.

 

'''

my_tuples = (1, 'strings', 1.25, True)
print(my_tuples[0]) # prints 1--> first index of the tuple
print(my_tuples.count('strings')) # this returns the count of the tuples
print(my_tuples.index(1.25)) # this returns the index of the tuples