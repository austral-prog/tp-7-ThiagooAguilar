def index_of_by_index(word, list, index):
    i=index
    while i < len(my_list):
        if my_list[i]==word:
            return i
        i+=1
    return -1


def index_of_empty(list):
    return -1


def index_of(word, my_list):
    i=0
    while i < len(my_list):
        if my_list[i]==word:
            return i 
        i+=1
    return -1


def put(word, list):
    return -1


def remove(word, list):
    return -1
