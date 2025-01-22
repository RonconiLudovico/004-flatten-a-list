def list_flattener(data):
    if not data:
        return []
    
    if type(data[0]) == list:
        l1 = list_flattener(data[0])
        l2 = list_flattener(data[1:])
        return l1 + l2
    
    else:
        l1 = [data[0]]
        l2 = list_flattener(data[1:])
        return l1 + l2


if __name__ == "__main__":
    non_flattened_list = [1, [2, 3], [4, [5, 6]], [7, 8]]
    print(list_flattener(non_flattened_list)) # [1, 2, 3, 4, 5, 6, 7, 8]