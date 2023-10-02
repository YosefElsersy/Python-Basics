def binarySearch(array, search, lowIndex, highInex):

    while lowIndex <= highInex:
        mid = lowIndex +(highInex - lowIndex) // 2 #floor()
        
        if array[mid] == search:
            return mid

        elif array[mid] < search:
            lowIndex = mid + 1

        else:
            highInex = mid - 1

    return -1

# Sorted Array
grades = [10, 12, 14, 15, 17, 19, 20] # length = 7
search = 20

# Linear Search
# Best Case : O(1)
# Worst Case : O(n) => O(7)

# Binary Search
# O(log n )


result = binarySearch(grades, search, 0, len(grades) - 1)

if result == -1:
    print("Not Found")
else:
    print("Found")