#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    -finds two items whose sum of weights equals the weight limit `limit`.
    -Your function will return an instance of an `Answer` tuple that has the following form:
    (zero, one)
    -where each element represents the item weights of the two packages. 
    **The higher valued index should be placed in the `zeroth` index and 
    the smaller index should be placed in the `first` index.**_ 
    -If such a pair doesn’t exist for the given inputs, your function should return `None`.
    """
    for i in range(len(weights)):
        div = hash_table_retrieve(ht, limit - weights[i])
        if div is not None:
            if div > i:
                return div, i
            else:
                return i, div
        hash_table_insert(ht, weights[i], i)
    # When calling `hash_table_retrieve` with a key that doesn't exist in the hash table, 
    # `hash_table_retrieve` will return `None`.
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
