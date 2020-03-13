#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    if length == 2 and (weights[0] + weights[1] == limit):
        return (1, 0)
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    for w in weights:
        retrieve_index = hash_table_retrieve(ht, limit - w)
        if retrieve_index is not None:
            this_index = hash_table_retrieve(ht, w)
            if retrieve_index < this_index:
                return (this_index, retrieve_index)
            else:
                return (retrieve_index, this_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
