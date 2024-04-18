import copy

def shallowvsdeep():
    original_list = [[1,2],[3,4]]
    #shallow copy
    shallowCopy = copy.copy(original_list);
    shallowCopy[0][0] = 'a'
    print(original_list) #[['a', 2], [3, 4]]

    #deep copy
    original_list = [[1,2],[3,4]]
    #deep copy
    deepCopy = copy.deepcopy(original_list);
    deepCopy[0][0] = 'a'
    print(original_list) #[[1, 2], [3, 4]]


shallowvsdeep()
