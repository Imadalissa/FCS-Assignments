def add_to_sort(integers, int1_4):

    for index in range(len(integers)):
        if int1_4 <= integers[index]:
            integers.insert(index, int1_4)
            return integers
    

    integers.append(int1_4)
    return integers

# Example usage
print(add_to_sort([1, 2, 4, 6, 32, 45, 76, 99, 110], 55))  
print(add_to_sort([1, 3, 5, 7, 9], -1))  
print(add_to_sort([10, 20, 30], 25))  
print(add_to_sort([10, 20, 30], 40))  