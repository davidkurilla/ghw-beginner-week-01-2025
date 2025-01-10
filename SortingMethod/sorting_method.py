
# Insertion sort function
def insertion_sort(array):
    
    for i in range(1, len(array)):
        
        temp = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
    
        array[j + 1] = temp

    return array

# TEST CODE

# Create an (array) list of numbers
unsorted_array = [9, 7, 5, 3, 1, 8, 6, 4, 2, 0]

print('Unsorted List:', unsorted_array)

# Sort the array
sorted_array = insertion_sort(unsorted_array)

print('Sorted List:', sorted_array)