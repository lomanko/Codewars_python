'''
You will be given an array of numbers. 
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

'''

def sort_array(source_array):
    odd_array = [number for number in source_array if number % 2 != 0]
    odd_array.sort()
    index = 0
    sorted_array = []
    for number in source_array:
        if number % 2 == 0: 
            sorted_array.append(number)
        else:
            sorted_array.append(odd_array[index])
            index += 1
    return sorted_array
