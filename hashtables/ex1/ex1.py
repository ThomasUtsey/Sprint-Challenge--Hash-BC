#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for index in range(length):
        hash_table_insert(ht,index,(weights[index],limit-weights[index]))
    for index in range(length):
        weight, needed_weight = hash_table_retrieve(ht,index)

        for jndex in range(index+1,length):
            weights, _ = hash_table_retrieve(ht,jndex)

            if weight == needed_weight:
                if index > jndex:
                    return (index,jndex)
                else:
                    return (jndex,index)
                            
                #  return index,jndex if index > jndex else jndex,index



    return None
    def get_indices_of_item_weights_(weights, length, limit):
        ht = HashTable(16)
        for index in range(length):
            hash_table_insert(ht,weight,index)
    
        for index in range(length):
            weight = weights[index]
            first = hash_table_retrieve(ht,weight)
            needed_weight = limit - weight
            second = hash_table_retrieve(ht,needed_weight)
            hash_table_insert(ht, weight, index)

            for jndex in range(index+1,length):
                weights, _ = hash_table_retrieve(ht,jndex)

            if second:
                if first > second:
                    return (first,second)
                else:
                    return (second,first)
                            
                #  return index,jndex if index > jndex else jndex,index



    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
