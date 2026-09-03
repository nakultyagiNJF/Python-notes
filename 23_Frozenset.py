# Different between 'set' and 'FrozenSet' in Python:

# set is mutable, meaning we can add or remove items after its creation.

# Example:
my_set = {'apple', 'banana', 'cherry'}
my_set.add('orange')  # Adding an item to the set
print(my_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# frozenset is immutable, meaning once it is created, we cannot change its items.

# Example:
my_frozenset = frozenset(['apple', 'banana', 'cherry'])
# my_frozenset.add('orange')  # This will raise an AttributeError
print(my_frozenset)  # Output: frozenset({'apple', 'banana', 'cherry'})
# Both 'set' and 'frozenset' support operations like union, intersection, and difference.